"""
Skill: interview_prep
功能: 根据岗位JD和公司信息生成面试准备材料
输入: 目标岗位JD、公司信息、用户简历
输出: 面试准备材料（常见问题、回答建议、公司背景等）
"""

from typing import Any


def main(**kwargs: Any) -> dict:
    """Skill 入口函数，由大模型调用。

    根据目标岗位JD和用户简历，生成定制化的面试准备材料。

    Args:
        **kwargs: 准备参数，包含:
            - job_description (str): 岗位JD
            - company_name (str): 公司名称
            - resume_text (str): 用户简历内容
            - interview_type (str): 面试类型（tech/hr/behavior）

    Returns:
        dict: 标准返回格式 {"success": bool, "data": dict, "message": str}
            data 包含:
                - common_questions (list[dict]): 常见面试问题及建议回答
                - company_info (dict): 公司背景信息
                - key_points (list[str]): 面试要点提醒
    """
    # TODO: 实现面试准备材料生成逻辑
    return {
        "success": False,
        "data": None,
        "message": "interview_prep skill 尚未实现",
    }
