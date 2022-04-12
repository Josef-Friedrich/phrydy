#! /usr/bin/env python

import os
import phrydy


def path(*path_segments):
    return os.path.join(os.getcwd(), *path_segments)


def open_file(*path_segments):
    file_path = path(*path_segments)
    open(file_path, 'w').close()
    return open(file_path, 'a')


template = open(path('README_template.rst'), 'r').read()
readme = open_file('README.rst')

template = template.replace('<< fields documentation table >>',
                             phrydy.doc_generator.format_fields_as_rst_table())

print(template)
readme.write(template)
readme.close()
