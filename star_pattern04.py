n = int(input("Enter The Number of Lines you want :"))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(1,i+1):
        print("*", end="")    
    print("\n")