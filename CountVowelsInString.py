input_string = input("Enter the string: ")
vowels = "aeiou"
vowels_count = 0
counter = input_string.__len__()
while(counter):
    if input_string[counter-1] in vowels:
        vowels_count = vowels_count+1
    counter = counter-1

print(f"there are {vowels_count} vowels in {input_string}")