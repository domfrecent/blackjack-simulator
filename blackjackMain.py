# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:32:43 2015

@author: dom
"""
from player import Player
from dealer import Dealer
from deck import Deck

class Game:
    def __init__(self):
        self.players = []
        self.deck = Deck()
        
    def addPlayer(self,player):
        self.players.append(player)
        
    def showAllHands(self):
        for player in self.players:
            player.hand.showHand()
    
    def clearTable(self):
        for player in self.players:
            player.hand.clearHand()
    
    def checkDeck(self):
        if len(self.deck.cards) <= 2 *  len(self.players):
            self.deck.newDeck()
        

# Start game
game = Game()

dom = Player('Dom', 1000)
stad = Player('Jordan', 5)
dealer = Dealer('Crack Ass Dealer', 10000)

game.addPlayer(dom)
game.addPlayer(dealer)
game.addPlayer(stad)

numHands = 0

while numHands < 1000:
    game.deck.dealHand(game.players)
    game.showAllHands()
    
    game.clearAllHands()


