#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

extras_require = {
    "test": [
        "pytest>=6.2.5",
        "hypothesis>=3.31.2",
        "tox>=2.6.0",
    ],
    "lint": [
        "flake8>=3.8.3",
        "mypy==0.910",
        "isort>=4.2.15",
        "black>=22.1.0",
    ],
    "deploy": [
        "bumpversion",
        "wheel",
    ],
    "dev": [
        "twine",
        "build",
    ],
}

extras_require["dev"] = (
    extras_require["deploy"]
    + extras_require["dev"]
    + extras_require["test"]
    + extras_require["lint"]
)

with open("./README.md") as readme:
    long_description = readme.read()

setup(
    name="eth-bloom",
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version="1.0.4",
    description="""Python implementation of the Ethereum Trie structure""",
    long_description_content_type="text/markdown",
    long_description=long_description,
    author="Piper Merriam",
    author_email="pipermerriam@gmail.com",
    url="https://github.com/ethereum/eth-bloom",
    include_package_data=True,
    py_modules=["eth_bloom"],
    install_requires=[
        "eth-hash[pycryptodome]>=0.4.0",
    ],
    python_requires=">=3.7, <4",
    extras_require=extras_require,
    license="MIT",
    zip_safe=False,
    package_data={"eth_bloom": ["py.typed"]},
    keywords="ethereum blockchain evm trie merkle",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
