# Write a Python function which will print the elements of a given list in different lines (list will be given as argument to the function)
def list_element(list):
    print("Elements Of List Are : ")
    for i in range(0,len(list)):
        print(list[i])
# list = [25 , 33 , 27 , 99 , 100 , 13 , 17]
list = []
num = int(input("Enter The Number Of Elements You Want In The List : "))
for elements in range(num):
    user = eval(input("Enter The Element Of The List : "))
    list.append(user)
print("Your Final List Is :- " , list)
list_element(list)