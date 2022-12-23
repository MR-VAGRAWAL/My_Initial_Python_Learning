ls = [[1,2,3],[4,5,6],[7,8,9]]
def my_matrix(ls1):
    n = len(ls1[0])
    for i in ls1:
        if len(i) != n:
            return False
    return True  
if my_matrix(ls):
    for i in ls:
        print(*i,sep = "\t")
else:
    print("Invalid Matrix")
