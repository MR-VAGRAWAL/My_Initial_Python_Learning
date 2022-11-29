str = input("Enter The String : ").upper()
for i in range(65,91):
    char = chr(i)
    if char not in str:
        print("The Given String Is Not Panagram")
        break
else:
    print("The Given String Is Panagram")