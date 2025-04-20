# Define the adult age constant (In the U.S., the legal adult age is 18)
ADULT_AGE = 18

def is_adult(age):
    # Check if the age is greater than or equal to ADULT_AGE
    if age >= ADULT_AGE:
        return True  # Person is an adult
    else:
        return False  # Person is not an adult

def check_adult_status():
    # Get user input for the age
    age = int(input("How old is this person?: "))
    
    # Call the is_adult function and print the result
    if is_adult(age):
        print("True 🧑‍🦱")  # The person is an adult
    else:
        print("False 🚫👶")  # The person is not an adult

# Call the function to check adult status
check_adult_status()
