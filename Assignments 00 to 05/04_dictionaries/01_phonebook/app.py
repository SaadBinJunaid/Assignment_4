def collect_phonebook_entries():
    """
    Collect phonebook entries from the user until they press Enter without entering a name.
    The user is asked to input names and phone numbers, which are stored in a dictionary.
    """
    phonebook = {}  # Create an empty phonebook dictionary
    print("📒 Phonebook Entry Collection 📒")  # Title for the section

    while True:
        name = input("\n💬 Enter a name (or press Enter to stop): ")  # Ask for a name with emoji
        if name == "":  # Stop if the user presses Enter without typing a name
            break
        
        while True:
            phone_number = input("📞 Enter a phone number: ")  # Ask for the phone number with emoji
            
            try:
                # Try to convert the phone number to an integer
                phone_number = int(phone_number)
                break  # If the conversion is successful, exit the inner loop
            except ValueError:
                # If the conversion fails, inform the user and ask again
                print("❌ Invalid input. Only numbers are allowed. Please try again. ❌")

        # Store the phone number as an integer in the dictionary with the name as the key
        phonebook[name] = phone_number
    
    return phonebook  # Return the collected phonebook


def display_phonebook(phonebook):
    """
    Display all entries in the phonebook (name and phone number).
    """
    print("\n📖 Phonebook Entries 📖")  # Title for the section
    if phonebook:
        for index, (name , number) in enumerate(phonebook.items(),start=1):  # Iterate over the dictionary and display the entries
            print(f"{index}. {name} 📞: {number}")
    else:
        print("The phonebook is empty.")


def search_in_phonebook(phonebook):
    """
    Allow the user to search for a name in the phonebook.
    If the name exists, print the corresponding phone number.
    Otherwise, inform the user that the name is not found.
    """
    print("\n🔍 Search in Phonebook 🔍")  # Title for the section
    while True:
        name = input("\n🔎 Enter a name to search for (or press Enter to stop): ")  # Search prompt with emoji
        if name == "":  # Exit the loop if the user presses Enter without entering a name
            break
        
        # If the name exists in the phonebook, print the phone number
        if name in phonebook:
            print(f"{name} 📞: {phonebook[name]}")
        else:
            print(f"❌ {name} not found in the phonebook. ❌")


def start_program():
    """
    Main function to start the program: collect phonebook entries, display them, and allow searching.
    """
    print("📱 Welcome to the Phonebook Program! 📱\n")  # Title with welcome message
    phonebook = collect_phonebook_entries()  # Collect phonebook entries
    display_phonebook(phonebook)  # Display all the entries
    search_in_phonebook(phonebook)  # Allow the user to search for a name


# Start the program
start_program()
