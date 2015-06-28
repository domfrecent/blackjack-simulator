# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:32:43 2015

@author: dom
"""

from players.player import Player
from players.dealer import Dealer
from cards.deck import Deck

class Game:
    def __init__(self, numDecks):
        self.players = []
        self.deck = Deck(numDecks)
        
    def addPlayer(self,player):
        self.players.append(player)
        
    def showAllHands(self):
        for player in self.players:
            player.hand.showHand()
        print '\n'
    
    def clearTable(self):
        for player in self.players:
            player.hand.clearHand()
    
    def checkDeck(self):
        if len(self.deck.cards) <= 2 *  len(self.players):
            self.deck.newDeck()
            print "Replacing deck with new deck\n"
        
# Start game with number of decks as parameter
game = Game(4)

dom = Player('Dom', 1000)
stad = Player('Jordan', 5)
dealer = Dealer('Crack Ass Dealer')

game.addPlayer(dom)
game.addPlayer(dealer)
game.addPlayer(stad)

numHands = 0

# game.deck.showDeck()

while numHands < 50:
    game.deck.dealHand(game.players)
    game.showAllHands()
    
    game.checkDeck()
    numHands+=1
    game.clearTable()

    


