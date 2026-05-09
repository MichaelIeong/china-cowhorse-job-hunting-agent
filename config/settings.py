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

# 互联网大厂官网招聘
COMPANY_PLATFORMS: dict = {
    "tencent": {
        "name": "腾讯",
        "base_url": "https://careers.tencent.com",
        "campus_url": "https://join.qq.com",
        "type": "company_official",
    },
    "bytedance": {
        "name": "字节跳动",
        "base_url": "https://jobs.bytedance.com",
        "type": "company_official",
    },
    "alibaba": {
        "name": "阿里巴巴",
        "base_url": "https://talent.alibaba.com",
        "type": "company_official",
    },
    "meituan": {
        "name": "美团",
        "base_url": "https://zhaopin.meituan.com",
        "type": "company_official",
    },
    "jd": {
        "name": "京东",
        "base_url": "https://zhaopin.jd.com",
        "campus_url": "https://campus.jd.com",
        "type": "company_official",
    },
    "baidu": {
        "name": "百度",
        "base_url": "https://talent.baidu.com",
        "type": "company_official",
    },
    "huawei": {
        "name": "华为",
        "base_url": "https://career.huawei.com",
        "type": "company_official",
    },
    "xiaomi": {
        "name": "小米",
        "base_url": "https://hr.xiaomi.com",
        "type": "company_official",
    },
    "netease": {
        "name": "网易",
        "base_url": "https://hr.163.com",
        "type": "company_official",
    },
    "kuaishou": {
        "name": "快手",
        "base_url": "https://zhaopin.kuaishou.com",
        "type": "company_official",
    },
    "pdd": {
        "name": "拼多多",
        "base_url": "https://careers.pinduoduo.com",
        "type": "company_official",
    },
    "didi": {
        "name": "滴滴",
        "base_url": "https://talent.didiglobal.com",
        "type": "company_official",
    },
    "ant": {
        "name": "蚂蚁集团",
        "base_url": "https://talent.antgroup.com",
        "type": "company_official",
    },
    "microsoft": {
        "name": "微软中国",
        "base_url": "https://careers.microsoft.com",
        "type": "company_official",
    },
    "byd": {
        "name": "比亚迪",
        "base_url": "https://job.byd.com",
        "type": "company_official",
    },
}

# 全部平台汇总
ALL_PLATFORMS: dict = {**CAMPUS_PLATFORMS, **SOCIAL_PLATFORMS, **COMPANY_PLATFORMS}


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
