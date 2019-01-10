#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

extras_require = {
    'test': [
        "pytest==3.0.7",
        "hypothesis==3.7.0",
        "tox==2.6.0",
    ],
    'lint': [
        "flake8>=3.5.0,<4.0.0",
        'mypy<0.600',
    ],
    'deploy': [
        'bumpversion>=0.5.3,<1.0.0',
        'wheel>=0.30.0,<1.0.0',
    ],
    'dev': [
        "twine",
    ],
}

extras_require['dev'] = (
    extras_require['deploy'] +
    extras_require['dev'] +
    extras_require['test'] +
    extras_require['lint']
)

setup(
    name='eth-bloom',
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version='1.0.3',
    description="""Python implementation of the Ethereum Trie structure""",
    long_description_markdown_filename='README.md',
    author='Piper Merriam',
    author_email='pipermerriam@gmail.com',
    url='https://github.com/ethereum/eth-bloom',
    include_package_data=True,
    py_modules=['eth_bloom'],
    setup_requires=['setuptools-markdown'],
    install_requires=[
        "eth-hash>=0.1.0a3,<0.3.0",
    ],
    python_requires='>=3.5, !=3.5.2, <4',
    extras_require=extras_require,
    license="MIT",
    zip_safe=False,
    package_data={'eth_bloom': ['py.typed']},
    keywords='ethereum blockchain evm trie merkle',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
