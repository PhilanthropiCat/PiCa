from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = "0.2.0"
DESCRIPTION = "PiCa is lightweight and minimalist package for autodiff."



# Setting up
setup(
    name="picalib",
    version=VERSION,
    author="Phikat",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(include=['pica']),
    install_requires=["networkx","matplotlib"],
)
