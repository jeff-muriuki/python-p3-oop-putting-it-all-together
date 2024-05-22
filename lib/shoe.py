#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = None
        self._size = None
        self.brand= brand
        self.size= size
    
    @property
    def brand(self):
        return self._brand    
    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self._brand= value
        else:
            print('brand must be a string of characters')    
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, value):
        if type(value) is int:
            self._size= value  
        else:
            print('size must be an integer')      
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"    