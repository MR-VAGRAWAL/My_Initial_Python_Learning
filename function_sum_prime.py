def prime_number(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    else:
        return True
a , b = list(map(int,input().split()))
for num in range(a,b+1):
    if prime_number(num):
        print(num)