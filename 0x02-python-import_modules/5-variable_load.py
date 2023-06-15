#!/usr/bin/python3
import importlib

if __name__ == "__main__":
    module_name = "variable_load_5"
    variable_load_5 = importlib.import_module(module_name)

    print(variable_load_5.a)
