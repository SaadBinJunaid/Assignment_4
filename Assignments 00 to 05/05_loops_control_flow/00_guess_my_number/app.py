import random  # Importing random module to generate random numbers

def main():
    print("🎯" * 15)
    print("     WELCOME TO GUESS MY NUMBER GAME!")
    print("🎯" * 15)
    print("\n💡 I'm thinking of a number between 1 and 100.")
    print("🤫 Can you guess what it is?\n")

    # Start the first game by generating a secret number
    random_number = random.randint(1, 100)
    attempts = 0  # Track number of attempts

    # Ask the user to start guessing
    user_guess = input("👉 Enter your guess (or press Enter to quit): ")

    # Game loop
    while True:
        if user_guess == "":
            print("👋 Goodbye! Thanks for playing! Come back soon.")
            break

        # Convert input to integer
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("⚠️ Please enter a valid number!")
            user_guess = input("👉 Enter your guess again: ")
            continue

        # Increment attempt counter
        attempts += 1

        # Check if the guess is in valid range
        if user_guess < 1 or user_guess > 100:
            print("🚫 Please enter a number between 1 and 100.")
        elif user_guess > random_number:
            print("📉 Too high! Try a smaller number.")
        elif user_guess < random_number:
            print("📈 Too low! Try a larger number.")
        else:
            print(f"\n🎉 Congrats! You guessed it right: {random_number}")
            print(f"🧮 You found the number in {attempts} attempts.")
            print("\n🔁 Starting a new round...\n")
            # Reset game
            random_number = random.randint(1, 100)
            attempts = 0  # Reset attempts for new round

        # Ask again
        user_guess = input("👉 Enter a new guess (or press Enter to quit): ")

# Required to run the program
if __name__ == '__main__':
    main()
