import numpy.random

# Global Constants
BUST = 1
WIN = 0
UNDETERMINED = -1
TARGET = 21


#a simple class for game cards.
#Suits are denoted by an integer 1-4 (corresponding to some permutation of heart, diamond, club, spade)
#Ace corresponds to 1, King to 13
class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

#a simple card deck which can deal random cards
class Deck:
    def __init__(self):
        self.deck = []
        for i in range(1,5):
            for j in range(1,14):
                self.deck.append(Card(i,j))
    #chooses a random card from the deck, removes it, and returns it
    def dealCard(self):
        dealtIndex = numpy.random.randint(0,len(self.deck))
        return self.deck.pop(dealtIndex)

#hand of a given player
class Hand:
    def __init__(self):
        self.hand = []
    #adds a card to a hand
    def addCard(self, card):
        self.hand.append(card)
        
    #given knowledge of cards in hand, calculates probability of the next card dealt being the target card 
    def probabilityOf(self, targetCard):
        #check if card is in hand
        for card in self.hand:
            if (card.suit == targetCard.suit and card.number == targetCard.number):
                return 0
        #otherwise card is equally likely to be anything remaining
        return 1/(52 - len(self.hand))

    # Sum of the cards in hand
    def sum(self):
        total = 0
        for card in self.hand:
            total += card.number
        return total

# Start game
def start():
    # Initialize the three parties
    deck = Deck()
    player = Hand()
    house = Hand()

    # Deal a card to each player in the game
    player.addCard(deck.dealCard())
    house.addCard(deck.dealCard())

    return player, house, deck


# Settle round and determine busts, etc.
def settle(player, deck):
    global BUST
    global WIN
    global UNDETERMINED
    global TARGET

    # Determine whether the player has busted or won
    if player.sum > TARGET:
        return BUST
    if player.sum == TARGET:
        return WIN
    return UNDETERMINED


