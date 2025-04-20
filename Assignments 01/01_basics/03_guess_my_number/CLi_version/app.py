import random

def Guess_My_Number():

    print("🎉 Welcome to 'Guess My Number'! 🎯")
    print("🤔 I'm thinking of a number between **1 and 100**. Can you guess it?")
    
    # Generate a random number between 1 and 100
    random_number = random.randint(1,100)   
     
    attempts = 0
    while True:
        try:
            user_guess_number = int(input("Enter a new guess number: "))
            if user_guess_number < 1 or user_guess_number > 100:
                print("❌ Invalid guess! Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue
            
        attempts += 1
        
        # 🎯 if user guess it in First Attempt so than this Success statment works
        if user_guess_number == random_number and attempts == 1:
            print(f"🎊 WOW! You nailed it on your FIRST attempt! ({attempts} try) 🏆 You're a genius! 🧠🔥")
            break
        
        # 📈 if Guess is High so than this statment works
        if user_guess_number > random_number:
            print("Your guess is High")
            
        # 📈 if Guess is Low so than this statment works   
        elif user_guess_number < random_number:
            print("Your guess is Low")
            
        # 🎉 if user guess it (After Multiple Attempts) so than this Success statment works
        else:
            print(f"Congratulations! You have guessed the number but guessed it in {attempts} attempts")
            break
        

# Call the function here
Guess_My_Number()