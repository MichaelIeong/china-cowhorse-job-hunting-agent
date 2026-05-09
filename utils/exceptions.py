"""
自定义异常类模块。

统一管理项目中的异常类型。
"""


class BaseError(Exception):
    """项目基础异常类。"""

    def __init__(self, message: str = "发生未知错误"):
        self.message = message
        super().__init__(self.message)


class ValidationError(BaseError):
    """输入校验异常。"""

    def __init__(self, message: str = "输入校验失败"):
        super().__init__(message)


class NetworkError(BaseError):
    """网络请求异常。"""

    def __init__(self, message: str = "网络请求失败，请检查网络连接"):
        super().__init__(message)


class PlatformAdapterError(BaseError):
    """平台适配器异常。"""

    def __init__(self, message: str = "平台适配器调用失败"):
        super().__init__(message)


class DataStorageError(BaseError):
    """数据存储异常。"""

    def __init__(self, message: str = "数据读写失败"):
        super().__init__(message)


class ParserError(BaseError):
    """数据解析异常。"""

    def __init__(self, message: str = "数据解析失败"):
        super().__init__(message)


class ConfigError(BaseError):
    """配置异常。"""

    def __init__(self, message: str = "配置加载失败"):
        super().__init__(message)
