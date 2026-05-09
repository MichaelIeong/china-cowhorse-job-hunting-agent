# 开发流程文档

> 中国牛马求职 Agent 项目开发指南

## 目录

1. [项目概述](#项目概述)
2. [环境搭建](#环境搭建)
3. [项目结构说明](#项目结构说明)
4. [开发流程](#开发流程)
5. [Skill 开发规范](#skill-开发规范)
6. [各 Skill 开发顺序与依赖关系](#各-skill-开发顺序与依赖关系)
7. [测试规范](#测试规范)
8. [Git 工作流](#git-工作流)
9. [注意事项与约束](#注意事项与约束)

---

## 项目概述

本项目是一个基于大模型 Skill 机制的中国求职辅助 Agent，以纯 Python 脚本实现。核心工作流如下：

```
用户对话 → 大模型判断意图 → 调用对应 Skill → 返回结构化结果 → 大模型整合回复用户
```

**设计原则：**
- 无前端、无数据库、无部署
- Skill 驱动，每个功能为独立脚本
- 数据本地 JSON 存储
- 支持校招和社招两大场景

---

## 环境搭建

### 前置条件

- Python 3.10+
- Git
- pip

### 初始化步骤

```bash
# 1. 克隆仓库
git clone git@github.com:MichaelIeong/china-cowhorse-job-hunting-agent.git
cd china-cowhorse-job-hunting-agent

# 2. 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. 安装 Playwright 浏览器（投递功能需要）
playwright install chromium

# 5. 配置环境变量（如有需要）
cp .env.example .env
# 编辑 .env 填入 API Key 等敏感信息
```

### 验证环境

```bash
# 运行测试确认环境正常
pytest tests/ -v

# 检查代码风格
flake8 skills/ utils/ config/
black --check skills/ utils/ config/
```

---

## 项目结构说明

```
cowhorse/
├── README.md                   # 项目说明
├── requirements.txt            # Python 依赖
├── .gitignore                  # Git 忽略规则
├── .claude/
│   └── CLAUDE.md               # Claude Code 开发指引
├── config/
│   ├── __init__.py
│   └── settings.py             # 全局配置（平台URL、参数、常量）
├── skills/                     # 每个 Skill 一个文件夹
│   ├── user_profile/
│   │   ├── skill.md            # Skill 元信息和使用方法
│   │   └── script/
│   │       └── main.py         # Skill 主逻辑入口
│   ├── job_search/
│   │   ├── skill.md
│   │   └── script/main.py
│   ├── job_shortlist/
│   │   ├── skill.md
│   │   └── script/main.py
│   ├── resume_optimizer/
│   │   ├── skill.md
│   │   └── script/main.py
│   └── interview_prep/
│       ├── skill.md
│       └── script/main.py
├── utils/
│   ├── __init__.py
│   ├── exceptions.py           # 自定义异常类
│   ├── validator.py            # 输入校验工具
│   ├── parser.py               # 数据解析工具（HTML/JSON/薪资）
│   └── platform_adapter.py     # 招聘平台+大厂官网适配器
├── data/
│   ├── .gitkeep                # 保持目录存在
│   ├── user_data.json          # 用户画像数据（运行时生成，不入库）
│   └── shortlist.json          # 心仪岗位列表（运行时生成，不入库）
├── tests/
│   └── ...
└── docs/
    └── development_workflow.md  # 本文档
```

### 模块职责

| 模块 | 职责 |
|------|------|
| `config/settings.py` | 全局配置，包括平台 URL、超时参数、求职类型定义 |
| `utils/exceptions.py` | 自定义异常类（ValidationError、NetworkError 等） |
| `utils/validator.py` | 输入校验函数（必填字段、类型、格式） |
| `utils/parser.py` | JSON 文件读写、HTML 文本提取、薪资解析 |
| `utils/platform_adapter.py` | 各招聘平台适配器基类和具体实现 |

---

## 开发流程

### 总体流程

```
需求理解 → 编写测试 → 实现功能 → 本地验证 → 提交推送
```

### 单个 Skill 开发步骤

1. **理解需求** - 明确该 Skill 的输入、输出、边界条件
2. **创建目录** - 在 `skills/<skill_name>/` 下创建 `skill.md` 和 `script/` 目录
3. **编写 skill.md** - 定义元信息、入参、出参、使用方法
4. **编写测试** - 在 `tests/` 下创建对应测试文件，先写测试用例
5. **实现功能** - 在 `skills/<skill_name>/script/main.py` 中实现主体逻辑
6. **补充工具** - 如需新工具函数，在 `utils/` 中添加
7. **运行测试** - `pytest tests/test_xxx.py -v` 确保全部通过
8. **代码检查** - `flake8` + `black` 确保代码风格统一
9. **提交推送** - `git add` + `git commit` + `git push`

---

## Skill 开发规范

### 入口函数模板

每个 Skill 必须遵循以下模板：

```python
"""
Skill: <skill名称>
功能: <一句话描述>
输入: <参数说明>
输出: <返回值说明>
"""

from typing import Any
from utils.validator import validate_required_fields
from utils.exceptions import ValidationError


def main(**kwargs: Any) -> dict:
    """Skill 入口函数，由大模型调用。

    Args:
        **kwargs: 参数说明...

    Returns:
        dict: 标准返回格式
    """
    # 1. 输入校验
    error = validate_required_fields(kwargs, ["field1", "field2"])
    if error:
        return {"success": False, "data": None, "message": error}

    # 2. 业务逻辑
    try:
        result = _do_business_logic(kwargs)
    except Exception as e:
        return {"success": False, "data": None, "message": f"处理失败: {e}"}

    # 3. 返回结果
    return {
        "success": True,
        "data": result,
        "message": "处理成功",
    }
```

### 返回值格式（强制统一）

```python
{
    "success": bool,       # 是否成功
    "data": Any,           # 具体数据（成功时为结果，失败时为 None）
    "message": str,        # 用户可读的中文说明
}
```

### 异常处理规则

- 所有外部调用（网络请求、文件读写）必须 try-except
- 不要让异常抛到 Skill 外部，统一在 main() 内捕获
- 错误信息使用中文，对用户友好

---

## 各 Skill 开发顺序与依赖关系

按以下顺序开发，后续 Skill 依赖前序 Skill 的输出：

```
┌─────────────────┐
│  1. user_profile │  ← 第一步，所有后续 Skill 依赖用户画像
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  2. job_search   │  ← 依赖用户画像中的求职类型和偏好
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  3. job_shortlist│  ← 依赖 job_search 的搜索结果
└────────┬────────┘
         │
         ├──────────────────┐
         ▼                  ▼
┌─────────────────┐  ┌─────────────────┐
│4. resume_optimizer│  │5. interview_prep │  ← 两者可并行，依赖心仪岗位
└─────────────────┘  └─────────────────┘
```

### 各 Skill 核心逻辑说明

#### Skill 1: user_profile（用户画像采集）

**核心任务：**
- 采集用户基本信息（姓名、学历、专业、毕业年份、工作年限）
- 采集求职偏好（目标城市、目标岗位、薪资期望）
- 采集技能列表和项目经验
- **关键判断**：根据毕业年份和工作年限自动判断 校招/社招

**判断逻辑：**
```python
# 校招条件：毕业年份 >= 当前年份，或工作年限 == 0
if graduation_year >= current_year or work_years == 0:
    job_type = "campus"
else:
    job_type = "social"
```

**输出数据持久化到 `data/user_data.json`**

#### Skill 2: job_search（职位搜索聚合）

**核心任务：**
- 读取用户画像，确定搜索平台（校招→牛客/实习僧，社招→Boss/拉勾/猎聘）
- 使用 `platform_adapter` 调用对应平台搜索接口
- 聚合多平台结果，去重
- 返回结构化岗位列表

**依赖：**
- `data/user_data.json`（用户画像）
- `utils/platform_adapter.py`（平台适配器）

#### Skill 3: job_shortlist（心仪岗位整理）

**核心任务：**
- 接收搜索结果，根据用户偏好排序筛选
- 进行薪资区间分析（使用 `parser.parse_salary_range`）
- 计算岗位匹配度
- 输出整理后的心仪岗位清单

**输出数据持久化到 `data/shortlist.json`**

#### Skill 4: resume_optimizer（简历优化）

**核心任务：**
- 接收用户简历文本和目标岗位 JD
- 分析关键词匹配度
- 对比简历内容与岗位要求的差距
- 输出匹配度评分和具体优化建议

#### Skill 5: interview_prep（面试准备）

**核心任务：**
- 根据岗位 JD 生成面试常见问题
- 在牛客网和小红书搜索该岗位/公司的面经
- 整合公司背景信息
- 输出面试准备材料文档

---

## 测试规范

### 测试文件命名

- 文件名：`test_<模块名>.py`
- 类名：`Test<功能描述>`
- 方法名：`test_<具体场景>`

### 测试用例结构

```python
"""test_user_profile.py - 用户画像 Skill 测试。"""

import pytest
from skills.user_profile import main


class TestUserProfile:
    """用户画像采集测试。"""

    def test_campus_user_detection(self):
        """测试校招用户识别。"""
        result = main(
            name="张三",
            education="本科",
            graduation_year=2026,
            work_years=0,
            skills=["Python", "机器学习"],
            target_cities=["北京", "上海"],
            target_positions=["算法工程师"],
        )
        assert result["success"] is True
        assert result["data"]["job_type"] == "campus"

    def test_social_user_detection(self):
        """测试社招用户识别。"""
        result = main(
            name="李四",
            education="硕士",
            graduation_year=2020,
            work_years=4,
            skills=["Java", "Spring"],
            target_cities=["深圳"],
            target_positions=["后端开发"],
        )
        assert result["success"] is True
        assert result["data"]["job_type"] == "social"

    def test_missing_required_field(self):
        """测试缺少必填字段。"""
        result = main(name="王五")
        assert result["success"] is False
        assert "缺少" in result["message"] or "必填" in result["message"]
```

### 运行测试

```bash
# 运行所有测试
pytest tests/ -v

# 运行单个测试文件
pytest tests/test_user_profile.py -v

# 查看覆盖率
pytest tests/ --cov=skills --cov=utils --cov-report=html
```

---

## Git 工作流

### Commit 规范

格式：`<type>: <description>`

| Type | 说明 | 示例 |
|------|------|------|
| `feat` | 新功能 | `feat: 添加用户画像采集skill` |
| `fix` | 修复bug | `fix: 修复薪资解析空值异常` |
| `refactor` | 重构 | `refactor: 重构平台适配器基类` |
| `test` | 测试 | `test: 添加job_search单元测试` |
| `docs` | 文档 | `docs: 更新开发流程文档` |
| `chore` | 杂项 | `chore: 更新依赖版本` |

### 提交节奏

- **每完成一个 Skill** → 必须 commit + push
- **每完成一个工具函数** → 建议 commit + push
- **每修复一个 bug** → 必须 commit + push

### 标准操作

```bash
# 查看状态
git status

# 添加文件（具体文件名，不用 git add .）
git add skills/user_profile.py tests/test_user_profile.py

# 提交
git commit -m "feat: 添加用户画像采集skill"

# 推送
git push origin main
```

---

## 注意事项与约束

### 安全约束

- **敏感信息**（API Key 等）通过环境变量传入，绝不硬编码
- **用户数据** 仅存本地 JSON，不上传任何服务器
- `.env` 文件已在 `.gitignore` 中，不会被提交

### 爬虫约束

- 遵守各平台 robots.txt
- 请求频率限制：同一平台间隔不少于 2 秒
- 设置合理的 User-Agent
- 网络请求必须设置 timeout（默认 30 秒）
- 请求失败自动重试（最多 3 次，间隔递增）

### 代码质量

- 所有函数必须有 type hints
- 所有函数和类必须有 docstring
- 变量命名使用 snake_case
- 遵循 PEP 8 规范
- 单个函数不超过 50 行

### 错误处理

- 所有外部调用必须 try-except
- 错误信息使用中文描述
- 自定义异常统一在 `utils/exceptions.py`
- Skill 入口函数不抛异常，统一返回错误格式

---

## 快速参考

### 开发新 Skill 检查清单

- [ ] 在 `skills/<name>/` 下创建文件夹
- [ ] 编写 `skill.md`（元信息、入参、出参、使用方法）
- [ ] 在 `script/main.py` 中实现入口函数 `main(**kwargs) -> dict`
- [ ] 在 `tests/` 下创建对应测试文件
- [ ] 有输入校验（使用 `utils/validator.py`）
- [ ] 有异常处理（不抛异常到外部）
- [ ] 返回值格式统一 `{"success", "data", "message"}`
- [ ] 有 docstring 和 type hints
- [ ] 测试通过
- [ ] commit + push

### 常用命令速查

```bash
pytest tests/ -v                    # 运行测试
flake8 skills/ utils/ config/       # 代码检查
black skills/ utils/ config/        # 自动格式化
mypy skills/ utils/                 # 类型检查
git status                          # 查看变更
git log --oneline -10               # 查看提交历史
```
