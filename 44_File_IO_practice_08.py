# Ques 1 : Write a program to read the text from a given file "poem.txt" and find out wheather it contains the word "Twinkle"
f = open ("44_poem.txt")
t = f.read()
if "Twinkle" in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()

#Ques 2 : The game() function in a program lets a user play a game and returns the score as an integer . You need to read a file "Hiscore.txt" which is either blank or contains the previous Hi-Score . You need to write a program to update the Hi-score whenever game() breaks the Hi-score.
def game():
    return 66
score = game()
with open("44_High_Score.txt") as f:
    High_Score = int(f.read())
if High_Score < score:
    with open("44_High_Score.txt" , "w") as f:
        f.write(str(score))

# Ques 3 : Write a program to generate multiplication tables from 2 to 20 and write it to the defined files . Place these files in a folder for a 13-years old.
for i in range(1,21):
    with open(f"44_Multipliaction_table_of_{i}" , "w") as f:
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}\n")