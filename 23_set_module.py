# Changing the elements of empty set. 
empty_set = set()
print(type(empty_set))
# To add values to an empty set .
empty_set.add(25)
empty_set.add(3)
empty_set.add(99)
empty_set.add(100)
empty_set.add((100,99,100))     # We can add tuple in our set.
empty_set.add(100)    # It does add up to the value to the set because it is repeatative.
empty_set.add(100)    # It does add up to the value to the set because it is repeatative.
# Adding a value repeatedly does not changes a set. 
print(empty_set)
# We can not add dictionary or list to sets because ther are mutable .
print(len(empty_set))   #--> Prints the length of the set.

empty_set.remove(3)     #--> Remove 3 from the set.
# empty_set.emove(17)     #--> Throwa error while trying to remove an element which is not present in the set.
print(empty_set)
print(empty_set.pop())    #--> Removes a random arbitary elements from the set and returns the elements removed.
print(empty_set)
empty_set.clear()
print(empty_set)
empty_set.add(27)
print(empty_set)