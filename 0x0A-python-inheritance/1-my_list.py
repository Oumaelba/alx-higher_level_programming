#!/usr/bin/python3
"""class MyList that inherits from list
"""


class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """prints the list, but sorted
        (ascending sort)
        """
        n = len(self)
        for i in range(n-1):
            for j in range(n-i-1):
                if self[j] > self[j+1]:
                    self[j], self[j+1] = self[j+1], self[j]
        for element in self:
            print(element)
