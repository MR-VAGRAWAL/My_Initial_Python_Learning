def showInfo(student_name , course_name = "B.TECH"):
    info = f'''Name : {student_name}
Course : {course_name}'''
    return info
print(showInfo("Vaibhav"))