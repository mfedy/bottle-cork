#!/usr/bin/env python

from setuptools import setup

__version__ = '0.5.3'

CLASSIFIERS = map(str.strip,
"""Environment :: Console
License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)
Natural Language :: English
Operating System :: POSIX :: Linux
Programming Language :: Python
Topic :: Internet :: WWW/HTTP :: WSGI
Topic :: Security
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines())

setup(
    name="bottle-cork",
    version = __version__,
    author = "Federico Ceratto",
    author_email = "federico.ceratto@gmail.com",
    description = "Authentication/Authorization library for Bottle",
    license = "LGPLv3+",
    url = "http://cork.firelet.net/",
    long_description = "Cork is a simple Authentication/Authorization library" \
        "for the Bottle web framework.",
    classifiers=CLASSIFIERS,
    python_requires=">=3.5",
    install_requires = [
        'bottle==0.11.6',
        'Beaker==1.8.0',
        'couchbase==4.0.5',
        'setuptools',
    ],
    packages = ['cork'],
    platforms = ['Linux'],
    test_suite='nose.collector',
    tests_require=['nose'],
)


