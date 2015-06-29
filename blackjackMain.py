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
        self.players.append( Dealer('Crack Ass Dealer') )
        self.deck = Deck(numDecks)
        
    def addPlayer(self,player):
        self.players.append(player)
        
    def showAllHands(self):
        for player in self.players:
            player.showHand()
        print '\n'
    
    def clearTable(self):
        for player in self.players:
            player.hand.clearHand()
    
    def checkCardsRemaining(self):
        if len(self.deck.cards) <= 2 *  len(self.players):
            self.deck.newDeck()
            print "Replacing deck with new deck\n"
    
     def checkHit(self, player):
        if player.hand.value < 9:
            self.deck.dealCard()
        
# Start game with number of decks as parameter
game = Game(4)

dom = Player('Dom', 1000)
stad = Player('Jordan', 5)

game.addPlayer(dom)
game.addPlayer(stad)

numHands = 0

game.deck.showDeck()

# One iteration of the while loop for each hand of blackjack played
while numHands < 10:
    game.deck.dealHand(game.players)
    
    # During each hand, iterate through players to check if they will hit or stay
    for i in range(1, len(game.players)):
        
        # game.players[i].checkHit()
    
    # dealer hits on 16 and lower
    while game.players[0].hand.value < 17:
        game.deck.dealCard(game.players[0])
    
    # Check for busts and payout
        
    game.showAllHands()
    
    game.checkCardsRemaining()
    numHands+=1
    game.clearTable()

    
