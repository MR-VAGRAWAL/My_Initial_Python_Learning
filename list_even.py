l1 = list(map(int,input().split()))
final_list = []
for element in l1:
    if element % 2 == 0:
        final_list.append(element)
print(final_list)