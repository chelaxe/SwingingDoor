#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

setup
=====

Package installation script.

"""

from setuptools import setup

import swinging_door

setup(
    name="swinging_door",
    version=swinging_door.__version__,
    description="Implementation of the SwingingDoor algorithm in Python.",
    long_description=swinging_door.__doc__,
    long_description_content_type="text/x-rst",
    author="Aleksandr F. Mikhaylov (ChelAxe)",
    author_email="chelaxe@gmail.com",
    url="https://github.com/chelaxe/SwingingDoor",
    py_modules=["swinging_door"],
    scripts=["swinging_door.py"],
    license="MIT",
    platforms="any",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development",
        "Typing :: Typed",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
