# setup.py

from setuptools import setup, find_packages
from os import path

import pylitproject.__about__ as about
import pylitproject.__version__ as version

with open('README.rst') as f:
    long_description = f.read()

setup (
    name = about.__title__,
    author = about.__author__,
    author_email = about.__email__,
    url = about.__url__,
    varsion = version.__version__,
    description = about.__summary__,
    long_description = long_description,
    license = about.__license__,
    install_requires = [],
    packages = find_packages(exclude=['docs', 'tests', 'rst']),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Documentation'
    ]
)
