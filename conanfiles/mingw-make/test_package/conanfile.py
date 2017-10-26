from conans import ConanFile
import os


class Test(ConanFile):

    def build(self):
        print os.getenv("PATH")
        self.run("mingw32-make --version")
        self.run("where mingw32-make")

    def test(self):
        pass