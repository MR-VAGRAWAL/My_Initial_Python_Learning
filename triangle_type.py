def check_triangle(side_1 , side_2 , side_3):
    if (side_1 == side_2 == side_3):
        print("It is an equivalent triangle")
    elif (side_1 == side_2) or (side_2 == side_3) or (side_3 == side_1):
        print("It is a isosceles triange")
    else:
        print("It is scalene triangle")
    return ("Have , A good day")
side_1 = int(input("Enter the side 1 : \n"))
side_2 = int(input("Enter the side 2 : \n"))
side_3 = int(input("Enter the side 3 : \n"))
print(check_triangle(side_1 , side_2 , side_3))