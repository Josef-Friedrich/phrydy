from setuptools import setup

setup(name='phrydy',
      version='0.3',
      description='A easy wrapper for mutagen',
      url='https://github.com/Josef-Friedrich/phrydy',
      author='Josef Friedrich',
      author_email='josef@friedrich.rocks',
      license='MIT',
      packages=['phrydy'],
      install_requires=['mutagen','enum','six'],
      zip_safe=False)
