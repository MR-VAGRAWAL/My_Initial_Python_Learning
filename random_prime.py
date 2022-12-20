import random 
def prime(user):
    count = 0
    for i in range(1,user+1):
        if user % i == 0:
            count += 1
    if count == 2:
        return True
# user = int(input())
count = 0
# n = int(input("Enter The Number Of Prime Numbers You Want : "))
# digit = int(input("Enter The Number Of Digit You Want : "))
while count<5:
    num = random.randint(1000,9999)
    if prime(num) == True:
        print(num)
        count += 1
