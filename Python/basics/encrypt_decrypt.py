alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def converter (user_text, shift_no, user_direction):
    resulting_text = ""

    if user_direction == "decode":
        shift_no *= -1

    for char in user_text:

        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_no
            resulting_text += alphabet[new_position]

        else:
            resulting_text += char

    print(f"\n\nhere is your {user_direction}d code : '{resulting_text}' .")

kill_this_task = False

from e_d_art import logo

print(logo)

while not kill_this_task:

    direction = input("\ntype 'encode' if u wanna encrypt a code and type 'decode' if u wanna decrypt a code : ")
    text = input ("\nenter the text : ")
    shift = int (input ("\nenter the number of shifts u want : "))

    if shift >26:
        shift %= 26     #shift = shift % 26

    converter(text, shift, direction)

    again = input ("\nU wanna run it again 'yes' or 'no' : ").lower()

    print("\n\n-------------------------------------------------------------------------------------------------------\n")

    if again == "yes":
        print("ohk..")
        

    elif again == "no":
        kill_this_task = True
        print("ohk, see u again..")

    else:
        kill_this_task = True
        print("\nplease enter a valid input.")



