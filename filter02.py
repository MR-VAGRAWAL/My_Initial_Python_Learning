# str = input()
# def func(str):
#     str = str.upper()
#     new_string = ""
#     for i in str:
#         if 65<=ord(i)<=90:
#             new_string += i
#         else:
#             pass
#     return new_string
# out = filter(func , str)
st = input()
def apna_fun(y):
    return y.isalpha()
out = list(filter(apna_fun,st))