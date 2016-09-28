#!/usr/bin/env python

from setuptools import setup, find_packages


install_requires = [
    'numpy',
    'scipy',
]

setup(
    name="demo_pkg",
    version=0.1,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    # description="Utility scripts ",
    author="Tim Staley",
    author_email="github@timstaley.co.uk",
    # url="https://github.com/",
    install_requires=install_requires,
)
