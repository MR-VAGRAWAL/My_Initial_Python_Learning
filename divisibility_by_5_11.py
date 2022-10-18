def divisibility(num):
    if (num % 5 == 0 )and (num % 11 == 0):
        print(f"{num} is divisible by 5 and 11 both")
    elif num % 5 == 0:
        print(f"{num} is divisible by 5")
    elif num % 11 == 0:
        print(f"{num} is divisible by 11")
    else :
        print(f"{num} is neither divisible by 5 nor 11 ")
    return("Good Luck 😊😎🤓")
num = int(input("Enter the number : \n"))
print(divisibility(num))