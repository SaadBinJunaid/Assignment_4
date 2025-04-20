import random

# 🎉 Welcome message
print("🎮 Welcome to the High-Low Game!")
print("✨ Test your instincts and beat the computer!")
print("---------------------------------------------")

# 🔁 Main game loop
while True:
    try:
        NUM_ROUNDS = int(input("🔢 Enter how many rounds you want to play: "))
        if NUM_ROUNDS <= 0:
            print("⚠️ Please enter a number greater than 0.")
            continue
    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number.")
        continue

    score = 0  # 🧮 Score starts at 0

    print("\n🎲 Let's begin the game!")
    print("═════════════════════════════════════════════")

    # 🔁 Round loop
    for round_number in range(1, NUM_ROUNDS + 1):
        my_num = random.randint(1, 100)
        computer_num = random.randint(1, 100)

        print(f"\n🔁 Round {round_number} of {NUM_ROUNDS}")
        print("─────────────────────────────────────────────")
        print(f"🧍 Your number is: {my_num}")

        # ❓ Ask for guess
        user_guess = input("🤔 Is your number 'higher' or 'lower' than the computer's?: ").strip().lower()

        # 🔁 Validate input
        while user_guess not in ["higher", "lower"]:
            user_guess = input("⚠️ Invalid input. Please enter 'higher' or 'lower': ").strip().lower()

        # ✅ Compare and check result
        if user_guess == "higher" and my_num > computer_num:
            print("✅ You are correct! 🎉 Your number is HIGHER!")
            score += 1
        elif user_guess == "lower" and my_num < computer_num:
            print("✅ You are correct! 🎉 Your number is LOWER!")
            score += 1
        else:
            print("❌ Oops! That's incorrect.")

        # 🤖 Reveal computer's number
        print(f"🖥️ The computer's number was: {computer_num}")
        print(f"📊 Your current score: {score}/{round_number}")
        print("═════════════════════════════════════════════")


    # 🏁 Game Over
    print("\n🏁 The game has ended!")
    print("📣 Here are your final results:")
    print("─────────────────────────────────────────────")
    print(f"🏆 Final Score: {score} out of {NUM_ROUNDS}")

    # 💬 Final message
    if score == NUM_ROUNDS:
        print("🌟 Incredible! You played perfectly! 🥇")
    elif score >= NUM_ROUNDS // 2:
        print("👍 Great job! You won more than half the rounds! 🎯")
    else:
        print("🙁 Better luck next time! Keep practicing! 💪")

    print("─────────────────────────────────────────────")

    # 🔁 Play again option
    play_again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\n👋 Thanks for playing! See you next time! ✨")
        break
