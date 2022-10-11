amount = int(input("Enter the amount which you want to withraw must be in multiple of 100 :"))
notes_2000 = amount//2000
notes_500 = (amount%2000)//500
notes_200 = (amount%500)//200
notes_100 = (amount%500)%(200)//100
if amount%100 !=0 :
    print("Please Enter Amount In The Multiple of 100")
else:
    print(f'''The Total number of Rs2000 notes are : {notes_2000}
The Total number of Rs500 notes are : {notes_500}
The Total number of Rs200 notes are : {notes_200}
The total number of Rs100 notes are : {notes_100}''')
