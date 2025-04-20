# 🎉 Double Number Program 🎉
# This program asks the user for a number, doubles it, and prints the result. 
# It continues asking until the user presses Enter without entering a number.

def double(num):
    # Function to double the input number
    double_it = num * 2  # Multiply the number by 2
    return double_it  # Return the doubled number

def start_program():
    # Title and introduction
    print("💥 Welcome to the Double Number Program! 💥")
    print("🔢 Enter a number, and I'll double it for you. Press Enter to quit.")
    
    # Infinite loop to continuously prompt the user
    while True:
        # Prompt user to input a number or quit by pressing Enter
        num = input("Enter a number or (press Enter To Quit): ")
        
        # If user presses Enter without input, exit the loop
        if num == "":
            print("👋 Bye bye! Thanks for playing!")  # Friendly exit message
            break
        
        # Check if the input is a valid number
        if not num.isdigit():
            print("❌ Invalid input. Please enter a valid number.")  # Error message for invalid input
            continue  # Skip the rest of the loop and ask for input again
        
        # Convert the input string to an integer
        num = int(num)
        
        # Print the result of doubling the number
        print(f"🌟 Double of {num} is {double(num)} 🌟")  # Display the doubled value with a nice message

# Start the program
start_program()
