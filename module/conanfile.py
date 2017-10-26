from conans import ConanFile, CMake
import os


class MyModule(ConanFile):
    name = "module"
    version = "0.1"
    settings = "os", "compiler", "arch"
    exports_sources = "src/*"
    requires = "mingw-make/3.82@user/testing"
    
    def imports(self):
        self.copy("*.cmake", "", "")
        self.copy("*.bat",  "", "")

    def build(self):        
        if self.settings.os == "none" and self.settings.compiler == "armgcc":
            if self.settings.compiler.version == "4.9.3":
                self.build_requires("arm-gcc/4.9.3@user/stable")
                cmake = CMake(self)
                self.run('cmake %s/src -DCMAKE_TOOLCHAIN_FILE=arm-none-eabi-gcc.cmake -G"MinGW Makefiles"' % (self.source_folder))
                self.run("cmake --build . %s" % cmake.build_config)
            elif self.settings.compiler.version == "6.2":
                self.build_requires("arm-gcc/6.2@user/stable")
            else:
                return
        
    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
    
    def package_info(self):
        self.cpp_info.libs = ["module"]