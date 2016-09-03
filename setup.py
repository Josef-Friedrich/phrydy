import os
from setuptools import setup

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name='phrydy',
	version='0.0.2',
	description='A easy wrapper for mutagen',
	url='https://github.com/Josef-Friedrich/phrydy',
	author='Josef Friedrich',
	author_email='josef@friedrich.rocks',
	license='MIT',
	packages=['phrydy'],
	long_description=read('README.rst'),
	install_requires=['mutagen', 'enum', 'six'],
	zip_safe=False
)
