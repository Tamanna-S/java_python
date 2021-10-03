from math import gamma
import random
def cards ():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def score_sum(cards):
    if sum(cards) == 21 and  len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, pc_score):
    if user_score==pc_score:
        return ("it's a draw")
    elif user_score == 0 :
        return("woop! you win with a blackjack")
    elif pc_score== 0:
        return ("you loose, opponent win with a blackjack")
    elif user_score >21:
        return ("oops! your score are overflowing..")
    elif pc_score>21:
        return ("you win, opponent's score are overflowing..")    
    elif user_score>pc_score:
        return("you win..")
    else:
        return ("you loose")

def play_game():

    user_card= []
    pc_card = []
    game_over = False

    for _ in range (2):
        user_card.append(cards())
        pc_card.append(cards())

    print(f"opponent's card is : {pc_card[0]}")
    pc_score = score_sum(pc_card)

    while not game_over:

        user_score = score_sum(user_card)
        print(f"\nyour cards are : {user_card} and current score is : {user_score}")

        if user_score==0 or pc_score==0 or user_score>21:
            game_over = True
        else:
            user_want_card = input("\ndo u want a card type 'y' or 'n' to pass : ").lower()
            if user_want_card == "y":
                user_card.append(cards())
            elif user_want_card == "n":
                game_over = True
            else:
                game_over=True
                print("\nplease, enter avalid input.")

    while pc_score != 0 and pc_score<16:
        pc_card.append(cards())
        pc_score= score_sum(pc_card)

    print(f"\nopponent's final hand is : {pc_card} and score is : {pc_score}")
    print(f"your final hand is : {user_card} and score is : {user_score}")

    print("\n--------------------------------------------------------------------------------------------------------\n")

    print (compare(user_score , pc_score))

import os
from time import process_time,sleep
def clear():
    _ = os.system('cls')

while input("do u want to play BLACKJACK..? type 'y' or 'n' : ").lower() =="y":
    clear()
    play_game()







