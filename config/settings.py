"""
全局配置模块。

定义各招聘平台 URL、默认参数、超时设置等。
"""

import os
from typing import Final


# ========== 项目基础配置 ==========

PROJECT_NAME: Final[str] = "中国牛马求职Agent"
VERSION: Final[str] = "0.1.0"

# 数据存储路径
BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR: str = os.path.join(BASE_DIR, "data")
USER_DATA_PATH: str = os.path.join(DATA_DIR, "user_data.json")
SHORTLIST_PATH: str = os.path.join(DATA_DIR, "shortlist.json")


# ========== 网络请求配置 ==========

REQUEST_TIMEOUT: int = 30  # 秒
REQUEST_RETRY_COUNT: int = 3
REQUEST_RETRY_DELAY: float = 1.0  # 秒
USER_AGENT: str = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)


# ========== 招聘平台配置 ==========

# 校招平台
CAMPUS_PLATFORMS: dict = {
    "nowcoder": {
        "name": "牛客网",
        "base_url": "https://www.nowcoder.com",
        "search_url": "https://www.nowcoder.com/search",
        "type": "campus",
    },
    "shixiseng": {
        "name": "实习僧",
        "base_url": "https://www.shixiseng.com",
        "search_url": "https://www.shixiseng.com/interns",
        "type": "campus",
    },
}

# 社招平台
SOCIAL_PLATFORMS: dict = {
    "boss": {
        "name": "Boss直聘",
        "base_url": "https://www.zhipin.com",
        "search_url": "https://www.zhipin.com/web/geek/job",
        "type": "social",
    },
    "lagou": {
        "name": "拉勾",
        "base_url": "https://www.lagou.com",
        "search_url": "https://www.lagou.com/jobs/list_",
        "type": "social",
    },
    "liepin": {
        "name": "猎聘",
        "base_url": "https://www.liepin.com",
        "search_url": "https://www.liepin.com/zhaopin/",
        "type": "social",
    },
    "maimai": {
        "name": "脉脉",
        "base_url": "https://maimai.cn",
        "search_url": "https://maimai.cn/job",
        "type": "social",
    },
}

# 全部平台汇总
ALL_PLATFORMS: dict = {**CAMPUS_PLATFORMS, **SOCIAL_PLATFORMS}


# ========== 求职类型配置 ==========

JOB_TYPES: dict = {
    "campus": {
        "label": "校招",
        "description": "应届生/实习生求职",
        "platforms": list(CAMPUS_PLATFORMS.keys()),
    },
    "social": {
        "label": "社招",
        "description": "社会招聘",
        "platforms": list(SOCIAL_PLATFORMS.keys()),
    },
}


# ========== 招聘季时间配置 ==========

CAMPUS_SEASONS: dict = {
    "autumn": {
        "label": "秋招",
        "months": [8, 9, 10],
    },
    "spring": {
        "label": "春招",
        "months": [2, 3, 4],
    },
}
