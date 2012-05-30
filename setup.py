#!/usr/bin/env python

from setuptools import setup, find_packages
import sys

from bodatools import __version__

LONG_DESCRIPTION = None
try:
    # read the description if it's there
    with open('README.rst') as desc_f:
        LONG_DESCRIPTION = desc_f.read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
]

install_requires=[]
if sys.version_info < (2, 7):
    install_requires.append("argparse==1.1")

setup(
    name='bodatools',
    version=__version__,
    author='Emory University Libraries',
    author_email='libsysdev-l@listserv.cc.emory.edu',
    url='https://github.com/emory-libraries/bodatools',
    license='Apache License, Version 2.0',
    packages=find_packages(),
    install_requires=install_requires,
    description='A collection of python utilities and scripts for working with binary files',
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    scripts=[
        'scripts/export-email',
    ],
)
