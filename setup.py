#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function

import os
import sys
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='phrydy',
    version='0.0.3',
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
