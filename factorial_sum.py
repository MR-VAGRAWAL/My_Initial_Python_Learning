def fact_sum(*arg):
    num = int(input("Enter The Number Of Integer : "))
    for i in range(num):
        number = int(input("Enter The Number : "))
        def fact(number):
            factorial = 1
            sum = 0
            for i in range(1,number+1):
                factorial *= i 
            sum += factorial
    return sum
print(fact_sum())