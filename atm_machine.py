amount = int(input("Enter The amount you want to withdraw : "))
notes_2000 = amount//2000
notes_500 = (amount%2000)//500
notes_200 = (amount%500)//200
notes_100 = (amount%200)//100
notes_50 = (amount%100)//50
notes_20 = (amount%50)//20
notes_10 = (amount%20)//10
notes_5 = (amount%10)//5
notes_2 = (amount%5)//2
notes_1 = (amount%2)//1
print(f"The person will get {notes_2000} notes of RS2000")
print(f"The person will get {notes_500} notes of RS500")
print(f"The person will get {notes_100} notes of RS100")
print(f"The person will get {notes_50} notes of R50")
print(f"The person will get {notes_20} notes of RS20")
print(f"The person will get {notes_10} notes of RS10")
print(f"The person will get {notes_5} notes of RS5")
print(f"The person will get {notes_2} notes of RS2")
print(f"The person will get {notes_1} notes of RS1")