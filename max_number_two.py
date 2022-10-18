def max_number(num1 , num2):
    max = 0 
    if num1 > num2:
        max = num1
    elif num1 == num2:
        max = (f"{num1} and {num2} and both are equal")
    else:
        max = num2
    return (f"The greater number between {num1} and {num2} is {max}")
num1 = eval(input("Enter the first number :\n"))
num2 = eval(input("Enter the second number :\n"))
print(max_number(num1,num2))