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
    version = version.__version__,
    description = about.__summary__,
    description_content_type = 'text/x-rst',
    long_description = long_description,
    long_description_content_type = 'text/x-rst',
    license = about.__license__,
    install_requires = [],
    entry_points = {
        'console_scripts': [
            'pylit=pyitproject.__main__:main',
        ]
    },
    packages = find_packages(exclude=['docs', 'tests', 'rst', '_venv']),
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
