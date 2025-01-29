# Upload package to PyPi.

from setuptools import setup

with open('README.md', 'r') as file:
      long_description = file.read()

setup(name='yalies',
      version='2.0.1',
      description='Library for easy interaction with the Yalies API (yalies.io/api)',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/Yalies/python-yalies',
      author='Erik Boesen',
      author_email='me@erikboesen.com',
      license_files=('LICENSE'),
      packages=['yalies'],
      install_requires=['requests'])
