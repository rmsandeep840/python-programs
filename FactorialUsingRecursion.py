def factorial (n :int) -> int:
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
    
number = int(input("please enter the number"))
print (f"factorial of a number {number} is", factorial(number))