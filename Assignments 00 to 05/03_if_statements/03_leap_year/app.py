# 🗓️ Prompt the user to enter a year for checking leap year status
year_input = int(input("Enter a year (e.g., 2000, 1900, 2025, etc): "))  # Get user input as an integer

# 🌟 First check: Is the year divisible by 4? (Basic rule for leap years)
if year_input % 4 == 0:
    
    # 🛑 Second check: Is the year divisible by 100? (Years divisible by 100 are not leap years unless divisible by 400)
    if year_input % 100 == 0:
        
        # 🔄 Third check: Is the year divisible by 400? (Divisible by 400 means it is a leap year)
        if year_input % 400 == 0:
            print(f"🎉 The year {year_input} is a leap year! 🌟")
        else:
            print(f"🚫 The year {year_input} is NOT a leap year. It is divisible by 100 but not 400. ❌")
    else:
        # 🎉 If the year is divisible by 4 but not by 100, it's a leap year!
        print(f"🎉 The year {year_input} is a leap year! 🌟")
else:
    # 🚫 If the year is not divisible by 4, it's not a leap year.
    print(f"🚫 The year {year_input} is NOT a leap year. ❌")
