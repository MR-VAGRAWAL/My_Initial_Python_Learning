def factorial_sum(*num):
    def fact(n):
        if n == 0:
            return 1
        factorial = 1
        for a in range(1,n+1):
            factorial *= a
        return factorial
    sum = 0
    for number in num:
        if number >= 0:         
            sum += fact(number)
    return sum
print(factorial_sum(1,2,3,4,5,-3,-7,-17,0))
