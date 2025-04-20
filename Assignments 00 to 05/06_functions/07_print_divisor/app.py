# 🚀 Divisor Finder Program

# 📥 This function prints all divisors of the given number
def divisor(num):
    print(f"\nHere are the divisors of {num} 🔢:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(f"✅ {i}")  # Divisor found, print it

# 🚦 Main controller function
def print_divisor():
    print("🎉 Welcome to the Divisor Finder Program! 🚀")  # Title with emoji
    while True:
        user_input = input("🔢 Enter a number (or press Enter to stop): ")
        
        if user_input == "":  # ⛔ Stop if user just presses Enter
            print("Goodbye! 👋")  # Goodbye message
            break
        
        if not user_input.isdigit():  # Validate input
            print("❌ Invalid input. Please enter a valid number.")
            continue  # Continue to the next iteration if invalid
        
        # Convert input to integer and call the divisor function
        divisor(int(user_input))

# 🏁 Start the program
print_divisor()  # Run the program
