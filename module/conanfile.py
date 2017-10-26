from conans import ConanFile, CMake
import os


class MyModule(ConanFile):
    name = "module"
    version = "0.1"
    # Just remove "os"
    settings = "compiler", "arch"
    exports_sources = "src/*"
    build_requires = "mingw-make/3.82@user/testing"

    def configure(self):
        del self.settings.compiler.libcxx #Pure C

    def build_requirements(self):
        if self.settings.compiler == "gcc" and self.settings.arch=="armv6":
            if self.settings.compiler.version == "4.9":
                self.build_requires("arm-gcc/4.9.3@user/testing")

    def build(self):
        cmake = CMake(self)
        toolchain_path = os.getenv("TOOLCHAIN_PATH")
        self.run('cmake %s/src -DCMAKE_TOOLCHAIN_FILE=%s/arm-none-eabi-gcc.cmake -G"MinGW Makefiles"'
                % (self.source_folder, toolchain_path))
        self.run("cmake --build . %s" % cmake.build_config)
        
    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
    
    def package_info(self):
        self.cpp_info.libs = ["module"]