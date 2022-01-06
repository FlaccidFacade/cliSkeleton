"""Package configuration."""
from setuptools import find_packages, setup

#TODO make sure this works for fresh install

setup(
    name="report",
    version="0.1",
    packages=find_packages("src"),
    include_package_data=True,
    package_dir={"":"src"},
    install_requires=['Click',],
    entry_points={
        'console_scripts' : 
        ['report = main:start']
    },

)