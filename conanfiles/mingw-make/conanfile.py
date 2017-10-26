from conans import ConanFile
import os
import shutil

class MinGwMakeConan(ConanFile):
    name = "mingw-make"
    version = "3.82"
    # There is no logic so far of having different binaries for different settings
    #sounds settings could be removed
    settings = "os"
    build_policy = "missing"
    description = "mingw-make for windows"
    
    def build(self):
        if self.settings.os == "Windows":
            self.run("git clone https://github.com/zabeloliver/conan-mingw-make.git")
            shutil.move("conan-mingw-make/make.exe", "conan-mingw-make/mingw32-make.exe")

    def package(self):
        self.copy(pattern="*", src="conan-mingw-make", dst="bin/", keep_path=True)

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))