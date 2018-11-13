import os
import platform
import tempfile
from PathType import PathType


class PathMgr(object):
    root_path: str
    temp_path: str

    def __init__(self):
        self.root_path = os.path.basename(__file__)
        self.temp_path = '/tmp' if platform.system() == 'Darwin' else tempfile.gettempdir()
        pass

    def get_path(self, path_type):
        if path_type is PathType.AuthConfigPath:
            return self.root_path + os.sep + ""
        if path_type is PathType.CacheConfigDir:
            return self.root_path + os.sep + str(PathType.AuthConfigPath)
        if path_type is PathType.InputExcelPath:
            return self.root_path + os.sep + str(PathType.AuthConfigPath)
        if path_type is PathType.OutputRootPath:
            return self.root_path + os.sep + str(PathType.AuthConfigPath)
        pass


# PathMgr
PathMgr = PathMgr()
