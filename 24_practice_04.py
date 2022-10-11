# Ques1: Write a programme to create a dictionary of hindi words with values as their english translation. Provide user with an option to look it up! 
myDict = {
    "Pankha" : "Fan",
    "Dabba" : "Box",
    "Kitab" : "Book"
}
print("Options are : ",myDict.keys())
a = input("Enter the hindi words :\n ")
print("The meaning of your word in english is  : ",myDict.get(a))

#Ques2: Write a programme to input eight numbers from the user and display all the unique numbers(once). 
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))
num4 = int(input("Enter number 4 : "))
num5 = int(input("Enter number 5 : "))
num6 = int(input("Enter number 6 : "))
num7 = int(input("Enter number 7 : "))
num8 = int(input("Enter number 8 : "))

mySet = {num1 , num2 , num3 , num4 , num5 , num6 , num7 , num8}
print(mySet)

#Ques3: Can we have a set with 18(int) and "18"(str) as a values in it? 
        #    set = {18 , "18"} 
                        # Is this can be done? 

set = {18 , "18"}
print(set)             
                    # Yes it can be done. 

#Ques4: What will be the length of the following set S:
#             S = set()
#             S.add(20)
#             S.add(20.0)
#             S.add("20") 
                    # Find Length of the set? 

new_set = {20 , 20.0 , "20"}
print(len(new_set))
print(new_set)    
#-->Hence the length of the set will be 2 beacuse set trats equally to the int value and float value. 

#Ques5: If
            # S = {}
    # What is the type of S ?    

#Ans5 : Ths is a empty Dictionary.        

# Ques6: Crate an empty dictionary . Allow 4 friends to enter their favorite language as values and use keys as their names . Assume that the names are unique.
FavLang = {}
a = input("Enter your Favorite Language Vaibhav\n")
b = input("Enter your Favorite Language Saurabh\n")
c = input("Enter your Favorite Language Aditya\n")
d = input("Enter your Favorite Language Pragyat\n")
a = FavLang["Vaibhav"]
b = FavLang["Aditya"]
c = FavLang["Saurabh"]
d = FavLang["Pragyat"]
print(FavLang)

#Ques7: If names of 2 frienda are same then what will happen to the above programme? 

# Ans7: Only the different names will be print. 

# Ques8: If language of two friends are same ; what will happen to the above programme?  

# Ans8 : The values of the two keys can be same.

#Ques9: Can we change list in a set?

# Ans9: We can not add a list in a set, then there can be no doubt on changing it.  