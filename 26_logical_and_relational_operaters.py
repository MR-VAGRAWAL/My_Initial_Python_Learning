age = int(input("Enter your age : "))
if (age>=18 and age<=24):
    print("Congratulations , you are eligible")
if (age<18 or age>24):
    print(not True)
# in opperator in python. 
a = None   
if (a is None):
    print("YES")
else:
    print("NO")

b = [15 , 29 , 100]
print(100 in b)