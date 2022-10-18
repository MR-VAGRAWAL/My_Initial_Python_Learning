def check(num):
    if num > 0:
        print(f"{num} is a positive number")
    elif num < 0:
        print(f"{num} is a negative number")
    else:
        print(f"{num} is zero")
    return ("Have , A Good Day 😎")
num = eval(input("Enter the Number : \n"))
print(check(num))