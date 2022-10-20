from re import A


def roots(a , b , c):
    D = (b**2 - 4*a*c)
    if D>=0:
        root1 = ((-b) + (D**0.5))/2*a
        root2 = ((-b) - (D**0.5))/2*a
        print(f"The Roots of the equation {a}x^2 + {b}x + {c} are {root1} and {root2}")
    else:
        print("No real Roots")
    return ("Have A Good Day")
a = int(input("Enter the value of a:\n"))
b = int(input("Enter the value of b:\n"))
c = int(input("Enter the value of c:\n"))
quadratic_equation = (f"{a}^2 + {b}x + {c}")
print(quadratic_equation)
print(roots(a,b,c))