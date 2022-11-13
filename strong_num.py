num = int(input("Enter The Number : "))
number = num
sum = 0
while num!=0:
    factorial = 1
    digit = num % 10
    for i in range(1,digit+1):
        factorial *= i
    sum += factorial
    num //= 10
print(sum)
if sum == number:
    print(f"{number} is a strong number")
else:
    print(f"{number} is not a strong number")