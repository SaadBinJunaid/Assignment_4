# Problem #1: List Practice

# fruit_list = ["apple","banana","orange","grape","pineapple"]
# print(f"before lenght: {len(fruit_list)}")
# print(f"The before list: {fruit_list}\n")

# fruit_list.append("mango")
# print(f"The updated list: {fruit_list}")
# print(f"after lenght: {len(fruit_list)}")



# Problem #2: Index Game
def show_menu_index_game():
    lst = [1, "hello world", 42, 3.14, "apple", "banana"]  # The list for the index game
    
    while True:
        print("\n🎮 Welcome to the Index Game!")
        print("1. Access an Element by Index")
        print("2. Modify an Element by Index")
        print("3. Slice the List")
        print("4. Display the List")
        print("5. Exit")
    
        choice = input("Enter your choice: ")
        
        if choice == "1":
            access_element(lst)
        elif choice == "2":
            Modifying_Elements(lst)
        elif choice == "3":
            Slicing_the_List(lst)
        elif choice == "4":
            display_list(lst)
        elif choice == "5":
            print("👋 Goodbye! Exiting the game.")
            break  # Exit the game
        else:
            print("❌ Invalid choice. Please choose a valid option.")

# Accessing Elements 1:

def  access_element(lst):
    while True:
        user_input = input("enter index what you want to access: ")
        if not user_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        user_input = int(user_input)
        try:
            print(f"index {user_input}: {lst[user_input]}")
        except IndexError:
            print("Index out of range. Please enter a valid index.")
            continue
            
        # ask again
        cont = input("do you want to continue? (yes/no): ").strip().lower()
        if cont != "yes":
            print("bye bye")
            break
        
        
# Modifying Elements 2:


# # Function to check if a string can be converted to a float 🌊
def is_float(value):
    try:
        float(value)  # Try converting to float
        return True   # If successful, return True
    except ValueError:
        return False  # If it fails, return False

# # Function to modify elements in the list 📋
def Modifying_Elements(lst):
    while True:
        try:
            # Ask for the index of the element to modify 🖊️
            user_input = int(input("Enter the index you want to modify: "))

            # Check if the input index is valid 🔒
            if user_input < 0 or user_input >= len(lst):
                print(f"❌ Index out of range. Please enter an index between 0 - {len(lst) - 1}.")
                continue

            # Ask the user what value they want to add 📝
            add_element = input("Enter the value you want to add: ")

            # Start conversion process 🛠️
            # This is for numbers: if the input is a digit, convert it from string to integer 🔢
            if add_element.isdigit():
                lst[user_input] = int(add_element)
                print(f"✅ Updated list: {lst}")

            # Check if the input is a float by using the is_float function 🌍
            elif is_float(add_element):
                lst[user_input] = float(add_element)
                print(f"✅ Updated list: {lst}")

            # Check for boolean value "True" 🔳
            elif add_element.lower() == "true":
                lst[user_input] = True
                print(f"✅ Updated list: {lst}")

            # Check for boolean value "False" ❌
            elif add_element.lower() == "false":
                lst[user_input] = False
                print(f"✅ Updated list: {lst}")

            # If it's none of the above, treat it as a string 🔤
            else:
                lst[user_input] = add_element
                print(f"✅ Updated list: {lst}")

            # End of conversion process 🔚

        except ValueError:
            # Handle invalid inputs 💥
            print("❌ Invalid input. Please enter a valid number or index.")
            continue

        # Ask if the user wants to continue 🛑
        cont = input("Do you want to continue? (yes/no): ").strip().lower()
        if cont != "yes":
            print("👋 Bye bye! Stay safe!")
            break

# Slicing the List 3:

def Slicing_the_List(lst):
    print("✨🎉 Welcome to the List Slicing Game! 🎉✨\n")  # Title with emojis for a fun start!
    
    while True:
        try:
            while True:
                # Getting the start index from user input
                start_index = input("🔢 Enter the start_index you want to slice (positive number): ").lstrip("0")
                if not start_index:
                    start_index = 0
                else:
                    start_index = int(start_index)
                
                # Checking if the start index is valid
                if start_index < 0 or start_index >= len(lst):
                    print(f"❌ Index out of range. Please enter an index between 0 - {len(lst) - 1}.")
                    continue
                # Check if user input start index equals the last index
                elif start_index == len(lst) - 1:
                    print(f"❌ Start index cannot be the last index of the list. Please provide a valid range.")
                    continue
                else:
                    break

            while True:
                # Getting the end index from user input
                end_index = input("⏹️ Enter the end_index where you want to stop (positive number): ").lstrip("0")
                if not end_index:
                    end_index = 0
                else:
                    end_index = int(end_index)

                # Checking if the end index is valid
                if end_index <= start_index or end_index > len(lst):
                    print(f"❌ Invalid range. Please enter an end index between {start_index} and {len(lst) - 1}.")
                    continue
                else:
                    break

            # Slicing the list from start_index to end_index (exclusive)
            slicing = lst[start_index:end_index]
            print(f"🎯 Sliced list: {slicing}")
            print(f"📜 Original list: {lst}\n")

        except ValueError:
            # Handle invalid inputs 💥
            print("❌ Invalid input. Please enter a valid number or index.\n")
            continue

        # Ask if the user wants to continue 🛑
        cont = input("🔄 Do you want to continue? (yes/no): ").strip().lower()
        if cont != "yes":
            print("👋 Bye bye! Stay safe! ✨")
            break
        
# Function to display the list
def display_list(lst):
    print(f"📜 Current list: {lst}")
    

show_menu_index_game()