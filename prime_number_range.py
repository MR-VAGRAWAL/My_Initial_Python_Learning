# Write a python program to print all prime numbers between given range 
start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
for i in range(start,end+1):
    for j in range(2,i):
        if i==0:
            print(f"{i} is not a prime number")
        elif i % j == 0:
            print(f"{i} is not a prime number")
        
    else:
        print(i)