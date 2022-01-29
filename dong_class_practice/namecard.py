from dataclasses import dataclass
from itertools import count
import os
import file_util
import math
from paging import Paginator


@dataclass
class NameCard:
    name: str
    phone: str
    email: str
    address: str = ''
    
    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        return setattr(self, key, value)
    
class NameCardBook:
    def __init__(self) -> None:
        self.book = []
        
    def get_page(self, page_num, count_per_page=10):
        page_obj = Paginator(self.book, page_num, count_per_page)
        
        return page_obj
    
    def add(self, name, phone, email, address):
        card = NameCard(name, phone, email, address)
        self.book.append(card)
        self.book.sort(key = lambda card: card.name)
        
    def update(self, ix, name, phone, email, address):
        card = self.book[ix]
        card.name = name
        card.phone = phone
        card.email = email
        card.address = address
        
    def remove(self, ix):
        if ix != -1:
            self.book.pop(ix)
    
    def search(self, name):
        result = list(filter(lambda card: name in card.name, self.book))
        return result