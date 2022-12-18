# Create a multiplication table by taking input from the user.
num = int(input("Enter the number : \n"))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")
