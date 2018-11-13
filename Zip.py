# coding: utf-8
import pyminizip
import os
import shutil


class Zip(object):

    def __init__(self):
        pass

    def zip(self, zip_file_path, source_file_path, password):
        pyminizip.compress(source_file_path, None, zip_file_path, password, int(5))
        pass

    def unzip(self, zip_file_path, extract_path, password):
        pyminizip.uncompress(zip_file_path, password, extract_path, int(0))
        pass

    def test(self):
        if os.path.exists("test"):
            shutil.rmtree("test", True)
        os.makedirs("test", 0o777)
        self.zip("test/test.zip", "Zip.py", b"123")
        self.unzip("test/test.zip", "test", "123")


Zip = Zip()


