"""
Skill: user_profile
功能: 采集用户信息，判断校招/社招类型，生成求职画像
输入: 用户基本信息（姓名、学历、工作年限、技能等）
输出: 用户画像字典，包含求职类型判断结果
"""

import os
import sys
from datetime import datetime
from typing import Any

# 确保项目根目录在 sys.path 中
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from config.settings import DATA_DIR, USER_DATA_PATH
from utils.validator import (
    validate_required_fields,
    validate_string,
    validate_list,
    validate_email,
    validate_phone,
)
from utils.parser import save_json_file, parse_json_file
from utils.exceptions import DataStorageError


# ========== 常量 ==========

VALID_EDUCATIONS = ["大专", "本科", "硕士", "博士"]

REQUIRED_FIELDS = [
    "name",
    "education",
    "major",
    "graduation_year",
    "work_years",
    "skills",
    "target_cities",
    "target_positions",
]


# ========== 核心逻辑 ==========


def _determine_job_type(graduation_year: int, work_years: int) -> str:
    """判断求职类型：校招或社招。

    判断逻辑：
    - 毕业年份 >= 当前年份 且 工作年限 == 0 → 校招
    - 其他情况 → 社招

    Args:
        graduation_year: 毕业年份。
        work_years: 工作年限。

    Returns:
        'campus' 或 'social'。
    """
    current_year = datetime.now().year

    if graduation_year >= current_year and work_years == 0:
        return "campus"
    return "social"


def _build_profile(data: dict) -> dict:
    """构建用户画像数据结构。

    Args:
        data: 经过校验的用户输入数据。

    Returns:
        完整的用户画像字典。
    """
    job_type = _determine_job_type(data["graduation_year"], data["work_years"])

    profile = {
        "basic_info": {
            "name": data["name"],
            "education": data["education"],
            "major": data["major"],
            "graduation_year": data["graduation_year"],
            "work_years": data["work_years"],
        },
        "contact": {},
        "job_type": job_type,
        "skills": data["skills"],
        "preferences": {
            "target_cities": data["target_cities"],
            "target_positions": data["target_positions"],
            "salary_expectation": data.get("salary_expectation"),
        },
        "experience": {
            "projects": data.get("projects", []),
            "internships": data.get("internships", []),
            "work_experience": data.get("work_experience", []),
        },
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }

    # 可选联系方式
    if data.get("phone"):
        profile["contact"]["phone"] = data["phone"]
    if data.get("email"):
        profile["contact"]["email"] = data["email"]

    return profile


def _save_profile(profile: dict) -> None:
    """将用户画像持久化到本地 JSON 文件。

    Args:
        profile: 用户画像数据。

    Raises:
        DataStorageError: 存储失败。
    """
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        save_json_file(USER_DATA_PATH, profile)
    except Exception as e:
        raise DataStorageError(f"用户画像保存失败: {e}")


def _validate_inputs(data: dict) -> str | None:
    """执行所有输入校验。

    Args:
        data: 用户输入数据。

    Returns:
        校验失败时返回错误信息，成功时返回 None。
    """
    # 必填字段检查
    error = validate_required_fields(data, REQUIRED_FIELDS)
    if error:
        return error

    # 姓名校验
    error = validate_string(data["name"], "姓名", min_length=1, max_length=20)
    if error:
        return error

    # 学历校验
    if data["education"] not in VALID_EDUCATIONS:
        return f"学历无效，应为 {VALID_EDUCATIONS} 之一"

    # 专业校验
    error = validate_string(data["major"], "专业", min_length=1, max_length=50)
    if error:
        return error

    # 毕业年份校验
    if not isinstance(data["graduation_year"], int):
        return "毕业年份必须为整数"
    if data["graduation_year"] < 1990 or data["graduation_year"] > 2035:
        return "毕业年份范围应在 1990-2035 之间"

    # 工作年限校验
    if not isinstance(data["work_years"], int):
        return "工作年限必须为整数"
    if data["work_years"] < 0 or data["work_years"] > 40:
        return "工作年限范围应在 0-40 之间"

    # 技能列表校验
    error = validate_list(data["skills"], "技能列表", min_items=1, max_items=30)
    if error:
        return error

    # 目标城市校验
    error = validate_list(data["target_cities"], "目标城市", min_items=1, max_items=10)
    if error:
        return error

    # 目标岗位校验
    error = validate_list(data["target_positions"], "目标岗位", min_items=1, max_items=10)
    if error:
        return error

    # 可选字段校验
    if data.get("email"):
        error = validate_email(data["email"])
        if error:
            return error

    if data.get("phone"):
        error = validate_phone(data["phone"])
        if error:
            return error

    return None


# ========== 入口函数 ==========


def main(**kwargs: Any) -> dict:
    """Skill 入口函数，由大模型调用。

    采集用户基本信息，根据学历和工作经验判断用户属于校招还是社招场景，
    生成完整的用户求职画像并持久化存储。

    Args:
        **kwargs: 用户信息参数，包含:
            - name (str): 姓名
            - education (str): 学历（大专/本科/硕士/博士）
            - major (str): 专业
            - graduation_year (int): 毕业年份
            - work_years (int): 工作年限（应届填0）
            - skills (list[str]): 技能列表
            - target_cities (list[str]): 目标城市
            - target_positions (list[str]): 目标岗位
            - phone (str, 可选): 手机号
            - email (str, 可选): 邮箱
            - salary_expectation (str, 可选): 薪资期望
            - projects (list[dict], 可选): 项目经历
            - internships (list[dict], 可选): 实习经历
            - work_experience (list[dict], 可选): 工作经历

    Returns:
        dict: 标准返回格式 {"success": bool, "data": dict, "message": str}
    """
    # 1. 输入校验
    error = _validate_inputs(kwargs)
    if error:
        return {"success": False, "data": None, "message": error}

    # 2. 构建用户画像
    try:
        profile = _build_profile(kwargs)
    except Exception as e:
        return {"success": False, "data": None, "message": f"画像构建失败: {e}"}

    # 3. 持久化存储
    try:
        _save_profile(profile)
    except DataStorageError as e:
        return {"success": False, "data": None, "message": str(e.message)}
    except Exception as e:
        return {"success": False, "data": None, "message": f"数据存储失败: {e}"}

    # 4. 返回结果
    job_type_label = "校招" if profile["job_type"] == "campus" else "社招"
    return {
        "success": True,
        "data": {
            "job_type": profile["job_type"],
            "profile": profile,
        },
        "message": f"用户画像生成成功，判定为{job_type_label}场景",
    }
