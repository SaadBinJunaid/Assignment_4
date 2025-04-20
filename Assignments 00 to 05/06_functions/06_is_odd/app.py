# 🚀 Even and Odd Number Counter Program

# 📥 This function gets a list of valid integers from the user
def get_list():
    lst = []  # 📦 Empty list to store numbers
    while True:
        user_input = input("🔢 Enter a number (or press Enter to stop): ")
        if user_input == "":  # ⛔ Stop if user just presses Enter
            break
        if not user_input.isdigit():
            print("❌ Invalid input. Please enter a valid number.")
            continue
        lst.append(int(user_input))  # ✅ Add valid number to list
    return lst

# 🔢 This function counts and prints how many even and odd numbers are in the list
def count_even_odd(lst):
    count_odd = 0  # 👥 Counter for odd numbers
    count_even = 0  # 👥 Counter for even numbers
    odd_numbers = []  # 🧺 Store odd numbers here
    even_numbers = []  # 🧺 Store even numbers here
    
    for i in lst:
        if i % 2 != 0:  # Odd number condition
            print(f"{i} is odd ✅")  # Print that the number is odd
            odd_numbers.append(i)  # Add odd number to the list
            count_odd += 1  # Increment odd count
        else:  # Even number condition
            print(f"{i} is even 🤔")  # Print that the number is even
            even_numbers.append(i)  # Add even number to the list
            count_even += 1  # Increment even count
    
    # 🎉 Display results for odd and even numbers
    print(f"\nThere are {count_odd} odd numbers in total 🎉")  # Output total odd count
    print(f"The odd numbers are: {odd_numbers}")  # List of odd numbers
    
    print(f"\nThere are {count_even} even numbers in total 🎉")  # Output total even count
    print(f"The even numbers are: {even_numbers}")  # List of even numbers

# 🚦 Main controller function
def start_program():
    print("🎉 Welcome to the Even and Odd Number Counter Program! 🚀")  # Title
    numbers = get_list()  # Get the list of numbers from the user
    count_even_odd(numbers)  # Count and display the even and odd numbers

# 🏁 Start the program
start_program()
