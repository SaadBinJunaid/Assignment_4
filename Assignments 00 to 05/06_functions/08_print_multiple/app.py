# Function to print the message multiple times
def print_multiple(message, repeats):
    # This loop will print the 'message' variable 'repeats' number of times
    for _ in range(repeats):
        print(message)  # Print the message

# Main function to handle user inputs
def take_input():
    # Add a title with some emojis to make it look nice
    print("🚀 Welcome to the Message Repeater Program! 🚀")
    print("=============================================")  # Add a separator for a clean look
    
    while True:  # This loop will run forever unless manually broken
        # Ask the user to type a message
        message = input("📝 Please type a message (or press Enter to exit): ").strip()  # Clean up any unwanted spaces
        
        # Check if the user typed an empty message (i.e., pressed Enter)
        if message == "":
            print("👋 You didn't type anything. Bye bye! 👋")
            break  # Exit the loop if no message is entered
        
        # Check if the user entered only numbers (which is not allowed)
        if message.isdigit():
            print("🚫 You entered a number. Please enter a valid string (not a number).")
            continue  # If the input is a number, ask again
        
        # Inner loop to ask how many times to repeat the message
        while True:
            # Ask the user for how many times they want to repeat the message
            repeats = input("⏳ Enter how many times to repeat your message (a positive number): ").strip()
            
            # Check if the entered value is not a number
            if not repeats.isdigit():  # If it's not a number
                print("❌ You entered something that is not a number. Please enter a valid number.")
                continue  # Ask again
            
            # Convert the string to an integer
            repeats = int(repeats)
            
            # Print the message the specified number of times
            print_multiple(message, repeats)
            
            # Ask the user if they want to play again
            play_again = input("🔄 Do you want to more Message Repeate again? Type 'yes' or 'y' to continue (Press Enter to exit): ").strip().lower()
            
            # If the user doesn't want to continue, exit the loop
            if play_again not in ["yes", "y"]:
                print("👋 Thanks for playing! Goodbye. 👋")  # Goodbye message
                return  # Exit the entire program

# Run the program
take_input()
