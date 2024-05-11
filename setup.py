#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages


def _load_requires_from_file(filepath):
    return [pkg_name.rstrip('\r\n') for pkg_name in open(filepath).readlines()]


def _install_requires():
    requires = _load_requires_from_file('requirements.txt')
    if sys.version_info >= (2, 7, 0):
        requires.remove('argparse')
    return requires


def _packages():
    return find_packages(
        exclude=[
            '*.tests',
            '*.tests.*',
            'tests.*',
            'tests'
        ],
    )


if __name__ == '__main__':
    description = 'Conversion script to Ansible inventory file ' \
                  'from OpenSSH configuration'
    setup(
        name='study',
        version='1.0.0',
        description=description,
        author='kachi',
        author_email='ykachip@gmail.com',
        url='https://github.com/ykachip/ec-study.git',
        classifiers=[
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.10',
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: Apache Software License',
            'Intended Audience :: Developers',
            'Natural Language :: Japanese',
            'Operating System :: POSIX'
        ],
        packages=_packages(),
        install_requires=_install_requires(),
        include_package_data=True,
        zip_safe=False,
        entry_points={
            "console_scripts": ""
            }
    )
