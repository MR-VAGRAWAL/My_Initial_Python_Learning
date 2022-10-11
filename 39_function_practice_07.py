# Ques1: Wirte a programme using function to find greatest of three numbers.
num1 = int(input("Emter the number 1 : ")) 
num2 = int(input("Emter the number 2 : ")) 
num3 = int(input("Emter the number 3 : ")) 
def greatest(num1 , num2 , num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if num2>num3:
            return num2
        else:
            return num3
greatest_num = greatest(num1 , num2 , num3)
print("The greatest number is " + str(greatest_num))
# Ques2: Write a python programme using function to convert Celsius to Fahrenite.
def fahrenite(celcius):
    return (celcius * 9/5) +32
celcius_temperature = float(input("Enter the temperature in celcius : "))
fahrenite_temperature = fahrenite(celcius_temperature)
print("Fahrenite Temperature is " + str(fahrenite_temperature))
# Ques3: How do you prevent a python print() function to print a new line at the end. 
print("Hello" , end=" ")
print("How" , end=" ")
print("Are" , end=" ")
print("You" , end=" ")
# Ques4: Write a recursive function to calculate the sum of first n natural numbers.
def sum_recursive(count):
    if count==1:
        return 1
    return count + sum_recursive(count-1)
count = int(input("Enter the number : "))
sum_num = sum_recursive(count)
print(f"Sum of first {count} natural numbers is {sum_num}")     
# Ques5: Write a python function to print first n lines of the following pattern:
#     * * *
#     * * 
#     *            for n = user input. 
count_2 = int(input("Enter the number  :"))
for i in range(count_2):
    print("*" * (count_2 - i))
# Ques6: Write a python function which converts inches to cms. 
def centimeters(inches):
    return 2.54 * inches
inches = float(input("Enter the inches which you want to convert in centimeter  :"))
in_centimeter = centimeters(inches)
print(f"{inches} inches is equal to {in_centimeter} centimeters")
# Ques7: Write a python function to remove a given word from a string and strip it at the same time.(Strip function is used to remove unwanted spaces in the string.)
def remove_and_strip(string):
    new_string = string.replace(word,"")
    return new_string.strip()
string = "      My name is Vaibhav      "
print(string)
word = input("Enter the word you want to remove => ")
new_string = remove_and_strip(string)
print(new_string)
# Ques8: Write a python function to print multipliaction table of a given number.
def table(number):
    for i in range(1,11):
        value = number * i 
        print(f"{number} * {i} = {value}")
    return "Have a Good Day(*_*)"
number = int(input("Enter the number  : "))
table_number = table(number)
print(table_number)