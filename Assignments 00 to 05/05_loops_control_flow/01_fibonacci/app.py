# Example 1

# # 🎯 MAX_VALUE is the upper limit for the Fibonacci sequence
# MAX_VALUE = 10000

# # 🐠 Starting values for Fibonacci sequence
# fib_1 = 0  # Fib(0)
# fib_2 = 1  # Fib(1)

# # ✨ Starting the Fibonacci sequence calculation
# print("🔢 Fibonacci Sequence up to", MAX_VALUE)
# print("-" * 40)  # Separator line for clarity

# # 🔄 Keep calculating until the current Fibonacci number exceeds MAX_VALUE
# while fib_1 <= MAX_VALUE:
#     print(fib_1)  # 🖨️ Print the current Fibonacci number
    
#     # ➕ Calculate the next Fibonacci number
#     fib_next = fib_1 + fib_2
    
#     # 🛠️ Update the Fibonacci numbers
#     fib_1 = fib_2  # Move fib_1 to the next number in the sequence
#     fib_2 = fib_next  # Move fib_2 to the next number in the sequence

# # 🎉 End of Fibonacci sequence
# print("-" * 40)  # Separator line for clarity
# print("🎉 The Fibonacci sequence up to", MAX_VALUE, "has been printed! 🎉")



# Example 2
# where user enter max value

# # 🎯 Ask the user for the maximum value for the Fibonacci sequence
# MAX_VALUE = int(input("Enter the maximum value for Fibonacci sequence: "))

# # 🐠 Starting values for Fibonacci sequence
# fib_1 = 0  # Fib(0)
# fib_2 = 1  # Fib(1)

# # ✨ Check if the user input is valid
# if MAX_VALUE <= 0:
#     print("❌ Please enter a positive value greater than 0. ❌")
# else:
#     # ✨ Starting the Fibonacci sequence calculation
#     print(f"🔢 Fibonacci Sequence up to {MAX_VALUE}")
#     print("-" * 40)  # Separator line for clarity

#     # 🔄 Keep calculating until the current Fibonacci number exceeds MAX_VALUE
#     while fib_1 <= MAX_VALUE:
#         print(fib_1)  # 🖨️ Print the current Fibonacci number
        
#         # ➕ Calculate the next Fibonacci number
#         fib_next = fib_1 + fib_2
        
#         # 🛠️ Update the Fibonacci numbers
#         fib_1 = fib_2  # Move fib_1 to the next number in the sequence
#         fib_2 = fib_next  # Move fib_2 to the next number in the sequence

#     # 🎉 End of Fibonacci sequence
#     print("-" * 40)  # Separator line for clarity
#     print(f"🎉 The Fibonacci sequence up to {MAX_VALUE} has been printed! 🎉")
