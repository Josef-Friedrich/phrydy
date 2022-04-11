import os

from setuptools import setup, find_packages
import versioneer

def read(file_name):
    """
    Read the contents of a text file and return its content.

    :param str file_name: The name of the file to read.

    :return: The content of the text file.
    :rtype: str
    """
    return open(
        os.path.join(os.path.dirname(__file__), file_name),
        encoding='utf-8'
    ).read()


setup(
    name='phrydy',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='A easy wrapper for mutagen',
    url='https://github.com/Josef-Friedrich/phrydy',
    author='Josef Friedrich',
    author_email='josef@friedrich.rocks',
    license='MIT',
    packages=find_packages(),
    long_description=read('README.rst'),
    long_description_content_type='text/x-rst',
    install_requires=[
        'mutagen==1.45',
        'enum34',
        'six>=1.10.0',
        'ansicolor',
        'mediafile==0.9.0',
        'typing-extensions==4.1.1',
    ],
    scripts=['bin/phrydy-debug'],
    zip_safe=False)
