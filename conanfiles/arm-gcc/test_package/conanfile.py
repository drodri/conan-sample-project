from conans import ConanFile
import os


class Test(ConanFile):

    def build(self):
        print os.getenv("TOOLCHAIN_PATH")

    def test(self):
        pass