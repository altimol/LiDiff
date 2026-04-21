from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename) as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#")
        ]

setup(
    name="lidiff",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=parse_requirements("requirements.txt"),
    package_data={
        "lidiff": [ 
            "*.cu",
            "*.cpp",
            "*.h",
            "*.cuh",
            "*.sh",
            "*.txt",
            "*.yaml",
            "*.pth",
            "**/*.cu",
            "**/*.cpp",
            "**/*.h",
            "**/*.cuh",
            "**/*.sh",
            "**/*.txt",
            "**/*.yaml",
            "**/*.pth",
        ]
    },
)
