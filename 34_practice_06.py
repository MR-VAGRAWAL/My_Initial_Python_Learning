# Ques1: Write a porogramme to print mutiplication table of a given number using for loop.
from curses import use_default_colors


num = int(input("Enter the number which table you want :\n ")) 
for i in range(1,11):
    # print(num," * ",i," = ",num*i)
                # OR
    print(f"{num} X {i} = {num*i}")   # f string.

# Ques2: Write a programme to greet all the person names stored in a list l1 and which starts with S:
# l1 = ["Vaibhav" , "Aditya" , "Saurabh" , "Pragyat"]
l1 = ["Vaibhav" , "Aditya" , "Saurabh" , "Shashwat"]
for name in l1:
    if name.startswith("S"):
        print("Hello " + name)

# Ques3: Attempt Ques1 using while loop. 
num2 = int(input("Enter the number which table you want :\n "))
x = 1
while x<11:
    print(f"{num2} X {x} = {num2*x}")
    x=x+1

# Ques4: Write a programme to find wheather a given number is prime or not. 
num3 = int(input("Enter a number :\n"))
prime = True
for i in range(2,num3):
    if num3 % i == 0:
        prime = False
        break
if prime :
    print("This is a prime number")
else:
    print("This is not a prime number")

# Ques5: Write a programme to find the sum of first n natural numbers using for loop. 
count = int(input("Enter the total number of natural numbers whose sum you want : ")) 
sum = 0
for i in range(1,count+1):
    sum = sum + i
    i = i + 1
print(f"Sum of first {count} natural number is {sum}")

# Ques6: Write a programme to calculate the factorial of a given number using for loop. 
num4 = int(input("Enter the number to get the factorial :\n"))
factorial = 1
for i in range(1,num4+1):
    factorial = factorial * i
print(f"Factorial of {num4} is {factorial}")

# Ques7: Write a programme to print the following star pattern:
#         *
#         **
#         ***       for n = input form the user
n2 = int(input("Enter the number :"))
for i in range(n2+1):
    print("*" * i)

# Ques8: Write a programme to print multiplication table of n using for loop in reversed order. 
num5 = int(input("Enter the number : "))
for i in range(10,0,-1):
    print(f"{num5} * {i} = {num5 * i}")

# Ques9: Write a programme to print the following star pattern:
#         ***
#         **
#         *       for n = input form the user
num6 = int(input("Enter the number :"))
for i in range(num6,0,-1):
    print("*" * i)