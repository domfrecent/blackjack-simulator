# -*- coding: utf-8 -*-

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

        
