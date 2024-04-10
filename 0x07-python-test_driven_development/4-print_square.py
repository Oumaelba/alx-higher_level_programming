#!/usr/bin/python3
"""Defines an print_square function."""


def print_square(size):
    """
    Print a square made up of '#' characters.

    Args:
        size (int): The size of the square. Must be a non-negative integer.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than zero.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
