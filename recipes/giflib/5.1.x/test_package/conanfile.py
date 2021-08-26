from conans import ConanFile, CMake, tools
import os


class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake", "cmake_find_package"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self):
            img_name = os.path.join(self.source_folder, "testimg.gif")
            bin_path = os.path.join("bin", "test_package")
            command = "{} {}".format(bin_path, img_name)
            self.run(command, run_environment=True)
