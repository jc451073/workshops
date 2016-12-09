
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator

    while denominator == 0:

        denominator = int(input("Enter the denominator: "))

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    print("Please enter a valid integer.")
print("Finished.")

