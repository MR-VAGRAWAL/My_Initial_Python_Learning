def days_in_month(month):
    return (f"There are {30*month} days in {month} months")
month = int(input("Enter the number of months :\n"))
print(days_in_month(month))