MAX_LENGTH = 3  # 🌟 Maximum allowed length for the list (You can change this value!)

# 🧠 Function to shorten the list to MAX_LENGTH by removing elements from the end
def shorten(lst):
    while len(lst) > MAX_LENGTH:  # 🔄 Check if the list is longer than MAX_LENGTH
        removed_item = lst.pop()  # 🔪 Remove the last item from the list
        print(f"🗑️ Oops! Removed item: {removed_item} 🙈")  # ✨ Print the removed item with a fun message

# 🧺 Function to ask the user for input and create the list
def get_list():
    lst = []  # 📦 Initialize an empty list to store the user's input
    print("🌟 Welcome to the List Maker! 🌟")  # ✨ Welcome message
    print("🔸 Enter items one by one and press Enter without typing anything to stop. 🔸")
    
    user_input = input("➡️ Please enter a value to add to your list: ")  # Ask the user to input the first value
    
    while user_input != "":  # 🛑 Stop when the user presses Enter without typing anything
        lst.append(user_input)  # ➕ Add the input value to the list
        print(f"💫 Great! You added: {user_input} to your list! 🌈")  # ✨ Confirm with the user
        user_input = input("➡️ Please enter another value or press Enter to stop: ")  # Ask again for another value
    
    print(f"📝 Here’s your final list: {lst} 🎉")  # 📜 Show the complete list at the end
    return lst  # 🚀 Return the full list once the user is done entering values

# 🚦 Main function to run the entire program
def start_program():
    lst = get_list()  # 🧺 Get the list from the user
    shorten(lst)  # ✂️ Shorten the list if it's longer than MAX_LENGTH
    print(f"✨ Final list after shortening: {lst} 🏁")  # 📋 Show the final list after the changes

# 🏁 Start the program
start_program()
