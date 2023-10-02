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

# Compares scores and return true if computer's one is greater than user's one
def computer_wins_or_draw(user_score,computer_score):
    if user_score > 21:
        return True
    if computer_score >= user_score:
        return True
    
    return False

# Print final state of game
def print_final_hands(player_hand,computer_hand,player_score,computer_score):
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

# Declare a winner for the game
def declare_winner(player_score,computer_score):
    if (player_score > 21):
        print("You went over. You lose 🙁")
    elif (computer_score > 21):
        print("Computer went over. You win 🙂")
    elif (player_score > computer_score):
        print("You win 🙂")
    elif (player_score == computer_score):
        print("Draw 🙃")
    else:
        print("You lose 🙁")

# Declare function to start the game
def blackjack_game():

    # Declare variables
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand = deal_cards(2, cards)
    computer_hand = deal_cards(2, cards)
    player_score = sum(player_hand)
    computer_score = sum(computer_hand)
    wants_another_card = "y"

    # Clear console and display logo
    clear_console()
    print(logo)

    # User game loop
    while wants_another_card == "y":
        # Display player's hand and score
        print(f"Your cards: {player_hand}, current score: {player_score}")

        # Display computer's first card
        print(f"Computer's first card: {computer_hand[0]}")

        # Reset condition to enter the loop
        wants_another_card = ""

        # Ask user if he/she wants another card
        while wants_another_card != "y" and wants_another_card != "n":
            wants_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        # If answer is "y", give another card to the user
        if wants_another_card == "y":
            player_hand += deal_cards(1,cards) # We join the two lists
            player_score = sum(player_hand) # We need to refresh the score
            # If player score is over 21, exit the loop
            if player_score > 21:
                break
    
    # It's computer turn
    # Computer plays while its score is below user's one or its over 21
    while not computer_wins_or_draw(player_score,computer_score) and (computer_score <= 21):
        computer_hand += deal_cards(1,cards) # We join the two lists
        computer_score = sum(computer_hand) # We need to refresh the score


    # When user has played and computer too, it's time to print final hands and declare a winner
    print_final_hands(player_hand, computer_hand, player_score, computer_score)
    declare_winner(player_score, computer_score)

# Display start question to user
answer = ""
while answer != "y" and answer != "n":
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

# If user wants to play, start the game
if answer == "y":
    blackjack_game()