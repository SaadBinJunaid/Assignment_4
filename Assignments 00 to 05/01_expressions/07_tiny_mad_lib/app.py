# Display the template sentence to the user with emojis for clarity
print("📝 Here is the template of the story: 📝")
print("🗣️ Code in Place is fun. I learned to program and used Python to make my {Adjective} {Noun} {Verb}! 🖥️")

# Collect inputs from the user with clear prompts
Adjective = input("👉 Please type an Adjective and press enter: ")
Noun = input("👉 Please type a Noun and press enter: ")
Verb = input("👉 Please type a Verb and press enter: ")

# Construct the story using an f-string
Story_Sentence = f"✨ Code in Place is fun. I learned to program and used Python to make my {Adjective} {Noun} {Verb}! ✨"

# Display the final sentence with emojis for emphasis
print("\n🎉 Here is your story: 🎉")
print(f"📜 {Story_Sentence} 📜")
