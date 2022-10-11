# Write a programme to display a user entered name followed by Good Afternoon using input() function. 

name = input("Enter your name :- \n ")
print("Good Afternoon , " +  name)

# Write a programme to fill in a letter template given below with name and date.
#        letter = ''' Dear <|NAME|>,
#                             You are selected!
#                             <|DATE|> '''

letter = '''Dear <|NAME|>,
      Greeting from GLA University , 
      I am hapy to tell you that , You are Selected!

                     <|DATE|>
'''
name  = input("Enter your name : \n")
date  = input("Enter date : \n")
letter = letter.replace("<|NAME|>" , name)
letter = letter.replace("<|DATE|>" , date)
print(letter)

# Write a programme to detect double spaces in a string. 

story =  "Once upon a time there is a king name  Vaibhav  , who lives with his family in his kingdom."
double_spaces = story.find("  ")
if double_spaces != 1:
    print("Yes , there is a double spaces in the string. ")
else:
    print("No , there is no double spaces in string")


# Replace a double spaces from above problem with single spaces. 

story = story.replace("  " , " ")    
print(story)


# Write a programme to format the following letter using escape sequence characters.         
   # letter = "Dear Vaibhav , This Python Course is nice. Thanks!" 
   
   
letter = "Dear Vaibhav , This Python Course is nice. Thanks!" 
print(letter)
formatted_letter = "Dear Vaibhav ,\n \t This Python Course is nice. \nThanks!"
print(formatted_letter) 
 