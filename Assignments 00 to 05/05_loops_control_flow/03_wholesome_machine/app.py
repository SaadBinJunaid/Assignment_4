# 🌟 Wholesome Affirmation Machine 🌟
# This program helps you repeat a positive affirmation until you get it right! 💪😊

affirmation = "I am capable of doing anything I put my mind to."

# 📝 Initial prompt to show the affirmation
print("\n🌈 Please type the following affirmation exactly as shown:")
print(f"👉 \"{affirmation}\"\n")

# 🔁 Start the input loop
while True:
    user_input = input("💬 Type it here (or press Enter to quit): ").strip()

    # 🚪 Exit condition
    if user_input == "":
        print("👋 Bye bye! Keep believing in yourself! 💖")
        break

    # ✅ Correct affirmation
    elif user_input == affirmation:
        print("✅ That's right! You are doing great! 🌟\n")
    
    # ❌ Incorrect input
    else:
        print("❌ Hmmm... that was not the affirmation. Try again! 🤔\n")
