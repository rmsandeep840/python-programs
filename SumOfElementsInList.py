print ("Add items to the Integer-List. Enter stop to stop adding.")
integer_list = []

while True:
    input_numberStr = input()
    if input_numberStr != "stop":
        integer_list.append(int(input_numberStr))
    else:
        break
print(integer_list)

sum = 0
while len(integer_list):
    sum = sum + integer_list.pop()
print(f"sum of all the numbers in the list in {sum}")


