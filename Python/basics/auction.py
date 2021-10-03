import os 
from time import process_time, sleep
bids = {}
finish = False

def finder_highest (bids):
    highest = 0
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print("\n--------------------------------------------------------------------------------\n")
    print(f"the winner of this auction is {winner} by giving Rs.{highest}")



def screen_clear():
    _ = os.system('cls')

from auction_art import logo

print(logo)

while not finish:
    name = input ("\nwhat is your name ? : ")
    bid = int (input ("\nhow many bids u wanna give ? : Rs."))

    bids[name] = bid
    restart = input("\ndeos any bidder left ? type 'yes' or 'no' : ").lower()

    if restart == "no":
        finish = True
        finder_highest(bids)
        
    elif restart == "yes":
        screen_clear()
        
    else:
        print("\nplease, enter a valid input.")




