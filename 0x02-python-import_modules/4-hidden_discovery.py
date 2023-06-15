#!/usr/bin/python3
import importlib

if __name__ == "__main__":
    module_name = "hidden_4"
    hidden_4 = importlib.import_module(module_name)

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
