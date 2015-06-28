# -*- coding: utf-8 -*-

from random import shuffle

class Deck:
    
    # To use more than one deck (as is done in most casinos, ~4 decks) instantiate 
    # multiple decks and add them together
    
    # Initializer for Deck class
    def __init__(self, numDecks):
        self.numDecks = numDecks
        self.newDeck()
        
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
        shuffle(self.cards)
    
    # Creates new, shuffled, stack of cards with the number of decks specified from self.numDecks, shuffles twice
    def newDeck(self):
        self.cards = [card for card in Deck.singleDeck for _ in range(self.numDecks)]
        self.shuffleDeck()
    
    def showDeck(self):
        print self.cards
    
    
    singleDeck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
                  '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
                  '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
                  '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        