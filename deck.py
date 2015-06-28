# -*- coding: utf-8 -*-

import random

class Deck:
    
    # Initializer for Deck class
    def __init__(self):
        self.cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
                      '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
                      '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
                      '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.shuffleDeck()
    
    # Returns randomly selected card from deck
    def dealCard(self):
        return self.cards.pop()
    
    # Maybe put this method in game class, replace with an update deck method
    def dealHand(self, players):
        for i in range(2):
            for player in players:
                tempCard = self.dealCard()
                player.hand.receiveCard(tempCard)
                
    def shuffleDeck(self):
        random.shuffle(self.cards)
        
        