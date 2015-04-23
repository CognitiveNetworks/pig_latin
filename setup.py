#!/usr/bin/env python
import os

__author__ = 'Mark Fox <mark.fox@cognitivenetworks.com>'

dependencies = []


# allow use of setuptools/distribute or distutils
kw = {}
try:
    from setuptools import setup

    kw['install_requires'] = dependencies
#     kw['entry_points'] = """
#     [console_scripts]
#     hello = cn_test_pypi.hello_world:main
# """

except ImportError:
    from distutils.core import setup

    kw['requires'] = dependencies

try:
    here = os.path.dirname(os.path.abspath(__file__))
    long_description = file(os.path.join(here, 'README.md')).read()
except IOError:
    long_description = ''

setup(
    name='pig_latin',
    version='0.0.2',
    description='Pig Latin translation library.',
    long_description=long_description,
    author='Mark Fox',
    author_email='mark.fox@cognitivenetworks.com',
    url='https://github.com/CognitiveNetworks/pig_latin',
    license='',
    packages=['pig_latin'],
    test_suite='nose.collector',
    **kw
)