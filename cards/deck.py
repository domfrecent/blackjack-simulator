# -*- coding: utf-8 -*-

from random import shuffle

class Deck:
    
    # Initializer for Deck class
    def __init__(self, numDecks):
        self.numDecks = numDecks
        self.newDeck()
        
    # Returns first card from deck
    def dealCard(self, player):
        nextCard = self.cards.pop()
        player.hand.receiveCard(nextCard)
    
    # Maybe put this method in game class, replace with an update deck method
    def dealHand(self, players):
        for i in range(2):
            for player in players:
                self.dealCard(player)
                
    def shuffleDeck(self):
        shuffle(self.cards)
    
    # Creates new, shuffled, stack of cards with the number of decks specified from self.numDecks, shuffles deck twice
    def newDeck(self):
        self.cards = [card for card in Deck.singleDeck for _ in range(self.numDecks)]
        self.shuffleDeck()
        self.shuffleDeck()
    
    def showDeck(self):
        print self.cards
    
    
    singleDeck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
                  '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
                  '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
                  '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        