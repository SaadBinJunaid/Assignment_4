from hashlib import sha256  # Importing the sha256 hashing function from hashlib library

# # Function to hash the password using SHA256
# def hash_password(password):
#     """
#     Takes in a password and returns the SHA256 hashed value of that password.
#     """
#     # The password is encoded to bytes, and then we apply the SHA256 hash function.
#     # After hashing, we return the hexadecimal representation of the hash.
#     return sha256(password.encode()).hexdigest()


# # Function to check the login credentials
# def login(email, stored_logins, password_to_check):
#     """
#     Checks if the password_to_check matches the stored hash for the given email.
    
#     email: The email of the user.
#     stored_logins: A dictionary that stores emails and their hashed passwords.
#     password_to_check: The password entered by the user that needs to be checked.
    
#     Returns: True if the password matches, False otherwise.
#     """
#     # Check if the email exists in the stored_logins dictionary
#     if email in stored_logins:
#         # Get the stored hashed password for the given email
#         stored_hash = stored_logins[email]
        
#         # Hash the entered password and compare it with the stored hash
#         if stored_hash == hash_password(password_to_check):
#             return True  # Login successful
#         else:
#             return False  # Login failed, password doesn't match the hash
    
#     return False  # If the email doesn't exist in stored_logins, return False


# # Main function to test the login system
# def main():
#     # This is a sample dictionary of stored login information
#     # The key is the email and the value is the hash of the password
#     stored_logins = {
#         "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # hash of "password"
#         "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # hash of "karel"
#         "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # hash of "123456"
#     }

#     # Testing login with correct password
#     print(login("example@gmail.com", stored_logins, "password"))  # Expected output: True
    
#     # Testing login with incorrect password
#     print(login("example@gmail.com", stored_logins, "wrongpassword"))  # Expected output: False
    
#     # Testing login with a different email
#     print(login("code_in_placer@cip.org", stored_logins, "karel"))  # Expected output: True
    
#     # Testing login with a non-existent email
#     print(login("non_existent_email@example.com", stored_logins, "password"))  # Expected output: False



# main()


# example 2

from hashlib import sha256  # Import SHA256 hashing

# 🔐 Hashing function
def convert_password_to_hash(password):
    return sha256(password.encode()).hexdigest()

# 🗂️ Storage dictionary
stored_logins = {}

# 🟩 REGISTRATION
print("\n🔐 Welcome to Registration Page\n")
while True:
    user_email = input("✉️ Enter email to register (or press Enter to stop): ")
    if user_email == "":
        break
    
    user_password = input("🔑 Enter password: ")
    stored_logins[user_email] = convert_password_to_hash(user_password)
    print("✅ You are registered successfully!\n")

# 🟨 LOGIN
print("\n🟨 Welcome to Login Page\n")
while True:
    user_email = input("✉️ Enter email to login (or press Enter to stop): ")
    if user_email == "":
        break

    if user_email in stored_logins:
        # 🌀 Keep asking for password until correct
        while True:
            user_password = input("🔑 Enter password: ")
            if stored_logins[user_email] == convert_password_to_hash(user_password):
                print("✅ You are logged in successfully!\n")
                break  # Exit password retry loop
            else:
                print("🚫 Incorrect password! Please try again.\n")
    else:
        print("🚫 Email not found!\n")
