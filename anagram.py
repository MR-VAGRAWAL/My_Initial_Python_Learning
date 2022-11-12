str1 = input("Enter the First word: \n")
str2 = input("Enter the Second word: \n")
if sorted(str1) == sorted(str2):
    print(f"{str1} and {str2} are anagram")
else:
    print(f"{str1} and {str2} are not anagram")
