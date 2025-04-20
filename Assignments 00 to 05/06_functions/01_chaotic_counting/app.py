import random

# Example 1


# def chaotic_counting():
#     for i in range(1,11):
#         print(i)
        
#         if done(i):
#             print("done")
#             break
# def done(num):
#     do_done = random.randint(1,10)
    
#     if do_done == num:
#         return True
#     else:
#         return False
    
        
# # Start the program
# def start_program():
#     print("Welcome to the chaotic counting program!")
#     print("This program will count from 1 to 10, but with a twist!")
#     print("Sometimes, the program will stop counting and say 'done!'")
    
#     chaotic_counting()  # Call the chaotic counting function


# start_program()



# Example 2

# # 🎉 Program Title: Chaotic Counting Game 🎉
# def chaotic_counting():
#     while True:
#         # 📝 Taking input for the first number
#         number_1 = input("Enter the first number (or press Enter to stop): ")
        
#         # 🚪 Exit the program if number_1 is empty
#         if number_1 == "":
#             print("Exiting the program... 👋")
#             break
        
#         # 🔍 Validate the input for number_1 (must be a number)
#         if not number_1.isdigit():
#             print("❌ Invalid input for first number. Please enter a valid number. 🙅‍♂️")
#             continue
#         else:
#             number_1 = int(number_1)

#         # 📝 Taking input for the second number with validation
#         while True:
#             number_2 = input("Enter the second number: ")
            
#             # 🚪 Exit if number_2 is empty
#             if number_2 == "":
#                 print("Exiting the program... 👋")
#                 return
            
#             # 🔍 Validate the input for number_2 (must be a number)
#             if not number_2.isdigit():
#                 print("❌ Invalid input for second number. Please enter a valid number. 🙅‍♂️")
#                 continue
#             else:
#                 number_2 = int(number_2)
#                 break
        
#         # 🔢 Start counting from number_1 to number_2
#         for i in range(number_1, number_2):
#             print(f"Counting: {i} 🧮")
            
#             # 🎲 Call done function to check if it's time to stop counting
#             if done(i, number_1, number_2):
#                 print("🎉 Done! 🎉")
#                 break

#         # 🔄 Ask the user if they want to play again, accepting 'yes', 'y', or 'no'
#         play_again = input("Do you want to play again? (yes/y ) or (Enter to no): ").strip().lower()
#         if play_again not in ["yes", "y"]:
#             print("👋 Thanks for playing! Goodbye. 👋")
#             break

# # 🎲 Function to check if 'done' condition occurs (random chance)
# def done(num, number_1, number_2):
#     # 🎰 Generate a random number within the user-defined range
#     do_done = random.randint(number_1, number_2)
    
#     # 🔍 Check if the random number matches the current number
#     if do_done == num:
#         return True
#     else:
#         return False

# # 🚀 Start the program
# def start_program():
#     # ✨ Welcome message with emojis and program title
#     print("🎉🎉 Welcome to the Chaotic Counting Program! 🎉🎉")
#     print("This program will count from a range you set, but with a twist! 🎲")
#     print("Sometimes, the program will stop counting and say 'done!' 🎯")
    
#     chaotic_counting()  # 🔄 Call the chaotic counting function

# # Execute the program
# start_program()
