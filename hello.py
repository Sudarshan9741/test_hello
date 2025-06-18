# Simple calculator in Python

print("Welcome to the Simple Calculator")

# Get input from the user
num1 = float(input("Enter the first number: "))
operation = input("Choose an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform calculation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation."

# Display the result
print("Result:", result)
