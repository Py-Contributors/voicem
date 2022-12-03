import setuptools
from glob import glob

from voicem.about import *

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name=__package_name__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    data_files=[('assets', glob('random_profile/assets/*'))],
    url=__github__,
    packages=setuptools.find_packages(),
    project_urls={"Documentation": "https://pycontributors.readthedocs.io/projects/voicem/en/latest/",
                  "Source": "https://github.com/Py-Contributors/voicem",
                  "Tracker": "https://github.com/Py-Contributors/voicem/issues",
                  "Funding": "https://github.com/sponsors/codePerfectPlus"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Environment :: Plugins"],
)
