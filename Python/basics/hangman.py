import random
from hangman_word import word_list

choose_word = random.choice(word_list)
word_length = len(choose_word)

lives = 6
from hangman_art import stages,logo
print(logo)

print("\nHEY..!!\nWelcome to the game...\nwe have a word for u, guess a letter and if it's present in that word we will fix that there and u have to complete the word. \nif u mitakes 6 times than u will loose the game and a life too..!! \nso, be carefull and start the game....")
display = []

for _ in range(word_length):
    display += "_"

end_of_game = False
print(f"\n{' '.join(display)}\n\nyou have to guess these {word_length} letters to win the game...")

while end_of_game == False:
    print("\n----------------------------------------------------------------------------------------\n")
    
    guess = input("guess a letter : ").lower()

    if guess in display:
        print(f"you have already guessed {guess}.")



    for position in range(word_length):
        letter = choose_word[position]
        if letter == guess:
            display[position] = letter
            print(f"you save a life.\nyou have {lives} more chance now..")

    
    print(f"\n{' '.join(display)}\n\n")

    if "_" not in display:
        end_of_game = True
        print("\nyou win.")

    if guess not in display:
        print(f"{guess} is not present in the word, you lost a life...\nnow u have only {lives-1} chance")
        lives -= 1
        print(stages[lives])

        if lives == 2:
            print("you're about to loose..")
            print(f"hint for u '{random.choice(choose_word)}'")


        elif lives == 0:
            print("\nyou loose ")
            print(f"\nhehe!!  the word is : '{choose_word}', give it a go again... ")
            end_of_game = True
    
    
    





