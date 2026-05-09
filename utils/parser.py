"""
数据解析工具模块。

提供 HTML/JSON 解析工具函数。
"""

import json
from typing import Any, Optional

from utils.exceptions import ParserError


def parse_json_file(file_path: str) -> dict:
    """读取并解析 JSON 文件。

    Args:
        file_path: JSON 文件路径。

    Returns:
        解析后的字典数据。

    Raises:
        ParserError: 文件读取或解析失败。
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise ParserError(f"文件不存在: {file_path}")
    except json.JSONDecodeError as e:
        raise ParserError(f"JSON 解析失败: {e}")
    except Exception as e:
        raise ParserError(f"文件读取失败: {e}")


def save_json_file(file_path: str, data: Any) -> None:
    """将数据保存为 JSON 文件。

    Args:
        file_path: 目标文件路径。
        data: 待保存的数据。

    Raises:
        ParserError: 文件写入失败。
    """
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise ParserError(f"文件写入失败: {e}")


def extract_text_from_html(html_content: str, selector: Optional[str] = None) -> str:
    """从 HTML 内容中提取纯文本。

    Args:
        html_content: HTML 字符串内容。
        selector: 可选的 CSS 选择器，用于定位特定元素。

    Returns:
        提取的纯文本内容。

    Raises:
        ParserError: 解析失败。
    """
    try:
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html_content, "html.parser")

        if selector:
            element = soup.select_one(selector)
            if element is None:
                return ""
            return element.get_text(strip=True)

        return soup.get_text(strip=True)
    except ImportError:
        raise ParserError("缺少 beautifulsoup4 依赖，请先安装: pip install beautifulsoup4")
    except Exception as e:
        raise ParserError(f"HTML 解析失败: {e}")


def parse_salary_range(salary_text: str) -> Optional[dict]:
    """解析薪资文本为结构化数据。

    支持格式如: "15k-25k", "15K-25K·14薪", "面议"

    Args:
        salary_text: 薪资文本。

    Returns:
        结构化薪资数据字典，格式: {"min": int, "max": int, "unit": str, "months": int}
        无法解析时返回 None。
    """
    import re

    if not salary_text or salary_text.strip() == "面议":
        return None

    salary_text = salary_text.strip().upper()

    # 匹配 "15K-25K" 或 "15K-25K·14薪" 格式
    pattern = r"(\d+)[K]?\s*[-~]\s*(\d+)[K]?"
    match = re.search(pattern, salary_text)

    if not match:
        return None

    min_salary = int(match.group(1))
    max_salary = int(match.group(2))

    # 判断单位（如果数字较小，说明单位是K）
    if min_salary < 1000:
        min_salary *= 1000
        max_salary *= 1000

    # 匹配月数（如 "14薪" "13薪"）
    months_match = re.search(r"(\d+)\s*薪", salary_text)
    months = int(months_match.group(1)) if months_match else 12

    return {
        "min": min_salary,
        "max": max_salary,
        "unit": "元/月",
        "months": months,
    }
