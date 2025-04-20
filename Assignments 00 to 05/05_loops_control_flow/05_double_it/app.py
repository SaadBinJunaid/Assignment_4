# 🚀 Welcome to the Number Doubler Program!
print("✨ Double It Until 100! ✨")
print("-" * 40)

# 🔁 Keep asking for input until the user exits
while True:
    user_input = input("🔢 Enter a number to double it (or press Enter to quit): ")

    if user_input == "":
        print("👋 Bye bye!")
        break

    if user_input.isdigit():
        curr_value = int(user_input)

        if curr_value < 100:
            print("🧠 Doubling your number until it's 100 or more:")
            while curr_value < 100:
                double_it = curr_value * 2
                print(f"The double of {curr_value} ➡️   {double_it}")
                curr_value = double_it
            print("\n✅ Done!\n")
        else:
            print("⚠️ Oops! Please enter a number less than 100.")
    else:
        print("❌ Invalid input! Please enter a valid number.")

    print("-" * 40)
