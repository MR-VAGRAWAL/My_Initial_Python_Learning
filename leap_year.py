#To Check The User Input Year Is Leap Or Not:
year = int(input("Enter the Year you want to check :\n"))
if year % 100 == 0:
    if year % 400 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    if year % 4 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")