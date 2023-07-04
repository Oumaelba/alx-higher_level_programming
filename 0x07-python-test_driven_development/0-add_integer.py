#!/usr/bin/python3
"""
This module contains the function add_integer.
"""


def add_integer(a, b=98):
    """
    Function to add two integers.

    Parameters:
    - a: An integer or float value.
    - b: An integer or float value. (Default: 98)

    Returns:
    - The sum of `a` and `b` as an integer.

    Raises:
    - TypeError: If `a` or `b` is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
