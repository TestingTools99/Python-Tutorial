print('print characters present in the given string')
s = "Premchand"
for x in s:
    print(x,end=" ")

print("===============print characters present in the given string==============")
s="Yasodhar"
i=0
for x in s:
    print('The character is present at:',i,"index is:",x)
    i=i+1

print("============print Hello 10 times====================")
for i in range(10):
    print("Hello")

print("============print 1 to 10====================")
for i in range(11):
    print(i,end=" ")

print("===========Display odd numbers from 0 to 20 =================")
for i in range(1,21):
    if i%2!=0:
        print(i,end=" ")

print("\n=============display numbers from 10 to 1 in descending order ===========")
for x in range(10,0,-1):
    print(x,end=" ")

print("===============print sum of numbers presenst inside list==============")
list=eval(input("Enter List:"))
sum=0
for x in list:
    sum = sum + x

print('Sum=',sum)

print("\n========================print numbers using while loop====================================")
i=1
while i<=10:
    print(i, end=" ")
    i=i+1

print("\n========================display the sum of first n numbers ====================================")
n = int(input("Enter number:"))
i=1
sum = 0
while i<=n:
   sum = sum + i
   i=i+1

print("Sum=",sum)

print("=========Write a program to prompt user to enter some name until entering Durga==============")
name=''
while name!='Prem':
    name = input('Enter name:')
print("Thank You for confirmation...")


print("==========Print * pattern =====================")
for i in range(1,10):
    for j in range(1,i+1):
        print('*', end=" ")
    print()

print("==========Print * in Pyramid Shape ==================")
n = int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(1, i+1):
        print("x",end="")
    print()


print("==============Using break statement================")
for i in range(1,101):
    if i==51:
        break
    print(i, end=" ")

print("\n==============Using break statement================")
cart = [10,20,600,50,70]
for item in cart:
     if item > 500:
         print("To place this order insurence must be required")
         break
     print(item)


print("\n============Using Continue Statement===============")
numbers = [10,20,30,0,5,30]
for n in numbers:
    if n == 0:
        print("Hey how we can divide with zero..just skipping")
        continue
    print("100/{} = {}".format(n, 100 / n))


print("===========Use Pass Statement===================")
n = 120
if n > 10:
    print("Big number")
else:
    pass

print("============Use del statement================")
numbers = [10, 20, 30, 40]
del numbers[1]
print(numbers)

numbers = [1, 2, 3, 4, 5]
del numbers[1:4]
print(numbers)

s=None
del s
s="prem"
print(s)