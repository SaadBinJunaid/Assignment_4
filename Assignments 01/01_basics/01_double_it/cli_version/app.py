
def double():
    while True:
        user_input = input("Enter a number to double or type exit to quite the program: ")
        if "exit" in user_input:
            print("Exiting program! bye bye")
            break
        
        if user_input.isdigit():
            num = int(user_input)
        
            if num < 100:
                 while num < 100:
                     num *= 2
                     print(num)
            else:
                print("Only less than 100 numbers are allowed.")
        else:
            print("Invalid input. Please enter a number or type exit to quit the program.")
    
# Run the function
double()
