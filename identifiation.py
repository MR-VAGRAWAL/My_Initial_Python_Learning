# Write a python program to count number of vowels , constants , digits , special characters , upper case alphabets , lower case alphabets , spaces and words in the given string:
str = input("Enter the string :\n")
vowel = "AEIOUaeiou"
count_vowel = 0
upper_case = 0
lower_case = 0
count_digit = 0
count_alphabets = 0
count_spaces = 0
special_characters = 0
for i in str:
    if i in vowel:
        count_vowel += 1
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        if ord(i)>=65 and ord(i)<=90:
            upper_case += 1
        else:
            lower_case += 1
        count_alphabets += 1 
    elif ord(i)>=48 and ord(i)<=57:
        count_digit += 1
    elif i == " ":
        count_spaces += 1
    else:
        special_characters += 1
print("Total number of vowels : ",count_vowel)
print("Total number of upper case aphabets : ",upper_case)
print("Total number of lower case alphabets : ",lower_case)
print("Total number of alphabets : ",count_alphabets)
print("Total number of digits : ",count_digit)
print("Total number of spaces : ",count_spaces)
print("Total number of special characters : ",special_characters)