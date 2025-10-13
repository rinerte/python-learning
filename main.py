# exception_handling

try:
    numerator = int(input("Enter a number: "))
    denominator = int(input("Enter a denominator: "))
    result = numerator / denominator
    print(f"{numerator} divided by {denominator} is {result}")
except ZeroDivisionError as e:
    print(e)
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")