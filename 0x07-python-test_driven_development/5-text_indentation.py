#!/usr/bin/python3
"""Defines an text_indentation function."""


def text_indentation(text):
    """
    Print the given text with indentation.

    The function prints the characters of
    the text one by one. If a period ('.'),
    question mark ('?'), or colon (':') is
    encountered, a newline character
    is printed to create indentation.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If the text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    is_newline = False
    for c in text:
        is_newline = False
        print(c, end='')
        if c in ".?:":
            print("\n")
            is_newline = True
    if not is_newline:
        print()
