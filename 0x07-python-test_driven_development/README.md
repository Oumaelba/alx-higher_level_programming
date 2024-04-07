# Python Test Driven Development

This directory contains Python scripts and test files for implementing and testing various functions using Test Driven Development (TDD) methodology.

## Files:

### 0-add_integer.py
This script contains a function named `add_integer`. It takes two integers or floats as input and returns their sum as an integer. The script also includes doctests to verify the correctness of the function.

### 2-matrix_divided.py
This script contains a function named `matrix_divided`. It takes a matrix (list of lists) and a divisor as input and returns a new matrix with all elements divided by the divisor. The script also includes doctests to verify the correctness of the function.

### 3-say_my_name.py
This script contains a function named `say_my_name`. It takes two strings as input (first name and last name) and prints a greeting message with the provided names.

### 4-print_square.py
This script contains a function named `print_square`. It takes an integer `size` as input and prints a square using the `#` character. The size of the square is determined by the value of `size`.

### 5-text_indentation.py
This script contains a function named `text_indentation`. It takes a string as input and prints the string with additional indentation after certain characters (`.`, `?`, `:`). The script ensures proper indentation for readability.

### 100-matrix_mul.py
This script contains a function named `matrix_mul`. It takes two matrices (lists of lists) as input and returns the result of multiplying the matrices. The script includes doctests to verify the correctness of the function.

### 101-lazy_matrix_mul.py
This script contains a function named `lazy_matrix_mul`. It takes two matrices (lists of lists) as input and returns the result of multiplying the matrices using NumPy. This implementation is optimized for large matrices.

### 102-python.c
This file contains a simple Python extension module implemented in C. It demonstrates how to write Python modules in C for performance-critical tasks.

## Tests:

The 'tests' directory contains test files for each script:

- **0-add_integer.txt:** Test cases for the `add_integer` function.
- **2-matrix_divided.txt:** Test cases for the `matrix_divided` function.
- **3-say_my_name.txt:** Test cases for the `say_my_name` function.
- **4-print_square.txt:** Test cases for the `print_square` function.
- **5-text_indentation.txt:** Test cases for the `text_indentation` function.
- **6-max_integer_test.py:** Test cases for the `max_integer` function.
