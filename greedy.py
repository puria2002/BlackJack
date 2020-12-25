from cards import *

# The greedy AI that draws until win or bust
def algorithm(hand, deck):
    global TARGET
    if hand.sum() < TARGET:
        hand.addCard(deck.dealCard())
        return hand, deck, 0
    return hand, deck, 1