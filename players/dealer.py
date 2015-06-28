# -*- coding: utf-8 -*-

from cards.hand import Hand

class Dealer:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

