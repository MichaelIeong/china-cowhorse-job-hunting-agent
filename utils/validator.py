"""
输入校验工具模块。

提供统一的参数校验函数，用于各 Skill 入口处的参数检查。
"""

from typing import Any, Optional


def validate_required_fields(data: dict, required_fields: list[str]) -> Optional[str]:
    """校验必填字段是否存在且非空。

    Args:
        data: 待校验的字典数据。
        required_fields: 必填字段列表。

    Returns:
        校验失败时返回错误信息字符串，成功时返回 None。
    """
    if not isinstance(data, dict):
        return "输入数据格式错误，期望为字典类型"

    for field in required_fields:
        if field not in data:
            return f"缺少必填字段: {field}"
        if data[field] is None or (isinstance(data[field], str) and data[field].strip() == ""):
            return f"字段不能为空: {field}"

    return None


def validate_string(value: Any, field_name: str, min_length: int = 1, max_length: int = 500) -> Optional[str]:
    """校验字符串类型参数。

    Args:
        value: 待校验的值。
        field_name: 字段名，用于错误信息。
        min_length: 最小长度。
        max_length: 最大长度。

    Returns:
        校验失败时返回错误信息字符串，成功时返回 None。
    """
    if not isinstance(value, str):
        return f"{field_name} 必须为字符串类型"
    if len(value.strip()) < min_length:
        return f"{field_name} 长度不能少于 {min_length} 个字符"
    if len(value) > max_length:
        return f"{field_name} 长度不能超过 {max_length} 个字符"

    return None


def validate_list(value: Any, field_name: str, min_items: int = 0, max_items: int = 100) -> Optional[str]:
    """校验列表类型参数。

    Args:
        value: 待校验的值。
        field_name: 字段名，用于错误信息。
        min_items: 最少元素数。
        max_items: 最多元素数。

    Returns:
        校验失败时返回错误信息字符串，成功时返回 None。
    """
    if not isinstance(value, list):
        return f"{field_name} 必须为列表类型"
    if len(value) < min_items:
        return f"{field_name} 至少需要 {min_items} 个元素"
    if len(value) > max_items:
        return f"{field_name} 最多允许 {max_items} 个元素"

    return None


def validate_job_type(job_type: str) -> Optional[str]:
    """校验求职类型。

    Args:
        job_type: 求职类型，应为 'campus' 或 'social'。

    Returns:
        校验失败时返回错误信息字符串，成功时返回 None。
    """
    valid_types = ["campus", "social"]
    if job_type not in valid_types:
        return f"求职类型无效，应为 {valid_types} 之一，实际为: {job_type}"

    return None


def validate_email(email: str) -> Optional[str]:
    """校验邮箱格式（简单校验）。

    Args:
        email: 邮箱地址。

    Returns:
        校验失败时返回错误信息字符串，成功时返回 None。
    """
    if not isinstance(email, str):
        return "邮箱必须为字符串类型"
    if "@" not in email or "." not in email.split("@")[-1]:
        return "邮箱格式无效"

    return None


def validate_phone(phone: str) -> Optional[str]:
    """校验中国大陆手机号格式。

    Args:
        phone: 手机号。

    Returns:
        校验失败时返回错误信息字符串，成功时返回 None。
    """
    if not isinstance(phone, str):
        return "手机号必须为字符串类型"
    phone_clean = phone.replace("-", "").replace(" ", "")
    if not phone_clean.isdigit():
        return "手机号只能包含数字"
    if len(phone_clean) != 11 or not phone_clean.startswith("1"):
        return "手机号格式无效，应为11位且以1开头"

    return None
