import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''  
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("HEY..!!\n")
print("Welcome to stone paper and scissors Game...!!")

user_choice =  int (input("if u wanna play with me !\nchoose '0' for rock\nchoose '1' for paper\nand choose '2' for scissors..!\n\n:"))

game_ascii = [rock , paper , scissors]

if user_choice < 0 or user_choice > 2:
        print("You cheat with me, YOU LOOSE !")

else:
    print("\nYour Choice :")
    print(game_ascii[user_choice])

    pc_choice = random.randint(0,2)

    print("\nMy Choice")
    print(game_ascii[pc_choice])

    if user_choice == 0 and pc_choice == 2:
        print("You WIN..!!")

    elif pc_choice == 0 and user_choice == 2:
        print("You Loose..!!")

    elif user_choice > pc_choice:
        print("You Win..!!")

    elif pc_choice > user_choice:
        print("You Loose..!!")

    elif pc_choice == user_choice:
        print("Oh! it's a DRAW..!!")


    





