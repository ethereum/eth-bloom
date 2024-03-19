#!/usr/bin/env python
from setuptools import (
    find_packages,
    setup,
)

extras_require = {
    "dev": [
        "build>=0.9.0",
        "bumpversion>=0.5.3",
        "ipython",
        "pre-commit>=3.4.0",
        "tox>=4.0.0",
        "twine",
        "wheel",
    ],
    "docs": [
        "sphinx>=6.0.0",
        "sphinx_rtd_theme>=1.0.0",
        "towncrier>=21,<22",
    ],
    "test": [
        "hypothesis>=3.31.2",
        "pytest>=7.0.0",
        "pytest-xdist>=2.4.0",
    ],
}

extras_require["dev"] = (
    extras_require["dev"] + extras_require["docs"] + extras_require["test"]
)

with open("./README.md") as readme:
    long_description = readme.read()

setup(
    name="eth-bloom",
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version="3.0.0",
    description="""A python implementation of the bloom filter used by Ethereum""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="The Ethereum Foundation",
    author_email="snakecharmers@ethereum.org",
    url="https://github.com/ethereum/eth-bloom",
    include_package_data=True,
    install_requires=[
        "eth-hash[pycryptodome]>=0.4.0",
    ],
    python_requires=">=3.8, <4",
    extras_require=extras_require,
    py_modules=["eth_bloom"],
    license="MIT",
    zip_safe=False,
    keywords="ethereum blockchain evm trie merkle",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"eth_bloom": ["py.typed"]},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
