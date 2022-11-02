# Write a program to read two numbers and print their quotient and remainder
divisor = int(input("Enter the divisor:\n"))
dividend = int(input("Enter the dividend:\n"))
quotient = dividend // divisor
remainder = dividend % divisor
print(f"If the Divisor is {divisor} and Dividend is {dividend} then the Quotient will be {quotient} and Remainder will be {remainder}")