def dimension(arr):
    n = len(arr[0])
    for element in ls:
        if len(element) != n:
            return "Invalid Matrix"
    return len(arr) , len(arr[0])
    
ls = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
for i in ls:
    print(*i , sep="\t")
print(dimension(ls))