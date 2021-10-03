#easy method :

import random


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['1','2','3','4','5','6','7','8','9','0']

symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','<','>','?','~','`','[',']','{','}','|']

print("HEY..!!\n")
print("Welcome to PASSWORD generator..\n")

alpha_no = int (input("how many alphabets u want in your password : "))

num_no = int (input("how many numbers u want in your password : "))

sym_no = int (input("how many symbols u want in your password : "))

# easy method :

password = ""           #an empty string -password

for alpha in range (alpha_no):
    password += random.choice(alphabets)        # password ke andr add ho jaye alphabets main se random choice or kitni baar ho jitni barr loop ki range h and that is the no of alphabets which is given by user and stored by us in alpha_no and we're passing this in range.

for num in range(num_no):
    password += random.choice(numbers)          # ab password ke andr add ho jaye numbers main se random choice (jisme se random choose krana h vo hum { () } ke andr likhte h) or kitni baar same as above -jitni barr loop ki range h and that is the no of  numbers which is given by user and stored by us in num_no and we're passing this in range.

for sym in range (sym_no):
    password += random.choice(symbols)      # ab password ke andr add ho jaye symbols main se random choice (jisme se random choose krana h vo hum { () } ke andr likhte h) or kitni baar same as above -jitni barr loop ki range h and that is the no of  symbols which is given by user and stored by us in sym_no and we're passing this in range.

print(f"\n\nyour password is : {password}")    #and f string se print kra diya password ko katam..



# tough method :

# import random


# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# numbers = ['1','2','3','4','5','6','7','8','9','0']

# symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','<','>','?']

# print("HEY..!!\n")
# print("Welcome to PASSWORD generator..\n")

# alpha_no = int (input("how many alphabets u want in your password : "))

# num_no = int (input("how many numbers u want in your password : "))

# sym_no = int (input("how many symbols u want in your password : "))

# #thoda tough method :

# password_list = []     #isme ek empty array ya list -password_list

# for alpha in range (alpha_no):
#     password_list += random.choice(alphabets)     # password_list ke andr add ho jaye alphabets main se random choice or kitni baar ho jitni barr loop ki range h and that is the no of alphabets which is given by user and stored by us in alpha_no and we're passing this in range.

# for num in range (num_no):
#     password_list += random.choice(numbers)       # ab password_list ke andr add ho jaye numbers main se random choice (jisme se random choose krana h vo hum { () } ke andr likhte h) or kitni baar same as above -jitni barr loop ki range h and that is the no of  numbers which is given by user and stored by us in num_no and we're passing this in range.

# for sym in range (sym_no):
#     password_list += random.choice(symbols)      # ab password_list ke andr add ho jaye symbols main se random choice (jisme se random choose krana h vo hum { () } ke andr likhte h) or kitni baar same as above -jitni barr loop ki range h and that is the no of  symbols which is given by user and stored by us in sym_no and we're passing this in range.


# password = ""    #fir ek empty string bnayi password

# random.shuffle(password_list)      #fir randomly shuffle kr diya password_list ko

# for char in password_list:        #fir suffle wali password_list main se ek ek krke add kra diye password main or ab koi range nhi di h mtlb ab ye 0 index se -1 means last index tk chlega
#     password += char

# print(f"your password is : {password}")       #fir use f string se print kra diya khatam..
