############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

# Import modules
import os
import random
from art import logo

# Clear console function (works on Windows and Linux)
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Declare function to deal cards
def deal_cards(number_of_cards, cards):
    selected_cards = []
    for i in range(number_of_cards):
        selected_cards.append(random.choice(cards))
    
    return selected_cards

# Declare function to start the game
def blackjack_game():

    # Declare variables
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    round = 1

    # Clear console and display logo
    clear_console()
    print(logo)

# Display start question to user
answer = ""
while answer != "y" and answer != "n":
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

# If user wants to play, start the game
if answer == "y":
    blackjack_game()