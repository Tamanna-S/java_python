#small pizza =50
#medium pizza = 100
#large puz#za = 150

#peproni on small = 5
# peproni on medium and large = 10

#cheeze on all = 5

print("A warm welcome to the online PIZZA HUT...!!!")
print("\nRates are as follows:")
print("\n\nSmall pizza = Rs.50\nMedium pizza = Rs.100\nLarge puz#za = Rs.150")
print("\n\npeproni on Small = Rs.5\npeproni on Medium and Large = Rs.10")
print("\n\ncheeze on all = Rs.5")

size = input("enter the size of pizza u want..?'S' , 'M' ,'L' -->  ")
peproni = input("\ndo u want to add peproni..? 'Y' or 'N' --> ")
cheeze = input("\ndo u want extra cheeze..? 'Y' or 'N' --> ")

print("\n-----------------------------------------------------------------------------------------------------------\n\n")

bill = 0

if size == "S":
    bill += 50
elif size == "M":
    bill += 100
elif size == "L":
    bill += 150

if peproni == "Y":
    if size == "S":
        bill += 5
    else:
        bill += 10

if cheeze == "Y":
    bill += 5

print(f"your final bill is Rs.{bill}")

# else:
#     print("please enter a valid input ..!!")