""" Minimal setup file """

from setuptools import setup, find_packages

setup(
    name='test',
    version='1.0',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
