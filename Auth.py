# coding: utf-8
from Logger import Logger
from PathMgr import PathMgr
from PathType import PathType


class Auth:
    config_file_path = None

    def __init__(self):
        config_file_path = PathMgr.get_path(PathType.AuthConfigPath)
        Logger.info(config_file_path)
        pass
