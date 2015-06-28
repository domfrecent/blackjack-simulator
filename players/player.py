# -*- coding: utf-8 -*-

from cards.hand import Hand

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = Hand()
    
    
    
    