def fruits_in_stock(fruits):
    # Dictionary containing fruit stock values 🍎🍌🍇🍓🍍🍒
    fruits = {
        "apple": 5,
        "banana": 10,
        "orange": 7,
        "grape": 15,
        "mango": 20,
        "kiwi": 0,  
        "pear": 1000, 
        "strawberry": 50,  
        "pineapple": 30,  
        "watermelon": 0,  
        "cherry": 100,  
        "blueberry": 200,  
        "peach": 12, 
    }
    return fruits

def check_in_stock():
    # Ask user to enter the fruit name 🥭🍍🍎🍊
    name = input("🍊 Enter a fruit name: ")
    
    # Check the stock of the fruit entered by the user 🍎
    fruits = fruits_in_stock(None)  # Call the fruits_in_stock function
    if name in fruits:  # If fruit is in the stock
        quantity = fruits[name]
        if quantity > 0:
            print(f"🍏 {name} is in stock! 🍒 Here is how many: {quantity} 🍇")
        else:
            print(f"🚫 Sorry, {name} is out of stock. 😞")
    elif name in ["all","a","al"]:
        for index, (A_name , quantity) in enumerate(fruits.items(),start=1):
            print(f"{index}) 🍓 {A_name.capitalize()} with quantity: {quantity} 🍇")
    else:
        # If the fruit is not found in the stock 🍑
        print(f"🍓 This fruit is not in stock. 🚫")

check_in_stock()
