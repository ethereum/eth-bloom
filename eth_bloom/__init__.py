import sys
import warnings

from .bloom import BloomFilter  # noqa: F401


if sys.version_info.major < 3:
    warnings.simplefilter('always', DeprecationWarning)
    warnings.warn(DeprecationWarning(
        "The `eth-bloom` library is dropping support for Python 2.  Upgrade to Python 3."
    ))
    warnings.resetwarnings()
