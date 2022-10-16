def table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")
    return ("Have , A Good Day😎")
num = int(input("Enter the number :\n"))
print(table(num))