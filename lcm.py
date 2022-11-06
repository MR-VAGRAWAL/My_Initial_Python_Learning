# To Find LCM Of Two Numbers:
num1 = int(input("Enter The Number :\n"))
num2 = int(input("Enter The Another Number :\n"))
greatest = 0
if num1 > num2 :
    greatest = num1
else:
    greatest = num2
while True :
    if (greatest % num1 == 0) and (greatest % num2 == 0):
        print(f"The LCM of {num1} and {num2} is {greatest}")
        greatest += 1