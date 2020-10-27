#!/usr/bin/env python
"""NavConfig
    Configuration Service for Navigator and DataIntegrator.
See:
https://github.com/phenobarbital/NavConfig
"""

from setuptools import setup, find_packages

setup(
    name='navconfig',
    version=open("VERSION").read().strip(),
    python_requires=">=3.7.0",
    url='https://github.com/phenobarbital/NavConfig',
    description='Configuration tool for Navigator Services',
    long_description='Configuration tool for Navigator Services',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.7',
    ],
    author='Jesus Lara',
    author_email='jlara@trocglobal.com',
    packages=find_packages(),
    install_requires=[
        'numpy >= 1.16.2',
        'asyncio==3.4.3',
        'python-dotenv==0.14.0',
        'PyDrive==1.3.1',
        'asyncdb==1.0.0',
        'yapf==0.30.0',
        'isort==5.6.4',
        'black==20.8b1'
    ],
    project_urls={  # Optional
        'Source': 'https://github.com/phenobarbital/NavConfig',
        'Funding': 'https://paypal.me/phenobarbital',
        'Say Thanks!': 'https://saythanks.io/to/phenobarbital',
    },
)
