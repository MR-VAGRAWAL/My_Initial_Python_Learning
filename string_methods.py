str = "hello world I am a World changer"
print(str.count('a'))               #To count the number of occurence of a char in the string
print(str.capitalize())             #To captilaize the first letter of the string
print(str.title())                  #To capitalize the first letter of each word present in the string
print(str.upper())                  #To capitalise the each letter of the string
print(str.lower())                  #To decapitalize the each letter of the stringprint
print(str.casefold())               #To convert the string in the lower case and ignore the uncovertable part
print(type(str))                    #To find the data type of the variable
print(ord("a"))                     #To convert the caharcter in to ASCII value
print(chr(65))                      #To determine the value assingned to the ASCII number
print(str.center(99,"$"))           
print(str.ljust(100,"@"))
print(str.zfill(99))
print(str.isalpha())
print(str.istitle())
print(str.isalnum())