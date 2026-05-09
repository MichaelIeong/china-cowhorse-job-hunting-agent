"""
招聘平台适配器模块。

使用适配器模式，每个招聘平台一个适配器类，提供统一的接口。
包含第三方招聘平台和各大互联网公司官网适配器。
"""

from abc import ABC, abstractmethod
from typing import Optional

from utils.exceptions import PlatformAdapterError


# ========== 基类 ==========


class BasePlatformAdapter(ABC):
    """招聘平台适配器基类。

    所有平台适配器必须继承此类并实现抽象方法。
    """

    def __init__(self, platform_name: str, base_url: str, platform_type: str = "third_party"):
        """初始化适配器。

        Args:
            platform_name: 平台名称。
            base_url: 平台基础 URL。
            platform_type: 平台类型（third_party/company_official）。
        """
        self.platform_name = platform_name
        self.base_url = base_url
        self.platform_type = platform_type

    @abstractmethod
    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索岗位。

        Args:
            keyword: 搜索关键词。
            city: 城市筛选。
            **kwargs: 其他平台特定参数。

        Returns:
            岗位列表，每个岗位为字典格式。
        """
        pass

    @abstractmethod
    def get_job_detail(self, job_id: str) -> dict:
        """获取岗位详情。

        Args:
            job_id: 岗位唯一标识。

        Returns:
            岗位详情字典。
        """
        pass

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(platform={self.platform_name})>"


# ========== 第三方招聘平台适配器 ==========


class BossAdapter(BasePlatformAdapter):
    """Boss直聘适配器。"""

    def __init__(self):
        super().__init__("Boss直聘", "https://www.zhipin.com", "third_party")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索Boss直聘岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("Boss直聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取Boss直聘岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("Boss直聘详情获取功能尚未实现")


class NowcoderAdapter(BasePlatformAdapter):
    """牛客网适配器。"""

    def __init__(self):
        super().__init__("牛客网", "https://www.nowcoder.com", "third_party")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索牛客网岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("牛客网搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取牛客网岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("牛客网详情获取功能尚未实现")


class LagouAdapter(BasePlatformAdapter):
    """拉勾适配器。"""

    def __init__(self):
        super().__init__("拉勾", "https://www.lagou.com", "third_party")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索拉勾岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("拉勾搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取拉勾岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("拉勾详情获取功能尚未实现")


class LiepinAdapter(BasePlatformAdapter):
    """猎聘适配器。"""

    def __init__(self):
        super().__init__("猎聘", "https://www.liepin.com", "third_party")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索猎聘岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("猎聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取猎聘岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("猎聘详情获取功能尚未实现")


class ShixisengAdapter(BasePlatformAdapter):
    """实习僧适配器。"""

    def __init__(self):
        super().__init__("实习僧", "https://www.shixiseng.com", "third_party")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索实习僧岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("实习僧搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取实习僧岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("实习僧详情获取功能尚未实现")


class MaimaiAdapter(BasePlatformAdapter):
    """脉脉适配器。"""

    def __init__(self):
        super().__init__("脉脉", "https://maimai.cn", "third_party")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索脉脉岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("脉脉搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取脉脉岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("脉脉详情获取功能尚未实现")


# ========== 互联网大厂官网适配器 ==========


class TencentAdapter(BasePlatformAdapter):
    """腾讯招聘适配器。"""

    def __init__(self):
        super().__init__("腾讯", "https://careers.tencent.com", "company_official")
        self.campus_url = "https://join.qq.com"

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索腾讯岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("腾讯招聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取腾讯岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("腾讯招聘详情获取功能尚未实现")


class BytedanceAdapter(BasePlatformAdapter):
    """字节跳动招聘适配器。"""

    def __init__(self):
        super().__init__("字节跳动", "https://jobs.bytedance.com", "company_official")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索字节跳动岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("字节跳动招聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取字节跳动岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("字节跳动招聘详情获取功能尚未实现")


class AlibabaAdapter(BasePlatformAdapter):
    """阿里巴巴招聘适配器。"""

    def __init__(self):
        super().__init__("阿里巴巴", "https://talent.alibaba.com", "company_official")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索阿里巴巴岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("阿里巴巴招聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取阿里巴巴岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("阿里巴巴招聘详情获取功能尚未实现")


class MeituanAdapter(BasePlatformAdapter):
    """美团招聘适配器。"""

    def __init__(self):
        super().__init__("美团", "https://zhaopin.meituan.com", "company_official")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索美团岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("美团招聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取美团岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("美团招聘详情获取功能尚未实现")


class JDAdapter(BasePlatformAdapter):
    """京东招聘适配器。"""

    def __init__(self):
        super().__init__("京东", "https://zhaopin.jd.com", "company_official")
        self.campus_url = "https://campus.jd.com"

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索京东岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("京东招聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取京东岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("京东招聘详情获取功能尚未实现")


class BaiduAdapter(BasePlatformAdapter):
    """百度招聘适配器。"""

    def __init__(self):
        super().__init__("百度", "https://talent.baidu.com", "company_official")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索百度岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("百度招聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取百度岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("百度招聘详情获取功能尚未实现")


class HuaweiAdapter(BasePlatformAdapter):
    """华为招聘适配器。"""

    def __init__(self):
        super().__init__("华为", "https://career.huawei.com", "company_official")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索华为岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("华为招聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取华为岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("华为招聘详情获取功能尚未实现")


class XiaomiAdapter(BasePlatformAdapter):
    """小米招聘适配器。"""

    def __init__(self):
        super().__init__("小米", "https://hr.xiaomi.com", "company_official")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索小米岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("小米招聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取小米岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("小米招聘详情获取功能尚未实现")


class NeteaseAdapter(BasePlatformAdapter):
    """网易招聘适配器。"""

    def __init__(self):
        super().__init__("网易", "https://hr.163.com", "company_official")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索网易岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("网易招聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取网易岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("网易招聘详情获取功能尚未实现")


class KuaishouAdapter(BasePlatformAdapter):
    """快手招聘适配器。"""

    def __init__(self):
        super().__init__("快手", "https://zhaopin.kuaishou.com", "company_official")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索快手岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("快手招聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取快手岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("快手招聘详情获取功能尚未实现")


class PDDAdapter(BasePlatformAdapter):
    """拼多多招聘适配器。"""

    def __init__(self):
        super().__init__("拼多多", "https://careers.pinduoduo.com", "company_official")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索拼多多岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("拼多多招聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取拼多多岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("拼多多招聘详情获取功能尚未实现")


class DidiAdapter(BasePlatformAdapter):
    """滴滴招聘适配器。"""

    def __init__(self):
        super().__init__("滴滴", "https://talent.didiglobal.com", "company_official")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索滴滴岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("滴滴招聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取滴滴岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("滴滴招聘详情获取功能尚未实现")


class AntGroupAdapter(BasePlatformAdapter):
    """蚂蚁集团招聘适配器。"""

    def __init__(self):
        super().__init__("蚂蚁集团", "https://talent.antgroup.com", "company_official")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索蚂蚁集团岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("蚂蚁集团招聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取蚂蚁集团岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("蚂蚁集团招聘详情获取功能尚未实现")


class MicrosoftChinaAdapter(BasePlatformAdapter):
    """微软中国招聘适配器。"""

    def __init__(self):
        super().__init__("微软中国", "https://careers.microsoft.com", "company_official")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索微软中国岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("微软中国招聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取微软中国岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("微软中国招聘详情获取功能尚未实现")


class BYDAdapter(BasePlatformAdapter):
    """比亚迪招聘适配器。"""

    def __init__(self):
        super().__init__("比亚迪", "https://job.byd.com", "company_official")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索比亚迪岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("比亚迪招聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取比亚迪岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("比亚迪招聘详情获取功能尚未实现")


# ========== 适配器注册表与工厂函数 ==========


# 第三方招聘平台
THIRD_PARTY_ADAPTERS: dict[str, type[BasePlatformAdapter]] = {
    "boss": BossAdapter,
    "nowcoder": NowcoderAdapter,
    "lagou": LagouAdapter,
    "liepin": LiepinAdapter,
    "shixiseng": ShixisengAdapter,
    "maimai": MaimaiAdapter,
}

# 互联网大厂官网
COMPANY_ADAPTERS: dict[str, type[BasePlatformAdapter]] = {
    "tencent": TencentAdapter,
    "bytedance": BytedanceAdapter,
    "alibaba": AlibabaAdapter,
    "meituan": MeituanAdapter,
    "jd": JDAdapter,
    "baidu": BaiduAdapter,
    "huawei": HuaweiAdapter,
    "xiaomi": XiaomiAdapter,
    "netease": NeteaseAdapter,
    "kuaishou": KuaishouAdapter,
    "pdd": PDDAdapter,
    "didi": DidiAdapter,
    "ant": AntGroupAdapter,
    "microsoft": MicrosoftChinaAdapter,
    "byd": BYDAdapter,
}

# 全部适配器
ALL_ADAPTERS: dict[str, type[BasePlatformAdapter]] = {
    **THIRD_PARTY_ADAPTERS,
    **COMPANY_ADAPTERS,
}


def get_adapter(platform_key: str) -> BasePlatformAdapter:
    """根据平台标识获取对应适配器实例。

    Args:
        platform_key: 平台标识（如 'boss', 'tencent', 'bytedance'）。

    Returns:
        对应平台的适配器实例。

    Raises:
        PlatformAdapterError: 不支持的平台。
    """
    if platform_key not in ALL_ADAPTERS:
        raise PlatformAdapterError(
            f"不支持的平台: {platform_key}，"
            f"可选第三方平台: {list(THIRD_PARTY_ADAPTERS.keys())}，"
            f"可选大厂官网: {list(COMPANY_ADAPTERS.keys())}"
        )

    return ALL_ADAPTERS[platform_key]()


def get_adapters_by_type(platform_type: str) -> list[BasePlatformAdapter]:
    """按类型获取所有适配器实例。

    Args:
        platform_type: 'third_party' 或 'company_official'。

    Returns:
        对应类型的适配器实例列表。
    """
    registry = THIRD_PARTY_ADAPTERS if platform_type == "third_party" else COMPANY_ADAPTERS
    return [adapter_cls() for adapter_cls in registry.values()]


def list_platforms() -> dict[str, list[str]]:
    """列出所有支持的平台。

    Returns:
        按类型分组的平台标识列表。
    """
    return {
        "third_party": list(THIRD_PARTY_ADAPTERS.keys()),
        "company_official": list(COMPANY_ADAPTERS.keys()),
    }
