#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = None
        self._page_count = None
        self.title= title
        self.page_count= page_count
    
    @property
    def title(self):
        return self._title    
    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self._title= value
        else:
            print('title must be a string of characters')    
    @property
    def page_count(self):
        return self._page_count
    @page_count.setter
    def page_count(self, value):
        if type(value) is int:
            self._page_count= value  
        else:
            print('page_count must be an integer')      

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")    