from setuptools import setup, find_packages

setup(
   name='jsonapi',
   version='1.0',
   description='A useful module',
   author='Marcela Vijil',
   author_email='vijil.m@northeastern.edu',
   packages=['src.jsonapi'],  #same as name
   install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
)