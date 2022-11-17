import sys

from .bloom import BloomFilter  # noqa: F401

if sys.version_info < (3, 7):
    raise EnvironmentError("Python 3.7 or above is required")
