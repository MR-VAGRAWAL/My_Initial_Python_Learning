n = int(input("Enter The Number of Lines you want :"))
for i in range(1,n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(1,i+1):
        if (j==i or j==1):
            print("$ ", end="")
        else:
            print("  ",end="")    
    print()
for i in range(1,n+1):
    if i==1:
        print(" WELCOME ")
    else:
        for j in range(1,i):
            print(" ",end="")
        for j in range(i,n+1):
            if (j==i or j==n):
                print("$ ",end="")
            else:
                print("  ",end="")
        print()