# -*- coding: utf-8 -*-

from cards.hand import Hand

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = Hand()
    
    def showHand(self):
        string = self.name + ': '
        for card in self.hand.cards:
            string += card + ' '
        string += 'with value ' + str(self.hand.value)
        print string
    
   
    