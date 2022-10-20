def check_triangle(side_1 , side_2 , side_3):
    if (side_1 + side_2 > side_3)and(side_1 + side_3 > side_2)and(side_2 + side_3 > side_1):
        print("It will form a triangle")
    else:
        print("It will not form a triange")
    return ("Have , A good day")
side_1 = int(input("Enter the side 1 : \n"))
side_2 = int(input("Enter the side 2 : \n"))
side_3 = int(input("Enter the side 3 : \n"))
print(check_triangle(side_1 , side_2 , side_3))