from conans import ConanFile
import os


class ArmGccConan(ConanFile):
    license = "none"
    settings = "os"
    generators = "virtualenv"
    description = "GCC for ARM Cross-Compiling for Windows"
    build_policy = "missing"
    
    def build(self):
        if self.settings.os == "none":
            if self.version == "4.9.3":
                self.run("git clone https://github.com/zabeloliver/conan-arm-gcc.git && cd conan-arm-gcc && git checkout arm-gcc-493")
            elif self.version == "6.2":
                self.run("git clone https://github.com/zabeloliver/conan-arm-gcc.git && cd conan-arm-gcc && git checkout arm-gcc-62")
        
    def package(self):
        #self.run("dir")
        self.copy(pattern="*", src="conan-arm-gcc", dst="toolchain", keep_path=True, excludes="*.cmake")
        self.copy(pattern="*.cmake", src="conan-arm-gcc", dst="toolchainfile")
    
    def package_info(self):
        self.env_info.TOOLCHAIN_PATH = os.path.join(self.package_folder, "toolchain")