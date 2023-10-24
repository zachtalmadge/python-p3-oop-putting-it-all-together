#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        
    @property
    def size(self):
        """Return the size of the Shot"""
        return self._size
    
    @size.setter
    def size(self, size):
        """Size must be an integer"""
        if not isinstance(size, int):
            print('size must be an integer')
            
        else:
            self._size = size
            
    def cobble(self):
        print('Your shoe is as good as new!')
        self.condition = "New"