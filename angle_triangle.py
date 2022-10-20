def check_triangle(angle_1 , angle_2 , angle_3):
    if angle_1 + angle_2 + angle_3 == 180:
        print(f"It is triabgle with angle {angle_1 , angle_2 , angle_3}")
    else:
        print("It will not form a triangle")
    return ("Have , A good day")
angle_1 = int(input("Enter the angle 1 : \n"))
angle_2 = int(input("Enter the angle 2 : \n"))
angle_3 = int(input("Enter the angle 3 : \n"))
print(check_triangle(angle_1 , angle_2 , angle_3))