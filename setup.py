from setuptools import setup, find_packages

VERSION = "0.1"
DESCRIPTION = "PiCa is lightweight and minimalist package for autodiff."


# Setting up
setup(
    name="picalib",
    version=VERSION,
    author="Phikat",
    description=DESCRIPTION,
    packages=find_packages(include=['pica']),
    install_requires=["networkx","matplotlib"],
)
