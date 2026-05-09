"""test_user_profile.py - 用户画像 Skill 单元测试。"""

import json
import os
import sys
import tempfile
from unittest.mock import patch

import pytest

# 确保项目根目录在 sys.path 中
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from skills.user_profile.script.main import main, _determine_job_type, _validate_inputs


# ========== 测试数据 ==========


def _campus_user_data() -> dict:
    """校招用户完整数据。"""
    return {
        "name": "张三",
        "education": "本科",
        "major": "计算机科学与技术",
        "graduation_year": 2026,
        "work_years": 0,
        "skills": ["Python", "机器学习", "PyTorch"],
        "target_cities": ["北京", "上海"],
        "target_positions": ["算法工程师", "机器学习工程师"],
    }


def _social_user_data() -> dict:
    """社招用户完整数据。"""
    return {
        "name": "李四",
        "education": "硕士",
        "major": "软件工程",
        "graduation_year": 2020,
        "work_years": 4,
        "skills": ["Java", "Spring Boot", "MySQL", "Redis"],
        "target_cities": ["深圳", "杭州"],
        "target_positions": ["后端开发工程师"],
        "email": "lisi@example.com",
        "phone": "13800138000",
    }


# ========== 求职类型判断测试 ==========


class TestDetermineJobType:
    """求职类型判断逻辑测试。"""

    def test_campus_fresh_graduate(self):
        """应届生判定为校招。"""
        assert _determine_job_type(2026, 0) == "campus"

    def test_campus_future_graduate(self):
        """未来毕业的学生判定为校招。"""
        assert _determine_job_type(2027, 0) == "campus"

    def test_social_with_work_experience(self):
        """有工作经验判定为社招。"""
        assert _determine_job_type(2020, 4) == "social"

    def test_social_graduated_no_experience(self):
        """已毕业但无工作经验也判定为社招（往届生）。"""
        assert _determine_job_type(2022, 0) == "social"

    def test_social_current_year_with_experience(self):
        """当前年份毕业但有工作经验判定为社招。"""
        assert _determine_job_type(2026, 1) == "social"


# ========== 输入校验测试 ==========


class TestValidateInputs:
    """输入校验测试。"""

    def test_valid_campus_data(self):
        """校招用户数据校验通过。"""
        assert _validate_inputs(_campus_user_data()) is None

    def test_valid_social_data(self):
        """社招用户数据校验通过。"""
        assert _validate_inputs(_social_user_data()) is None

    def test_missing_name(self):
        """缺少姓名字段。"""
        data = _campus_user_data()
        del data["name"]
        error = _validate_inputs(data)
        assert error is not None
        assert "name" in error

    def test_empty_name(self):
        """姓名为空。"""
        data = _campus_user_data()
        data["name"] = ""
        error = _validate_inputs(data)
        assert error is not None

    def test_invalid_education(self):
        """无效学历。"""
        data = _campus_user_data()
        data["education"] = "高中"
        error = _validate_inputs(data)
        assert error is not None
        assert "学历" in error

    def test_invalid_graduation_year_too_old(self):
        """毕业年份过早。"""
        data = _campus_user_data()
        data["graduation_year"] = 1980
        error = _validate_inputs(data)
        assert error is not None
        assert "毕业年份" in error

    def test_invalid_work_years_negative(self):
        """工作年限为负。"""
        data = _campus_user_data()
        data["work_years"] = -1
        error = _validate_inputs(data)
        assert error is not None
        assert "工作年限" in error

    def test_empty_skills_list(self):
        """技能列表为空。"""
        data = _campus_user_data()
        data["skills"] = []
        error = _validate_inputs(data)
        assert error is not None
        assert "技能" in error

    def test_invalid_email(self):
        """无效邮箱格式。"""
        data = _campus_user_data()
        data["email"] = "invalid-email"
        error = _validate_inputs(data)
        assert error is not None
        assert "邮箱" in error

    def test_invalid_phone(self):
        """无效手机号。"""
        data = _campus_user_data()
        data["phone"] = "12345"
        error = _validate_inputs(data)
        assert error is not None
        assert "手机号" in error

    def test_valid_optional_contact(self):
        """有效的可选联系方式。"""
        data = _campus_user_data()
        data["email"] = "test@example.com"
        data["phone"] = "13912345678"
        assert _validate_inputs(data) is None


