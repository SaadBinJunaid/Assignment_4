# Prompt the user to enter the first number (dividend)
num1 = int(input("Please enter an integer to be divided: "))

# Prompt the user to enter the second number (divisor)
num2 = int(input("Please enter an integer to divide by: "))

# Use the divmod() function to calculate the quotient and remainder
# divmod(num1, num2) returns a tuple (quotient, remainder)
quotient, remainder = divmod(num1, num2)

# Print the result, showing both the quotient and the remainder of the division
print(f"The result of this division is {quotient} with a remainder of {remainder}")


# example Output
# Please enter an integer to be divided: 17
# Please enter an integer to divide by: 5
# The result of this division is 3 with a remainder of 2