# Example 1



# def make_sentence(word, part_of_speech):
#     if part_of_speech == 0:
#         print(f"I am excited to add this {word} to my vast collection of them!")
#     elif part_of_speech == 1:
#         print(f"It's so nice outside today it makes me want to {word}!")
#     elif part_of_speech == 2:
#         print(f"Looking out my window, the sky is big and {word}!")
#     else:
#         print("Part of speech must be 0, 1, or 2! Can't make a sentence.")
        
# def print_sentence():
#     word = input("Enter a word: ").strip()
#     part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
#     make_sentence(word, part_of_speech)

# print_sentence()


# Example 2



# 🎉 Welcome to the Sentence Maker Program! 🎉
# This program will create a sentence based on the word and part of speech you provide.

# def make_sentence(word, part_of_speech):
#     """This function creates a sentence based on the word and part of speech."""
#     if part_of_speech == 0:
#         print(f"📝 I am excited to add this {word} to my vast collection of them! 🎉")
#     elif part_of_speech == 1:
#         print(f"🌞 It's so nice outside today, it makes me want to {word}! 🌳")
#     elif part_of_speech == 2:
#         print(f"🌅 Looking out my window, the sky is big and {word}! 💫")
#     else:
#         print("❌ Part of speech must be 0, 1, or 2! Can't make a sentence. 🚫")

# def print_sentence():
#     """This function prompts the user to enter a word and part of speech, then calls make_sentence."""
#     while True:
#         word = input("🔠 Enter a word (noun, verb, or adjective): ").strip()
        
#         # Validate the word input (not empty)
#         if not word:
#             print("❌ You must enter a word! Please try again. 🙅‍♂️")
#             continue
        
#         # Validate the part of speech input (must be an integer: 0, 1, or 2)
#         while True:
#             try:
#                 part_of_speech = int(input("🔢 Type 0 for noun, 1 for verb, 2 for adjective: "))
#                 if part_of_speech not in [0, 1, 2]:
#                     print("❌ Invalid choice! Please enter 0, 1, or 2. 🙅‍♀️")
#                     continue
#                 break
#             except ValueError:
#                 print("❌ Please enter a valid number (0, 1, or 2). 🧮")
#                 continue

#         # Call the function to make the sentence
#         make_sentence(word, part_of_speech)

#         # Ask if the user wants to play again
#         play_again = input("🔄 Do you want to try again? (yes/y to continue or press Enter to exit): ").strip().lower()
#         if play_again not in ['yes', 'y']:
#             print("👋 Thanks for playing! Goodbye! 🎉")
#             break

# # 🚀 Start the program
# print_sentence()
