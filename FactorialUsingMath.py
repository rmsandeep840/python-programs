import math

def factorial(n: int):
    return math.factorial(n)

number = int( input("please enter the nubmer"))

if (number < 0):
    print("factorial cant be determined for negative numbers")
else:
    print(f"factorial of given number {number} is: ", factorial(number))