# Example 1


# def averages(a,b):
#     average = (a + b) / 2
#     return average

# def print_averages():
#     avg_1 = averages(0 ,10)
#     avg_2 = averages(8, 10)
#     result = averages(avg_1, avg_2)
#     print(f"🎉 The average of {avg_1} and {avg_2} is: {result} 🎉\n")

# print_averages()



# Example 2


# # 🚀 Function to calculate the average of two numbers
# def averages(a, b):
#     average = (a + b) / 2
#     return average

# # 🧠 Function to validate if input is a valid number
# def validation(num):
#     try:
#         num = float(num)  # Try to convert to float
#         return True
#     except ValueError:
#         return False  # Return False if invalid input

# # ✨ Main function to handle the input and calculation
# def Print_average():
#     print("✨ Welcome to the Average Calculator! ✨")
    
#     while True:
#         # 🚨 Ask for the first number
#         a = input("🔢 Enter the first number: ")
        
#         if a == "":
#             print("👋 Bye bye! See you next time!")  # Exit condition
#             break
        
#         # Check if the first input is valid
#         if not validation(a):
#             print("❌ Invalid input! Please enter a valid number for the first value.\n")
#             continue  # Ask for input again if invalid
        
#         # 🚨 Ask for the second number, with validation loop
#         while True:
#             b = input("🔢 Enter the second number: ")
            
#             # Check if the second input is valid
#             if not validation(b):
#                 print("❌ Invalid input! Please enter a valid number for the second value.\n")
#                 continue  # Ask for input again if invalid
            
#             # If valid, break out of the second input loop
#             break
        
#         # Convert inputs to floats after validation
#         a = float(a)
#         b = float(b)

#         # Calculate and print the average
#         average_result = averages(a, b)
#         print(f"🎉 The average of {a} and {b} is: {average_result} 🎉\n")
        
#         # ✨ Continue or exit the loop
#         print("-" * 40)  # Divider line for clarity
#         continue_choice = input("Would you like to calculate another average? (y/n): ").lower()

#         if continue_choice != "y":
#             print("👋 Bye bye! Have a great day!")
#             break  # Exit if user doesn't want to continue

# # 🚀 Run the program
# Print_average()
