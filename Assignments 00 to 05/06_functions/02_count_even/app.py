# 🚀 Even Number Counter Program

# 📥 This function gets a list of valid integers from the user
def get_list():
    lst = []  # 📦 Empty list to store numbers
    while True:
        user_input = input("🔢 Enter a number (or press Enter to stop): ")
        if user_input == "":
            break  # ⛔ Stop if user just presses Enter
        if not user_input.isdigit():
            print("❌ Invalid input. Please enter a valid number.")
            continue
        lst.append(int(user_input))  # ✅ Add valid number to list
    return lst

# 🔢 This function counts and prints how many even numbers are in the list
def count_even(lst):
    count = 0
    even_numbers = []  # 🧺 Store even numbers here
    
    for i in lst:
        if i % 2 == 0:
            print(f"{i} is even ✅")
            even_numbers.append(i)
            count += 1

    print(f"\nThere are {count} even numbers in total 🎉")
    print(f"The even numbers are: {even_numbers}")


# 🚦 Main controller function
def start_program():
    print("🎉 Welcome to the Even Number Counter Program!")
    numbers = get_list()
    count_even(numbers)

# 🏁 Start the program
start_program()
