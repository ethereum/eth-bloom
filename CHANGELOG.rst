eth-bloom v3.1.0 (2025-01-08)
-----------------------------

Features
~~~~~~~~

- Merge template, including adding support for py313 and replacing ``bumpversion`` with ``bumpmyversion``. (`#48 <https://github.com/ethereum/eth-bloom/issues/48>`__)


eth-bloom v3.0.1 (2024-04-24)
-----------------------------

Internal Changes - for eth-bloom Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Change the name of ``master`` branch to ``main`` (`#41 <https://github.com/ethereum/eth-bloom/issues/41>`__)
- Merge template updates, notably adding python 3.12 support (`#44 <https://github.com/ethereum/eth-bloom/issues/44>`__)


Miscellaneous Changes
~~~~~~~~~~~~~~~~~~~~~

- `#45 <https://github.com/ethereum/eth-bloom/issues/45>`__


eth-bloom v3.0.0 (2023-10-30)
-----------------------------

Breaking Changes
~~~~~~~~~~~~~~~~

- Drop python 3.7 support (`#40 <https://github.com/ethereum/eth-bloom/issues/40>`__)


Internal Changes - for eth-bloom Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Merge updates from the python project template (`#40 <https://github.com/ethereum/eth-bloom/issues/40>`__)


2.0.0 (Nov. 28, 2022)
---------------------

- Drop support for python 3.6
- Add support for python 3.8, 3.9, 3.10, 3.11
- Modernize `setup.py`, `tox.ini`, `config.yaml`, `Makefile`, and docs
- Add and run `isort`
- Add and run `black`

0.5.0
-----

* Rename python library name to `eth-bloom`
* Deprecation warning for python 2

0.4.0
-----

* Add `BloomFilter.from_iterable` API
* Add `BloomFilter.extend` API
* Allow use of integer types with `|`, `|=`, `+` and `+=` operations.

0.2.0
-----

* Add API for combining filters.

0.1.0
-----

* Initial Release