# ========== 主函数集成测试 ==========


class TestMain:
    """main 函数集成测试。"""

    def setup_method(self):
        """每个测试前创建临时数据目录。"""
        self.temp_dir = tempfile.mkdtemp()
        self.temp_data_path = os.path.join(self.temp_dir, "user_data.json")

    def teardown_method(self):
        """每个测试后清理临时文件。"""
        if os.path.exists(self.temp_data_path):
            os.remove(self.temp_data_path)
        if os.path.exists(self.temp_dir):
            os.rmdir(self.temp_dir)

    @patch("skills.user_profile.script.main.DATA_DIR")
    @patch("skills.user_profile.script.main.USER_DATA_PATH")
    def test_campus_user_success(self, mock_path, mock_dir):
        """校招用户成功生成画像。"""
        mock_dir.__str__ = lambda x: self.temp_dir
        mock_path.__str__ = lambda x: self.temp_data_path

        # 使用真实路径 patch
        with patch("skills.user_profile.script.main.DATA_DIR", self.temp_dir), \
             patch("skills.user_profile.script.main.USER_DATA_PATH", self.temp_data_path):
            result = main(**_campus_user_data())

        assert result["success"] is True
        assert result["data"]["job_type"] == "campus"
        assert "校招" in result["message"]
        assert result["data"]["profile"]["basic_info"]["name"] == "张三"

    @patch("skills.user_profile.script.main.DATA_DIR")
    @patch("skills.user_profile.script.main.USER_DATA_PATH")
    def test_social_user_success(self, mock_path, mock_dir):
        """社招用户成功生成画像。"""
        with patch("skills.user_profile.script.main.DATA_DIR", self.temp_dir), \
             patch("skills.user_profile.script.main.USER_DATA_PATH", self.temp_data_path):
            result = main(**_social_user_data())

        assert result["success"] is True
        assert result["data"]["job_type"] == "social"
        assert "社招" in result["message"]
        assert result["data"]["profile"]["contact"]["email"] == "lisi@example.com"
        assert result["data"]["profile"]["contact"]["phone"] == "13800138000"

    def test_missing_required_field_returns_error(self):
        """缺少必填字段返回错误。"""
        result = main(name="王五")
        assert result["success"] is False
        assert result["data"] is None
        assert result["message"] is not None

    def test_invalid_data_returns_error(self):
        """无效数据返回错误。"""
        data = _campus_user_data()
        data["education"] = "小学"
        result = main(**data)
        assert result["success"] is False
        assert "学历" in result["message"]

    @patch("skills.user_profile.script.main.DATA_DIR")
    @patch("skills.user_profile.script.main.USER_DATA_PATH")
    def test_profile_persisted_to_file(self, mock_path, mock_dir):
        """画像数据成功持久化到文件。"""
        with patch("skills.user_profile.script.main.DATA_DIR", self.temp_dir), \
             patch("skills.user_profile.script.main.USER_DATA_PATH", self.temp_data_path):
            main(**_campus_user_data())

        assert os.path.exists(self.temp_data_path)
        with open(self.temp_data_path, "r", encoding="utf-8") as f:
            saved_data = json.load(f)
        assert saved_data["job_type"] == "campus"
        assert saved_data["basic_info"]["name"] == "张三"

    @patch("skills.user_profile.script.main.DATA_DIR")
    @patch("skills.user_profile.script.main.USER_DATA_PATH")
    def test_optional_fields_included(self, mock_path, mock_dir):
        """可选字段正确包含在画像中。"""
        data = _campus_user_data()
        data["salary_expectation"] = "15k-25k"
        data["projects"] = [{"name": "推荐系统", "description": "基于协同过滤"}]

        with patch("skills.user_profile.script.main.DATA_DIR", self.temp_dir), \
             patch("skills.user_profile.script.main.USER_DATA_PATH", self.temp_data_path):
            result = main(**data)

        assert result["success"] is True
        profile = result["data"]["profile"]
        assert profile["preferences"]["salary_expectation"] == "15k-25k"
        assert len(profile["experience"]["projects"]) == 1
