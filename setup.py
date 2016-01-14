#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

# Gives the relative path of a file from the setup.py
relpath = lambda filename: os.path.join(os.path.dirname(__file__), filename)

# Read the README file
README = open(relpath('README.rst')).read()

setup(
    author='Fernando Felix do Nascimento Junior',
    author_email='fernandojr.ifcg@live.com',
    classifiers=[
        'Environment :: Web Environment',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],  # see more: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    description='A observer pattern implementation in Python based on jQuery.',
    keywords='observer design pattern',
    license='MIT License',
    long_description=README,
    name='observer',
    py_modules='observer',
    platforms='any',
    url='https://github.com/fernandojunior/observer',
    version='1.0.0',
    zip_safe=False
)
