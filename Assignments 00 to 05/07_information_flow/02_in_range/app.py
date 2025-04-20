def in_range(n, low, high):
    # 🧮 Check if n is within the inclusive range [low, high]
    if n >= low and n <= high:
        return True  # n is in range
    else:
        return False  # n is out of range
    
def prints_value():
    # 📝 Prompt user for input
    n = int(input("Enter a number (n): "))
    low = int(input("Enter the low boundary: "))
    high = int(input("Enter the high boundary: "))
    
    # 🚀 Check if n is in the range and print the result
    if in_range(n, low, high):
        print(f"✅ {n} is in the range of {low} to {high}.")
    else:
        print(f"❌ {n} is NOT in the range of {low} to {high}.")

# 🏁 Call the function to start the program
prints_value()
