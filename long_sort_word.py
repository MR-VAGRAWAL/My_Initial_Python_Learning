str = input()
lst = set(str.split())
# longest = []
# shortest = []
# for word in lst:
#     long = max(lst,key = len) 
#     short = min(lst,key = len)
#     longest.append(long)
#     shortest.append(short)
#     # lst.remove(long)
#     # lst.remove(short)
# print("Longest Word :",longest)
# print("Shortest Word :",shortest)
long = len(max(lst,key=len))
short = len(min(lst,key=len))
print("Longest : ")
for long_word in lst:
    if len(long_word) == long:
        print(long_word)
print("Shortest : ")
for short_word in lst:
    if len(short_word) == short:
        print(short_word)