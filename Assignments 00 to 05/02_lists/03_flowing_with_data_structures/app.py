# Function that adds three copies of the data to the list
def add_three_copies(li, data):
    # Loop to add the data three times to the list
    for i in range(3):
        # Append the data to the list
        li.append(data)

# Main function to execute the program
def main():
    # Prompt the user to enter the data they want to copy with an emoji
    user_input = input("Enter what you want to copy 📜: ")
    
    # Initialize an empty list to store the copies
    li = []
    
    # Call the add_three_copies function to add three copies to the list
    add_three_copies(li, user_input)
    
    # Print the final list after all three copies have been added with a fun emoji
    print(f"Final list with 3 copies: 🎉 {li}")

# Calling the main function to start the program
main()
