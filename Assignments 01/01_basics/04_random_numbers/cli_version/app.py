import random
# Example 1


# Constants for the number of random numbers, and the min/max range
# N_NUMBERS: int = 10
# MIN_VALUE: int = 1
# MAX_VALUE: int = 100

# def generate_random_numbers():
#     print("🎲 Generating 10 random numbers between 1 and 100: ")
    
#     for i in range(N_NUMBERS):
#         number = random.randint(MIN_VALUE, MAX_VALUE)  # Generate random number
#         print(f"Number {i+1}: {number} 🎉")  # Display number with index

# # Call the function to print random numbers
# generate_random_numbers()



# Example 2


def get_user_input():
    # Asking user for the number of random numbers
    while True:
        n_numbers = input("Enter the number of random numbers to generate (or press Enter to exit): ").strip()
        
        if n_numbers == "":
            print("👋 Bye! Have a great day!")  # User chose to exit the program
            exit()
        
        if n_numbers.isdigit() and int(n_numbers) > 0:
            N_NUMBERS = int(n_numbers)
            break
        else:
            print("❌ Invalid input! Please enter a positive integer for the number of random numbers.")

    # Asking user for the minimum value
    while True:
        min_value = input("Enter the minimum value for the random numbers (or press Enter to exit): ").strip()
        
        if min_value == "":
            print("👋 Bye! Have a great day!")  # User chose to exit the program
            exit()
        
        if min_value.isdigit() and int(min_value) >= 0:
            MIN_VALUE = int(min_value)
            break
        else:
            print("❌ Invalid input! Please enter a non-negative integer for the minimum value.")

    # Asking user for the maximum value
    while True:
        max_value = input("Enter the maximum value for the random numbers (or press Enter to exit): ").strip()
        
        if max_value == "":
            print("👋 Bye! Have a great day!")  # User chose to exit the program
            exit()
        
        if max_value.isdigit() and int(max_value) > MIN_VALUE:
            MAX_VALUE = int(max_value)
            break
        else:
            print(f"❌ Invalid input! Please enter an integer greater than or equal to {MIN_VALUE} for the maximum value.")

    return N_NUMBERS, MIN_VALUE, MAX_VALUE

def generate_random_numbers(N_NUMBERS, MIN_VALUE, MAX_VALUE):
    print(f"🎲 Generating {N_NUMBERS} random numbers between {MIN_VALUE} and {MAX_VALUE}: ")
    for i in range(N_NUMBERS):
        number = random.randint(MIN_VALUE, MAX_VALUE)  # Generate random number
        print(f"Number {i+1}: {number} 🎉")  # Display number with index

# Main function to run the program
def start_program():
    while True:
        N_NUMBERS, MIN_VALUE, MAX_VALUE = get_user_input()
        generate_random_numbers(N_NUMBERS, MIN_VALUE, MAX_VALUE)


start_program()
