# Write a command to store seven fruits in a list entered by the user.

fru1 = input("Enter Fruit Name 1 : ")
fru2 = input("Enter Fruit Name 2 : ")
fru3 = input("Enter Fruit Name 3 : ")
fru4 = input("Enter Fruit Name 4 : ")
fru5 = input("Enter Fruit Name 5 : ")
fru6 = input("Enter Fruit Name 6 : ")
fru7 = input("Enter Fruit Name 7 : ")
MyFruitList = [fru1 , fru2 , fru3 , fru4 , fru5 , fru6 , fru7]
print(MyFruitList)

# Write a programme to accept marks of 6 students and display them in a sorted manner. 

Marks1 = int(input("Enter the marks obtained b student 1 : "))
Marks2 = int(input("Enter the marks obtained b student 2 : "))
Marks3 = int(input("Enter the marks obtained b student 3 : "))
Marks4 = int(input("Enter the marks obtained b student 4 : "))
Marks5 = int(input("Enter the marks obtained b student 5 : "))
Marks6 = int(input("Enter the marks obtained b student 6 : "))
MyList = [ Marks1 , Marks2 , Marks3 , Marks4 , Marks5 , Marks6 ]
MyList.sort()
print(MyList)

# Check that a tuple cannot be chanegd in python.

tuple = (25,95,75,755,25)
tuple[2] = 100

# Write a programme to suma list with 4 numbers. 

list = [25 , 65 , 89 , 96]
print(list[0] + list[1] + list[2] + list[3])
print(sum(list))

# Write a programme to count the number of zeros in the following tuple:
#              a = (7 , 0 , 8 , 0 , 0 , 9 )

a = (7 , 0 , 8 , 0 , 0 , 9 )
print(a.count(0))