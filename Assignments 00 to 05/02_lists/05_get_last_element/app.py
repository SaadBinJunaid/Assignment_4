# 🧠 Function to show the Last element of the list
def get_last_element(lst):
    print("🎯 Here is the Last element of your list:")
    print(lst[len(lst) - 1])  # 📌 Shows the Last item

# 🧺 Function to let the user make a list
def make_user_list():
    print("📝 Let's make a list! Type one item at a time.")
    print("💡 Press Enter without typing to finish the list.")
    
    lst = []  # 📦 Empty list to store user's items
    elemt = input("➡️ Please enter an element of the list or press enter to stop: ")
    
    while elemt != "":
        lst.append(elemt)  # 🧩 Add the item to the list
        elemt = input("➡️ Please enter an element of the list or press enter to stop: ")
        
    return lst  # 🚀 Return the full list

# 🚦 function to start the program 
def start_program():
    print("📌 Welcome! In this program, you'll:")
    print("1️⃣ Create a list")
    print("2️⃣ Then see the Last item you typed!\n")
    
    lst = make_user_list()  # 🧺 Get the list from the user
    get_last_element(lst)  # 🎯 Show the Last element

# 🏁 Start the program
start_program()
