#Ques1: Write a programme to find greatest of four numbers entered by the user. 
num1 = int(input("Enter your first number :\n"))
num2 = int(input("Enter your second number :\n"))
num3 = int(input("Enter your third number :\n"))
num4 = int(input("Enter your fourth number :\n"))
# LONG PROCEDUR.
# if (num1 >= num2 and num1 >=num3 ) and (num1 >= num4):
#     print("The greatest number is " ,num1)
# elif (num2 >= num3 and num2 >=num4 ) and (num2 >= num1):
#     print("The greatest number is " ,num2)
# elif (num3 >= num4 and num3 >=num1 ) and (num3 >= num2):
#     print("The greatest number is " ,num3)
# :
#     print("The greatest number is " ,num4)
if (num1 >= num2):
    f1 = num1
else:
    f1 = num2
if (num3 >= num4):
    f2 = num3
else:
    f2 = num4
if (f1 >= f2):
    print(f1," is the greates number.")
else:
    print(f2," is the greatest number")

# Ques2: Write a programme to find out wheather a student is pas or fail , if it requires total 40% and at least 33% in each subject to pass . Assume 3 subjects and take marks as an input from the user. 

marks1 = int(input("Enter the marks obtained in subject 1 out of 100: "))
marks2 = int(input("Enter the marks obtained in subject 2 out of 100 : "))
marks3 = int(input("Enter the marks obtained in subject 3 out of 100: "))
if (marks1<33) or (marks2<33) or (marks3<33):
    print("You are fail because you have not scored more than 33% in each subject.")
elif ((marks1+marks2+marks3)/3 < 40):
    print("You are fail due to total percentage less than 40 ")
else:
    print("You are pass")


# Ques3: A spam comment is defined as a text containing following keywrds:
# "make a lot of money" , "buy now" , "subscribe this" , "click this" .
# Write a programme to detect these spams. 

text = input("Enter the text \n")
spam = False
if ("make a lot of money" in text):
    spam = True
elif ("buy now" in text):
    spam = True
elif ("subscribe this" in text):
    spam = True
elif ("click this" in text):
    spam = True
else:
    spam = False
if (spam):
    print("This text is spam!")
else:
    print("This text is not a spam")    

# Ques4: Write a programme to find wheather a given username contains less than 10 character or not. 

username = input("Engter the username :\n")
if (len(username)>10):
    print("more than 10 characters")
elif(len(username)=10):
    print("exactly 10 character")
else:
    print("less than 10 characters")
# Ques5: Write a programme which finds out wheather a given name is present in a list or not . 

names = ("vaibhva" , "aditya" , "saurabh" , "pragyat" , "mushkan")
name = input("Enter the name to check :\n")
if name in names:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")

# Ques6 :Write a programme to calculate the grade of a student from re import A
# from his marks from the following scheme:
#         90 - 100 -> Ex
#         80 - 90 -> A
#         70 - 80 -> B
#         60 - 70 -> C
#         50 -60 -> D 
#         <50 - F

marks = int(input("Enter your marks  :\n"))
if (100 > marks > 90):
    grade = Ex
elif (90 > marks > 80):
    grade = A
elif (80 > marks > 70):
    grade = B
elif (70 > marks > 60):
    grade = C
elif (60 > marks > 50):
    grade = D
else:
    grade = F
print("Your grade is : " ,grade)

# Ques7: Write a programme to find out wheather a given post is talking about "Vaibhav" or not. 
post = input("Enter the post :")
if ("vaibhav" in post.lower()):
    print("Yes! , the post contains the name Vaibhav.")
else:
    print("No! , the post doesnot contains the name Vaibhav .")