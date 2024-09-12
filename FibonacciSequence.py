# Python program to generate Fibonacci sequence up to 100
#The Fibonacci sequence is the series of numbers where each number is the sum of the two preceding numbers

# # Initialize the first two numbers
# a, b = 0, 1

# # Print the Fibonacci sequence until the value exceeds 100
# print("Fibonacci sequence up to 100:")

# while a <= 100:
#     print(a, end=" ")
#     a, b = b, a + b  # Update to the next Fibonacci numbers


# version 2
a = 0
b = 1

input_number = int (input("Enter the max number for your Fibonacci sequence "))

while a <= input_number:
    temp = a
    print (a , end=" ")
    a = b
    b = temp + b