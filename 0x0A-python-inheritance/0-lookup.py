#!/usr/bin/python3
"""  returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """returns the list of available attributes"""
    all = []

    for item in dir(obj):
        if hasattr(obj, item):
            all.append(item)

    return all
