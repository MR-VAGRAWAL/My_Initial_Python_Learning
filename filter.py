def prime(num):
    count = 0
    for i in range(1,num+1):
        if num == 1:
            return ("Not Defined")
        elif num % i == 0:
            count += 1
    if count == 2:
        return "Prime"
    else:
        return "Not Prime"
list1 = [25,23,4,5,6,88,55]
out = filter(prime , list1)
print(out)