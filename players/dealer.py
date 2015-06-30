# -*- coding: utf-8 -*-

from cards.hand import Hand

class Dealer:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def showHand(self):
        string = self.name + ': '
        for card in self.hand.cards:
            string += card + ' '
        string += 'with value ' + str(self.hand.value)
        print string
    
    def getUpCard(self):
        return Hand.cardValue[self.hand.cards[1]]