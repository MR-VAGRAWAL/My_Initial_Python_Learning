def max_number(num1,num2,num3):
    max = 0
    if num1>num2 and num1>num3:
        max = num1
    elif num2>num1 and num2>num3:
        max = num2
    else :
        max = num3
    return (f"The greatest number between {num1} , {num2} and {num3} is {max}")
num1 = eval(input("Enter the first number :\n"))
num2 = eval(input("Enter the second number :\n"))
num3 = eval(input("Enter the third number :\n"))
print(max_number(num1 , num2 , num3))