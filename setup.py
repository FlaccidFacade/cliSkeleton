"""Package configuration."""
from setuptools import find_packages, setup


setup(
    name="cliSkeleton",
    version="0.1",
    packages=find_packages("src/modules"),
    include_package_data=True,
    package_dir={"":"src/modules"},
    install_requires=['Click',],
    entry_points={
        'console_scripts' : 
        ['cliSkeleton = main:start']
    },

)