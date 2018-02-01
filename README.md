# Ethereum Bloom Filter

[![Build Status](https://travis-ci.org/ethereum/eth-bloom.svg?branch=master)](https://travis-ci.org/ethereum/eth-bloom)
[![PyPI version](https://badge.fury.io/py/eth-bloom.svg)](https://badge.fury.io/py/eth-bloom)
[![Python versions](https://img.shields.io/pypi/pyversions/eth-bloom.svg)](https://pypi.python.org/pypi/eth-bloom)

A python implementation of the bloom filter used by Ethereum.

> This library and repository was previously located at https://github.com/pipermerriam/ethereum-bloom.  It was transferred to the Ethereum foundation github in November 2017 and renamed to `eth-bloom`.  The PyPi package was also renamed from `ethereum-bloom` to `eth-bloom.

## Installation

```shell
$ pip install eth-bloom
```


## Development

```sh
pip install -e . -r requirements-dev.txt
```


### Running the tests

You can run the tests with:

```sh
py.test tests
```

Or you can install `tox` to run the full test suite.


### Releasing

Pandoc is required for transforming the markdown README to the proper format to
render correctly on pypi.

For Debian-like systems:

```
apt install pandoc
```

Or on OSX:

```sh
brew install pandoc
```

To release a new version:

```sh
bumpversion $$VERSION_PART_TO_BUMP$$
git push && git push --tags
make release
```


#### How to bumpversion

The version format for this repo is `{major}.{minor}.{patch}` for stable, and
`{major}.{minor}.{patch}-{stage}.{devnum}` for unstable (`stage` can be alpha or beta).

To issue the next version in line, use bumpversion and specify which part to bump,
like `bumpversion minor` or `bumpversion devnum`.

If you are in a beta version, `bumpversion stage` will switch to a stable.

To issue an unstable version when the current version is stable, specify the
new version explicitly, like `bumpversion --new-version 4.0.0-alpha.1 devnum`


## Usage

The `BloomFilter` object

```python
>>> from eth_bloom import BloomFilter
>>> b = BloomFilter()
>>> b'a value' in b  # check whether a value is present
False
>>> b.add(b'a value')  # add a single value
>>> b'a value' in b
True
>>> int(b)  # cast to an integer
3458628712844765018311492773359360516229024449585949240367644166080576879632652362184119765613545163153674691520749911733485693171622325900647078772681584616740134230153806267998022370194756399579977294154062696916779055028045657302214591620589415314367270329881298073237757853875497241510733954508399863880080986777555986663988492288946856978031023631618215522505971170427986911575695114157059398791122395379400594948096
>>> bin(b)  # cast to a binary string
'0b100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
```

You can also add an iterable of items to a bloom filter.

```python
>>> b = BloomFilter()
>>> b'value-a' in b
False
>>> b'value-b' in b
False
>>> b.extend([b'value-a', b'value-b'])
>>> b'value-a' in b
True
>>> b'value-b' in b
True
```

You can initialize a bloom filter from an iterable of byte strings.

```python
>>> b = BloomFilter.from_iterable([b'value-a', b'value-b'])  # initialize from an iterable of values.
>>> b'value-a' in b
True
>>> b'value-b' in b
True
```

You can initialize a bloom filter from the integer representation of the bloom bits.

```python
>>> b = BloomFilter(3458628712844765018311492773359360516229024449585949240367644166080576879632652362184119765613545163153674691520749911733485693171622325900647078772681584616740134230153806267998022370194756399579977294154062696916779055028045657302214591620589415314367270329881298073237757853875497241510733954508399863880080986777555986663988492288946856978031023631618215522505971170427986911575695114157059398791122395379400594948096)
>>> b'a value' in b
True
```

You can also merge bloom filters

```python
>>> from eth_bloom import BloomFilter
>>> b1 = BloomFilter()
>>> b2 = BloomFilter()
>>> b1.add(b'a')
>>> b1.add(b'common')
>>> b2.add(b'b')
>>> b2.add(b'common')
>>> b'a' in b1
True
>>> b'b' in b1
False
>>> b'common' in b1
True
>>> b'a' in b2
False
>>> b'b' in b2
True
>>> b'common' in b2
True
>>> b3 = b1 + b2  # using addition
>>> b'a' in b3
True
>>> b'b' in b3
True
>>> b'common' in b3
True
>>> b4 = b1 | b2  # or using bitwise or
>>> b'a' in b4
True
>>> b'b' in b4
True
>>> b'common' in b4
True
>>> b1 |= b2  # or using in-place operations (works with += too)
>>> b'a' in b1
True
>>> b'b' in b1
True
>>> b'common' in b1
True
```
