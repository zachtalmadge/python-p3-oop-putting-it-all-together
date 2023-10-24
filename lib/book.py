#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count  # set the internal attribute directly to avoid the setter

    @property
    def page_count(self):
        """The page_count property"""
        return self._page_count
        
    @page_count.setter
    def page_count(self, page_count):
        """page count must be an integer"""
        if not isinstance(page_count, int):
            print('page_count must be an integer')
        else:
            self._page_count = page_count
            
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")