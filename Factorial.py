input_number = int (input("Enter an integer: "))
factorial_result = 1
givenNumber = input_number
while input_number > 0:
    factorial_result = factorial_result * input_number
    input_number= input_number-1

print (f"Factorial of a given number  {givenNumber} is : {factorial_result}")