largest_number = None  # Initialize with None to handle negative numbers
counter = 1

while counter <= 3:
    input_number = int(input(f"Enter Number {counter}: "))
    
    # If it's the first iteration or input_number is greater than current largest_number
    # largest_number is None should be first in the if condition. if it evaluates to true then the second expression input_number > largest_number is not executed.
    # else it will give you  TypeError: '>' not supported between instances of 'int' and 'NoneType'
    if largest_number is None or input_number > largest_number:
        largest_number = input_number    
    counter += 1

print(str(largest_number) + " is the largest of all numbers.")
