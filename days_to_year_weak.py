def check(days):
    count_year = 0
    count_month = 0
    count_week = 0
    for i in range(1 , days+1):
        if i % 365 == 0 :
            count_year = count_year + 1
        elif i % 7 == 0 :
            count_week = count_week + 1 
        elif i % 30 == 0 :
            count_month = count_month + 1
    return (f"No. of years is {count_year} and No. of months is {count_month} and No. of weeks is {count_week} ")
days = int(input("Enter the number of days : \n"))
print(check(days))