#To Check The Number Given By The User Is Prime Or Not.
num = int(input("Enter The Number Which You Want To Check : \n "))
for i in range(2,num):
    if num == 1 or num == 0:
        print("It is not a prime number")
    elif num % i == 0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")