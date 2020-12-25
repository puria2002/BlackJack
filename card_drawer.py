import numpy as np
import pandas as pd
import random


# Reset the deck
def reset():
    cards = []
    for i in range(4):
        cards.append([i+1 for i in range(13)])
    return cards

# Shuffle the deck
def deck_shuffle():
    return random.shuffle(reset())

# Draw a card
def draw_card(cards):
    return cards.pop(0), cards

# Start game
def start():
    cards = deck_shuffle()
    player = []
    house = []
    player_card, cards = draw_card(cards)
    player.append(player_card)
    house_card, cards = draw_card(cards)
    house.append(house_card)
    return player, house, cards

# Settle round
def settle(player, house, cards):
    


