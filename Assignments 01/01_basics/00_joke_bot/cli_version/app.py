import pyjokes

def joke_bot():
    while True:
        prompt = input("What type of joke do you want? (All/Neutral/Chuck) or type 'exit' to quit: ").lower().strip()
        valid_categories = ["all", "neutral", "chuck"]

        if prompt in valid_categories:
            joke = pyjokes.get_joke(category=prompt)
            print(joke)
        elif prompt == "exit":
            print("bye bye")
            break
        else: 
            print("Sorry, I only tell jokes from the given categories.")

joke_bot()
