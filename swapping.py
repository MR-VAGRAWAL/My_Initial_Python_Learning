def swapping(num1,num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    return (f"First number after swapping {num1} and second number after swapping {num2}")
num1 = int(input("Enter the first number : \n"))
num2 = int(input("Enter the second number : \n"))
print(swapping(num1,num2))