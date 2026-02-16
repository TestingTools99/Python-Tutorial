name=input("Please enter your name:")
if name== 'Prem':
    print("Good morning Prem")
print("Hello, How are you?")

print("==============If-elif-else======================")
brand = input("Enter Your Favourite Brand:")
if brand == 'RC':
    print("It is children's brand")
elif brand == 'KF':
    print("It is not that much kick")
elif brand == "FO":
    print("Buy one get Free One")
else:
    print("Other Brands are not recommended")

print("=============Find Biggest of given 2 Numbers from the command prompt=====================")
n1 = int(input("Enter First number:"))
n2 = int(input("Enter Second number:"))
if n1 > n2:
    print("Greatest number is:", n1)
else:
    print("Greatest number is:", n2)

print("=============Find Biggest of given 3 Numbers from the command prompt=====================")
n1 = int(input("Enter First number:"))
n2 = int(input("Enter Second number:"))
n3 = int(input("Enter Third number:"))
if n1 > n2 and n1 > n3:
    print("Greatest number is:", n1)
elif n2 > n3:
    print("Greatest number is:", n2)
else :
    print("Greatest number is:", n3)

print("============= Program to Check whether the given Number is in between 1 and 100? =====================")
number = int(input("Enter a Number:"))
if 1<=number <= 100:
    print("Number is in between 1 and 100")
else:
    print("Number is not in between 1 and 100")

print("=======Program to take a Single Digit Number from the KeyBoard and Print is Value in English Word?======")
n = int(input("Enter a digit from 0 to 9: "))

if n == 0:
    print("ZERO")
elif n == 1:
    print("ONE")
elif n == 2:
    print("TWO")
elif n == 3:
    print("THREE")
elif n == 4:
    print("FOUR")
elif n == 5:
    print("FIVE")
elif n == 6:
    print("SIX")
elif n == 7:
    print("SEVEN")
elif n == 8:
    print("EIGHT")
elif n == 9:
    print("NINE")
else:
    print("PLEASE ENTER A DIGIT FROM 0 TO 9")