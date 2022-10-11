#   Ques_1 => Write a Python programme to add two numbers.
a=int(input("Enter your first Number "))
b=int(input("Enter your second Number "))
print("The sum of two numbers you entered is ",a+b)

#  Ques_2 => Write a python programme to find remainders whenn a number is divided by 2
num1 = int(input("Enter your number "))
num2 = 2
print("The remainder when the entered number is divided by 2 is ",a%2)
 
#  Ques_3 => Check the type of the variable assigned using input() function .
fun1= input("Enter the function to know the type ")
print(type(fun1))  #It always print 'str' because the output of input function is always a string.

#  Ques_4 => Use comparison operater to find out whether a given variable "a" is greater than "b" or not
a=int(input("Enter your first number"))
b=int(input("Enter your second number"))
if a>b:
    print(a,"is greater than ",b)
elif b>a:
    print(b,"is greater then ",a)
else:
    print("Both are equal") 

#  Ques_5 => Write a python programme to find average of two numbers enterd by the user.   
num3 = int(input("Enter the first number ")) 
num4 = int(input("Enter the second number ")) 
print("The average of the entered number is ",(num3+num4)/2)        

#  Ques_6 => Write a python programme to calculate square of a number entered by the user
num5 = int(input("Enter the number whose square you want : "))
print("The square of the number entered is",num5**2)