import os

from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain
from conan.tools.files import copy

from conan import ConanFile


class HelloConan(ConanFile):
    name = "hello"
    version = "0.1"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Hello here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Generators
    generators = "CMakeToolchain", "CMakeDeps"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        generators_dir = os.path.join(
            "build",
            "os-system",
            "os-arch",
            "conan",
            "generators",
        )

        build_dir = os.path.join("build", "os-system", "os-arch", "target")

        self.folders.root = os.path.join("..", "..")
        self.folders.source = "."
        self.folders.build = build_dir
        self.folders.generators = generators_dir

    def export_sources(self):
        copy(
            self,
            "CMakeLists.txt",
            os.path.join(self.recipe_folder, os.path.join("..", "..")),
            self.export_sources_folder,
        )

        copy(
            self,
            "src/*",
            os.path.join(self.recipe_folder, os.path.join("..", "..")),
            self.export_sources_folder,
        )

        copy(
            self,
            "include/*",
            os.path.join(self.recipe_folder, os.path.join("..", "..")),
            self.export_sources_folder,
        )

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["hello"]

    def requirements(self):
        self.requires("sqlite3/3.39.3")
        self.requires("sqlitecpp/3.2.0")

    def configure(self):
        if self.settings.os in ["iOS", "tvOS", "watchOS"]:
            self.options["sqlite3"].omit_load_extension = True
        else:
            self.options["sqlite3"].omit_load_extension = False

        self.options["sqlite3"].threadsafe = 1
        self.options["sqlite3"].build_executable = False
