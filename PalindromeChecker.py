input_string = input("Enter the string: ")
reversed_string = ""
counter = input_string.__len__()
while (counter):
    reversed_string = reversed_string + input_string[counter-1]
    counter = counter-1
if input_string == reversed_string:
    print(f"Entered String {input_string} is Palindrome")
else:
    print(f"Entered String {input_string} is not palindrome")