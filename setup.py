#!/usr/bin/env python

from setuptools import setup, Extension


setup(
    name="mecab-python-windows",
	version="0.99.6",
	py_modules=["MeCab"],
	ext_modules=[
		Extension(
		    "_MeCab",
			["MeCab_wrap.cxx",],
			include_dirs=["C:\Program Files (x86)\MeCab\sdk"],
			library_dirs=["C:\Program Files (x86)\MeCab\sdk"],
			libraries=["libmecab"]
		)
	],
	author='Yukino Ikegami',
    author_email='yknikgm@gmail.com',
	platforms=['Windows'],
	classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: Microsoft',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing'
    ],
	description='Python wrapper for MeCab on Windows: Morphological Analysis engine',
	long_description='''This is a python wrapper for MeCab. It works on Windows.

License
---------
MeCab is copyrighted free software by Taku Kudo <taku@chasen.org> and Nippon Telegraph and Telephone Corporation, and is released under any of the GPL (see the file GPL), the LGPL (see the file LGPL), or the BSD License (see the file BSD).
'''
)