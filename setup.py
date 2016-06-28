#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-env',
    version='0.1.0',
    author='Ana Ribeiro',
    author_email='aninhacostaribeiro@gmail.com',
    maintainer='Ana Ribeiro',
    maintainer_email='aninhacostaribeiro@gmail.com',
    license='Mozilla Public License 2.0',
    url='https://github.com/ribeiroana/pytest-env',
    description='Plugin to show the environment where the tests were executed',
    long_description=read('README.rst'),
    py_modules=['pytest_env'],
    install_requires=['pytest>=2.9.1'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        
    ],
    entry_points={
        'pytest11': [
            'env = pytest_env',
        ],
    },
)
