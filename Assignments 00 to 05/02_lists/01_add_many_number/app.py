#  Defining a function to sum the list manually
def add_sum(num2) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total_sum = 0  # Initialize total_sum to 0
    for num1 in num2:  # Loop through each number in the list
        total_sum += num1  # Add the current number to the total_sum
    
    return total_sum  # Return the total sum after the loop finishes

def add_list():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # List of numbers
    sum_numbers = add_sum(numbers)  # Call the add_sum function
    print(sum_numbers)  # Print the final sum

add_list()  # Calling the function to test it
