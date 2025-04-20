# Dictionary containing fruit names as keys and their respective prices as values
fruits = {
    "apple": 2.5,
    "banana": 1.5,
    "orange": 3.0,
    "grape": 2.0,
    "jackfruit": 3.5,
    "kiwi": 1.2,
    "rambutan": 4.5,
    "mango": 3.0
}

# Variable to store the total cost of the fruits the user buys
total_fruits_cost = 0

# Starting message for user
print("Welcome to the Fruit Shop! 🍎🍌🍊")

# Loop through each fruit in the dictionary
for fruit_name in fruits:
    price = fruits[fruit_name]  # Get the price of the current fruit
    # Ask the user how many of the current fruit they want to buy
    fruits_to_buy = input(f"How many {fruit_name}s do you want to buy? (Enter a number or press Enter to stop buying): ")

    # If the user presses Enter without providing an input, stop the loop
    if fruits_to_buy == "":
        print("You have chosen to stop buying. Thank you for visiting!")
        break
    else:
        try:
            # Convert the user input to an integer and calculate the cost for the current fruit
            fruits_to_buy = int(fruits_to_buy)
            total_fruits_cost += price * fruits_to_buy  # Update the total cost
            print(f"Added {fruits_to_buy} {fruit_name}(s) to your basket. 🍎 Total so far: ${total_fruits_cost}")
        except ValueError:
            # Handle the case where the user enters something other than a number
            print("Oops! Please enter a valid number.")

# Display the total amount of all the fruits the user decided to buy
print(f"\n🎉 Here is your total amount for the fruits you selected is ${total_fruits_cost}.")
print("Thanks for shopping with us! 🍏🍌🍇")
