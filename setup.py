#!/usr/bin/env python3

# Copyright (C) 2019-2023 The Xaya developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from setuptools import setup, Extension

neoscrypt_module = Extension('neoscrypt',
                               sources = ['neoscryptmodule.c',
                                          'neoscrypt.c'],
                               include_dirs=['.'])

setup (name = 'neoscrypt_python',
       version = '1.0.4',
       license = 'MIT',
       description = 'Bindings for the NeoScrypt proof-of-work algorithm',
       author = 'Autonomous Worlds Ltd',
       author_email = 'info@autonomousworlds.com',
       url = 'https://github.com/xaya/neoscrypt_python',
       download_url = 'https://github.com/xaya/neoscrypt_python/archive/v1.0.4.tar.gz',
       ext_modules = [neoscrypt_module])
