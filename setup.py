# Upload package to PyPi.

from setuptools import setup

setup(name='yalies',
      version='2.0.0',
      description='Library for easy interaction with the Yalies API (yalies.io/api)',
      url='https://github.com/Yalies/python-yalies',
      author='Erik Boesen',
      author_email='me@erikboesen.com',
      license='MIT',
      packages=['yalies'],
      install_requires=['requests'])
