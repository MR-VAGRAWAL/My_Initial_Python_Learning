# Write a short program that asks you for height in centimeters and then converts your height to feet and inches (1 foot = 12 inches, 1 inch = 2.54 cm)
height_cm = eval(input("Enter The Height In Centimeter :\n"))
height_inch = height_cm /(2.54)
height_feet = height_inch / 12
print("Height in inches will be", height_inch)
print("Height in feets will be", height_feet)