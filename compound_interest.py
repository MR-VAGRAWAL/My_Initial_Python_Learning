def compound_interest(principal , rate , number , time):
    amount = (principal)*(1+(rate/number))**(number*time)
    compound_interest = amount - principal
    return (f"The Amount after compunding will be {compound_interest}")
principal = int(input("Enter the principal amount you want to invest : \n"))
rate = eval(input("Enter the rate of interest you are offered : \n"))
number = int(input("Enter the number of time interest is compounded per year : \n"))
time = eval(input("Enter the number of Years for which you want to invest : \n"))
print(compound_interest(principal , rate , number , time))