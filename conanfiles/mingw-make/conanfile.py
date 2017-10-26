from conans import ConanFile
import os
import shutil

class MinGwMakeConan(ConanFile):
    name = "mingw-make"
    version = "3.82"
    settings = "os", "compiler", "arch"
    enerators = "virtualenv"
    build_policy = "missing"
    description = "mingw-make for windows"
    
    def source(self):
        self.run("git clone https://github.com/zabeloliver/conan-mingw-make.git")
        shutil.move("mingw-make/make.exe", "mingw-make/mingw32-make.exe")

    def package(self):
        self.copy(pattern="*", src="mingw-make", dst="bin/", keep_path=True)

    def package_info(self):
        self.env_info.MAKE_PATH = os.path.join(self.package_folder, "bin")
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))