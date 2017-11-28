#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='eth-bloom',
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version='0.5.2',
    description="""Python implementation of the Ethereum Trie structure""",
    long_description_markdown_filename='README.md',
    author='Piper Merriam',
    author_email='pipermerriam@gmail.com',
    url='https://github.com/ethereum/eth-bloom',
    include_package_data=True,
    py_modules=['eth_bloom'],
    setup_requires=['setuptools-markdown'],
    install_requires=[
        "pysha3>=0.3",
    ],
    license="MIT",
    zip_safe=False,
    keywords='ethereum blockchain evm trie merkle',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
