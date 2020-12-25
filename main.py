import cards
import greedy
import players
import notsogreedy

# Constants to determine which method we are using
GREEDY = 0
NOTSOGREEDY = 1

# Allows us to switch between algorithms easily
def algorithm(hand, deck, method):
    if method == GREEDY:
        return greedy.algorithm(house, deck)
    if method == NOTSOGREEDY:
        return notsogreedy.algorithm(house, deck)


# Main method

player, house, deck = cards.start()

timer = -1
while timer < 0:
    # The player always goes first
    player, deck, player_stop = players.algorithm(player, deck)
    player_last_settled = cards.settle(player, deck)
    if player_last_settled >= 0:
        timer = 1

    # The house's turn (greedy AI)
    house, deck, house_stop = algorithm(house, deck, NOTSOGREEDY)
    house_last_settled = cards.settle(house, deck)
    if house_last_settled >= 0:
        timer = 1
    
    # Finish the game if both players stop drawing cards
    if player_stop + house_stop > 1:
        timer = 1

# Print the results of the game
if player_last_settled > 0:
    print("Player Lost")
elif player_last_settled == 0 or house_last_settled > 0:
    print("Player Won")
elif house_last_settled == 0:
    print("Player Lost")
else:
    if player.sum() >= house.sum():
        print("Player Won")
    else:
        print("Player Lost")

    