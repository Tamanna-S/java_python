from random import randint

E_TURN = 10
H_TURN = 5

def level():
    level = input ("\nchoose a level -- type 'easy' or 'hard' : ")
    if level == "hard":
        return H_TURN
    elif level == "easy":
        return E_TURN
    else:
        return False
        
def compare(guess, answer, turns):
    if guess > answer:
        print("it's high, guess a low number..")
        return turns - 1        
    elif guess < answer:
        print("it's low, guess a high number..")
        return turns - 1
    else:
        print("\n---------------------------------------------------------------------------------------\n")
        print(f"woop! you got that was {answer}")
        return "finish"

answer = randint(1,100)
def play_game():
    from num_guess_art import logo
    print(logo)
    print("Welcome to Number Guessing Game..")
    print("\nI'm thinking of a number from (1-100) \nyou have to guess it for win this game : ")

    turns = level()
    if turns == False:
        return ("please, enter a valid input. :|")
    else :
        guess = 0
        while guess != answer:

            print(f"\nyou have {turns} attempts to guess the number.\n")
            guess = input("guess a  no : ")

            if not guess.isdigit():
                print("\n---------------------------------------------------------------------------------------\n")
                return ("you have not enter a number, you loose! :|")

            else:
                turns = compare (int(guess), answer, turns)
                if turns == 0:
                    print("\n---------------------------------------------------------------------------------------\n")
                    return (f"your all attempts are finished, you loose! :(\n\nthe number was {answer}, give it a go again..")
                elif turns == "finish":
                    return ":)"
                else:
                    print("\ntry again..\n")

import os
from time import process_time, sleep

def clear():
    _ = os.system("cls")

play = input("\ndo u wanna play Number Guessing Game ..?  type 'y' or 'n' : ")
if play == "y":
    clear()
    print(play_game())
elif play == "n":
    print("see u again")
else:
    print("please, enter a valid input. :|")
            

