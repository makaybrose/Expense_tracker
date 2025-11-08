#this file is created to allow folders to be seen as models for easy access.
#the init file in the app makes python see the app as a module

from setuptools import setup, find_packages

setup(
    name = "expense-tracker",
    version = "0.1.0",
    packages = find_packages()
)