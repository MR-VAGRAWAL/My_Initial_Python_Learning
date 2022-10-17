def simple_interest(principal , rate , time):
    simple_interest = (principal * rate * time)/100
    return (f"Simple Interest is equals to {simple_interest}")
principal = int(input("Enter the Initial Value : \n"))
rate = eval(input("Enter the interest rate you are offered :\n"))
time = eval(input("Enter the No. of years for which you want to invest :\n"))
print(simple_interest(principal , rate , time))