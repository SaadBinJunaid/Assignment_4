def collect_numbers():
    """
    Prompt the user to enter numbers one by one. 
    Stop collecting when the user presses Enter without entering a number.
    The entered numbers are stored in a list.
    """
    print("🎯 Welcome to the Number Frequency Counter! 🎯")
    print("You can input numbers one by one. Press Enter when you're done. Let's go!")
    
    numbers = []  # Initialize an empty list to store the numbers
    while True:
        user_input = input("Enter a number (or press Enter to stop): ")  # Ask for user input
        if user_input == "":  # If the user presses Enter without typing anything, stop the loop
            break
        numbers.append(int(user_input))  # Convert input to an integer and add it to the list
    
    return numbers  # Return the list of entered numbers


def count_number_frequency(numbers):
    """
    Count how many times each number appears in the list.
    """
    frequency_dict = {}  # Initialize an empty dictionary to store the counts
    for num in numbers:  # Loop through each number in the list
        if num not in frequency_dict:  # If the number is not in the dictionary, add it with a count of 1
            frequency_dict[num] = 1
        else:  # If the number is already in the dictionary, increment its count
            frequency_dict[num] += 1
    
    return frequency_dict  # Return the dictionary with number counts


def display_number_frequency(frequency_dict):
    """
    Display how many times each number appears, based on the frequency dictionary.
    """
    print("📊 Results: Number Frequency 📊")  # Title for the results section
    for num in frequency_dict:  # Loop through each number in the dictionary
        print(f"{num} appears {frequency_dict[num]} times. 🧮")  # Print the number and its count with a visual touch


def run_program():
    """
    Run the program: collect numbers, count their occurrences, and display the results.
    """
    numbers = collect_numbers()  # Get numbers from the user
    frequency_dict = count_number_frequency(numbers)  # Count the frequency of each number
    display_number_frequency(frequency_dict)  # Display the results


# Start the program
run_program()
