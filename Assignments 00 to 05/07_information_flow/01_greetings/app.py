# 🎉 Function to greet the user with their name
def greet(name):
    # Format the greeting message
    name = f"Greetings {name}!"
    return name  # Return the formatted greeting

# 📝 Function to ask for the user's name and call greet() to display the greeting
def user_name():
    # 🌟 Take the user's name as input
    name = input("What's your name?: ")
    # 🖨️ Call greet function and print the greeting
    print(greet(name))  # Show the greeting

# 🚀 Call the user_name function to start the greeting process
user_name()
