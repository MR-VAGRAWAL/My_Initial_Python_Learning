# n! = 1 * 2 * 3 * 4 * 5 ............. * n

# FACTORIAL THROUGH SIMPLE FOR LOOP!!!

# n = int(input("Enter the number :\n"))
# factorial = 1
# for i in range(1,n+1):
#     factorial = i * factorial
# print(factorial)

# FACTORIAL THROUGH FUNCTION!!!

# def factorial_iter(num):
#     factorial = 1
#     for i in range(1,num+1):
#         factorial = factorial * i
#     return factorial
# number = int(input("Enter the number :\n"))
# factorial_num = factorial_iter(number)
# print(factorial_num)

# FACTORIAL THROUGH RECURSION METHODS WHICH DIRECTLY IMPLEMENT MATHEMATICAL FORMULAS!!!

def factorial_recursive(n):
    if n == 0 or n == 1:
        return n 
    return n * factorial_recursive(n-1)
n = int(input("Enter the number :\n"))
factorial_n = factorial_recursive(n)
print(factorial_n)