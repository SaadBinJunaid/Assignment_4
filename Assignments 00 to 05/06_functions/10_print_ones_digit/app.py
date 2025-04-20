# 🎉 Function to extract the last digit (ones digit) of a number
def the_one_digit(num):
    # 💡 Get the remainder when dividing by 10, which gives the ones digit
    one_digit = num % 10
    return one_digit

# 📝 Function to prompt the user and print the result
def print_digit():
    # 📥 Asking the user to enter a number
    num = int(input("🔢 Enter a number: "))

    # 🧮 Get the last digit using the the_one_digit function
    num = the_one_digit(num)

    # 🎯 Print the result with a clear and fun message
    print(f"The last digit of the number is: {num} 🎉")

# 🚀 Calling the print_digit function to run the program
print_digit()
