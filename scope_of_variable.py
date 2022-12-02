# scope of the variable
'''
1. local
2. nonlocal
3. global
'''
# def add():
#     num = 10  # local variable
#     print(num)
# num = 12  # gloabl variable 
# add()
# print(num)
##################
# def add():
#     global a
#     a = 23


# # global Scope
# a = 10  # global variable 
# add()
# print(a)
def add():
    print(a)
    a = 0
a = 17
add()
print(a)