import cards
import greedy
import players
import notsogreedy

# Constants to determine which method we are using
MANUAL = -1
GREEDY = 0
NOTSOGREEDY = 1

# Allows us to switch between algorithms easily
def algorithm(hand, deck, method):
    if method == GREEDY:
        return greedy.algorithm(hand, deck)
    if method == NOTSOGREEDY:
        return notsogreedy.algorithm(hand, deck)


# One iteration of the game
def game(method):
    player, house, deck = cards.start()

    timer = -1
    while timer < 0:
        # The player always goes first
        player, deck, player_stop = players.algorithm(player, deck)
        player_last_settled = cards.settle(player, deck)
        if player_last_settled >= 0:
            timer = 1

        # The house's turn (greedy AI)
        house, deck, house_stop = algorithm(house, deck, method)
        house_last_settled = cards.settle(house, deck)
        if house_last_settled >= 0:
            timer = 1
    
        # Finish the game if both players stop drawing cards
        if player_stop + house_stop > 1:
            timer = 1

    # Print the results of the game
    if player_last_settled > 0:
        print("Player Lost")
        return 0
    elif player_last_settled == 0 or house_last_settled > 0:
        print("Player Won")
        return 1
    elif house_last_settled == 0:
        print("Player Lost")
        return 0
    else:
        if player.sum() >= house.sum():
            print("Player Won")
            return 1
        else:
            print("Player Lost")
            return 0

# Main method to investigate the performance of the player
epoches = 10
wins = 0
for i in range(epoches):
    wins += game(NOTSOGREEDY)
print(wins/epoches)

    