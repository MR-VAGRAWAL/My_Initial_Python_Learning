def even_odd(num):
    if num == 0:
        print(f"{num} is zero😒")
    elif num % 2 == 0:
        print(f"{num} is an even number😎")
    else:
        print(f"{num} is an odd number🤓")
    return ("Have , A Nice Day😀")
num = int(input("Enter the number : \n"))
print(even_odd(num))
