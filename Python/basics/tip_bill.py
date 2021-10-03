print("welcome to tip calculator!!")

bill = float( input("enter the bill: Rs.") )
tip = int ( input("how much tip do u wanna give: 10 / 20 / 30 / 40 or 50..?  "))
people = int ( input("how many people want to tip : "))

amount = tip / 100 * bill + bill
amount2 = amount // people     # ab ye return krega int agr / ek baar hi lgati to float value deta

#final = round(amount2)     isse kya hota ki final ke andr amount2 main agr bhot bda floating point hota to use km likhna jse agr (7.66666666666666666666) hota to ye krke 7 de deta or agr main likhti     {   final = round (amount2 ,2)   } to ab ye (7.66) return krta

print(f"each {people} people should pay : Rs.{amount2}")

