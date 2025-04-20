# Example 1

# # 📝 Starting the loop to print first 20 even numbers
# print("✨ First 20 Even Numbers: ✨")
# print("-" * 40)  # Separator line for clarity

# # 🔄 Loop through the range and print even numbers
# for i in range(20):
#     print(i * 2, end=" ")  # 🖨️ Print the even number on the same line

# print("\n" + "-" * 40)  # End separator line for clarity
# print("🎉 Done! First 20 even numbers printed! 🎉")

# Example 2
# while True:
#     try:
#         # 📝 Take user input for how many even numbers to print
#         user_input = int(input("Enter how many even numbers you want to print (e.g., 20, 40, etc.): "))
        
#         if user_input <= 0:
#             print("⚠️ Please enter a positive integer greater than 0.")
#         else:
#             break  # Exit the loop if valid input is entered
#     except ValueError:
#         print("⚠️ Invalid input! Please enter a valid integer.")

# # 🎯 Starting the loop to print even numbers based on user input
# print("✨ Printing Even Numbers as per your request: ✨")
# print("-" * 40)  # Separator line for clarity

# # 🔄 Loop through the range and print even numbers
# for i in range(user_input):
#     print(i * 2, end=" ")  # 🖨️ Print the even number on the same line

# print("\n" + "-" * 40)  # End separator line for clarity
# print(f"🎉 Done! {user_input} even numbers printed! 🎉")
