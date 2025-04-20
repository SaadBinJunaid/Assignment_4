# 🧠 Function to create a list from user input
def get_list():
    full_list = []  # 📦 Initialize an empty list to store user input
    
    # ✍️ Ask for user input
    user_input = input("Enter a value which you want to add in list: ")

    # 🛑 Loop continues as long as the user enters something (not an empty string)
    while user_input:  
        full_list.append(user_input)  # 🧩 Add the user's input to the list
        # ✍️ Prompt the user for another value
        user_input = input("Enter a value which you want to add in list: ")

    # 🎯 Once the user presses Enter without typing anything, print the list
    print(f"Here's the list: {full_list}")  # 📜 Shows the final list to the user
    
    
# 🏁 Call the function to run the program
get_list()
