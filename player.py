# -*- coding: utf-8 -*-

from hand import Hand

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = Hand()
    
    
    
    