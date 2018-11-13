from enum import Enum


class PathType(Enum):
    AuthConfigPath: str
    OutputRootPath: str
    InputExcelPath: str
    CacheConfigDir: str
    CacheConfigPath: str
