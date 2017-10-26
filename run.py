import os

def run(command):
    retcode = os.system(command)
    if retcode != 0:
        raise Exception("Error while executing:\n\t %s" % command)


run("cd conanfiles/mingw-make && conan create user/testing")
run("cd conanfiles/arm-gcc && conan create arm-gcc/4.9.3@user/testing")
run("cd module && conan create user/testing -s compiler=gcc -s compiler.version=4.9 -s arch=armv6")
