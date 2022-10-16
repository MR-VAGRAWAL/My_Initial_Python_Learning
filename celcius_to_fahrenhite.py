#Celcius to Fahrenhite Converter:
def converter(celcius):
    fahrenhite = (celcius*(9/5))+32              #F = ( C * 9/5)+32
    return fahrenhite
celcius = eval(input("Enter the celcius value you want to convert :\n"))
fahrenhite = converter(celcius)
print(f"{celcius} celcius when converted into fahrenhite is :{fahrenhite}")