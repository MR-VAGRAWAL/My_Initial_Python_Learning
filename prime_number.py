num = int(input("Enter The Number : "))
for i in range(2,num):
    if num % i == 0:
        break
else:
    print(f"{num} is a prime number")