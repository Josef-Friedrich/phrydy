#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function

import os
from setuptools import setup
import phrydy

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


VERSION = phrydy.__version__

setup(
    name='phrydy',
    version=VERSION,
    description='A easy wrapper for mutagen',
    url='https://github.com/Josef-Friedrich/phrydy',
    author='Josef Friedrich',
    author_email='josef@friedrich.rocks',
    license='MIT',
    packages=['phrydy'],
    long_description=read('README.rst'),
    install_requires=[
        'mutagen>=1.33', 'enum34', 'six>=1.9'
    ],
    zip_safe=False)
