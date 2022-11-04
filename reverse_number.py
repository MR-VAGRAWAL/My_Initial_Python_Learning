num = int(input("Enter The Number :\n"))
while num!=0:
    reverse_num = num%10
    num//=10
    print(reverse_num , end="")