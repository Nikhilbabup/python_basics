try:
    number = int(input("Enter a number: "))
    print(f"You enterd number: {number}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
