# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:32:43 2015

@author: dom
"""
from player import Player
from game import Game

dom = Player('Dom', 1000)
stad = Player('Jordan', 5)
dealer = Player('Dealer Jim', 10000)

game = Game()
game.addPlayer(dom)
game.addPlayer(dealer)
game.addPlayer(stad)
game.deck.dealHand(game.players)

game.showAllHands()



