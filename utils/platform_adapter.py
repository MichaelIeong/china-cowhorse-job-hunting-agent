"""
招聘平台适配器模块。

使用适配器模式，每个招聘平台一个适配器类，提供统一的接口。
"""

from abc import ABC, abstractmethod
from typing import Optional

from utils.exceptions import PlatformAdapterError


class BasePlatformAdapter(ABC):
    """招聘平台适配器基类。

    所有平台适配器必须继承此类并实现抽象方法。
    """

    def __init__(self, platform_name: str, base_url: str):
        """初始化适配器。

        Args:
            platform_name: 平台名称。
            base_url: 平台基础 URL。
        """
        self.platform_name = platform_name
        self.base_url = base_url

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


class BossAdapter(BasePlatformAdapter):
    """Boss直聘适配器。"""

    def __init__(self):
        super().__init__("Boss直聘", "https://www.zhipin.com")

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
        super().__init__("牛客网", "https://www.nowcoder.com")

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
        super().__init__("拉勾", "https://www.lagou.com")

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
        super().__init__("猎聘", "https://www.liepin.com")

    def search_jobs(self, keyword: str, city: Optional[str] = None, **kwargs) -> list[dict]:
        """搜索猎聘岗位。"""
        # TODO: 实现具体搜索逻辑
        raise PlatformAdapterError("猎聘搜索功能尚未实现")

    def get_job_detail(self, job_id: str) -> dict:
        """获取猎聘岗位详情。"""
        # TODO: 实现具体获取逻辑
        raise PlatformAdapterError("猎聘详情获取功能尚未实现")


def get_adapter(platform_key: str) -> BasePlatformAdapter:
    """根据平台标识获取对应适配器实例。

    Args:
        platform_key: 平台标识（如 'boss', 'nowcoder'）。

    Returns:
        对应平台的适配器实例。

    Raises:
        PlatformAdapterError: 不支持的平台。
    """
    adapters: dict[str, type[BasePlatformAdapter]] = {
        "boss": BossAdapter,
        "nowcoder": NowcoderAdapter,
        "lagou": LagouAdapter,
        "liepin": LiepinAdapter,
    }

    if platform_key not in adapters:
        raise PlatformAdapterError(f"不支持的平台: {platform_key}，可选: {list(adapters.keys())}")

    return adapters[platform_key]()
