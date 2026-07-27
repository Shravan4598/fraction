"""
fraction
~~~~~~~~

A lightweight, pure-Python Fraction data type.

Example
-------
>>> from fraction import fraction
>>> a = fraction(1, 2)
>>> b = fraction(3, 4)
>>> print(a + b)
5/4
"""

from .fraction import fraction

__all__ = ["fraction"]

__version__ = "1.0.0"
__author__ = "Shravan Kumar Pandey"
__license__ = "MIT"
