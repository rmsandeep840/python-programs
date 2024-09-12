def IsPrime(number: int) -> bool:
    if number <= 1:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

input_number = int(input("Enter the Number: "))
if IsPrime(input_number):
    print(f"Given Number {input_number} is Prime")
else:
    print(f"Given Number {input_number} is not a Prime")
