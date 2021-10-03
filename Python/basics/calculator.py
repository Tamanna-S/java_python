import os
from time import process_time, sleep
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def calculation():
    from calculator_art import logo
    print(logo)
    print("\n---------------------------------------------------------------------------------\n")
    num1 = float (input ("enter the first no : "))

    new_calculation = False

    while not new_calculation:

        operations = {
            "+" : add,
            "-" : subtract,
            "*" : multiply,
            "/" : divide,
        }

        print("\n")
        for symbol in operations:
            print(symbol)

        operation = input ("pick any of the above operation : ")
        if operation not in operations:
            print("please, enter a valid input. ")

        num2 = float(input( "\nenter next no : "))

        answer = operations[operation](num1, num2)

        print(f"the calculation is done : {num1} {operation} {num2} = {answer}")
        

        again = input ("\n\nif u wanna calculate more with the answer type 'yes'.\nif u wanna start a new calculation type 'no'.\nand if u wanna exit type 'exit'. : ").lower()

        if again == "yes":
            num1 = answer

        elif again == "no":
            def clear():
                _ = os.system('cls')
            clear()
            new_calculation = True
            calculation()

        elif again == "exit":
            print("\n---------------------------------------------------------------------------------\n")
            return "ohk..see u again.."

        else:
            print("\n---------------------------------------------------------------------------------\n")
            return "please, enter valid input."


print(calculation())
            





