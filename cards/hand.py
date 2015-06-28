# -*- coding: utf-8 -*-

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
    
    def receiveCard(self,card):
        self.cards.append(card)
        self.updateHandVal(card)
    
    def updateHandVal(self, card):
        self.value += Hand.value[card]
        
    def clearHand(self):
        self.cards = []
        self.value = 0
        
    def showHand(self):
        string = ''
        for card in self.cards:
            string += card + ' '
        string += 'with value ' + str(self.value)
        print string
    
#    def getHandVal(self):
#        tempVal = 0
#        for i in range(len(self.cards)):
#            tempVal += Hand.value[self.cards[i]]
#        return tempVal
#    
        
    value = {'2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 10,
            'Q': 10,
            'K': 10,
            'A': 11}
    