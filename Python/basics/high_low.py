import random

def compare(guess, a ,b):
    if a["age"]>b["age"]:
        if guess == "a":
            return True
        else: 
            return False
    else:
        if guess == "b":
            return True
        else:
            return False

from hl_list import data

game_over= False

a = random.choice(data)
b = random.choice(data)
from hl_art import hl, vs
score = 0

while not game_over:
    print(hl)
    while a == b:
        b = random.choice(data)
    print(f"option A: {a['name']}")
    print(vs)
    print(f"option B: {b['name']}")

    guess = input("whoose age is greater? type 'A' or 'B' : ").lower()
    result = compare(guess, a, b)
    if result == True:

        import os
        from time import process_time, sleep

        def clear():
            _ = os.system('cls')

        score += 1
        clear()
        print(f"you're right!, keep going.. \ncurrent score : {score}")

        a=b
    else:
        print(f"you're wrong!, give it a go again..\nfinal score : {score}")
        game_over = True





