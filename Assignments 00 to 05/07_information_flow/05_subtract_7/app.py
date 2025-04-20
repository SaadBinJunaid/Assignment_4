def subtract_seven(num):
    # Subtract 7 from the given number and return the result
    return num - 7

def print_subtracted_number():
    # Ask the user to enter a number they want to subtract 7 from
    num = int(input("🔢 Enter a number which you want to subtract 7 from: "))
    
    # Call the subtract_seven function to perform the subtraction
    result = subtract_seven(num)
    
    # Print the result in a clear and formatted way
    print(f"🔻 Result of subtracting 7 from {num} is: {result} ✅")  # Show the final result

# Run the function to get the result from the user input
print_subtracted_number()
