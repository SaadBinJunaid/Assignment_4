import re

# Example 1

# def get_user_data():
#     while True:
#         first_Name = input("Enter your First Name: ").strip().capitalize()
#         if re.search(r"[a-zA-Z]", first_Name):
#             break
#         else:
#             print("❌ Invalid input! First Name must contain letters.")

#     while True:
#         last_Name = input("Enter your Last Name: ").strip().capitalize()
#         if re.search(r"[a-zA-Z]", last_Name):
#             break
#         else:
#             print("❌ Invalid input! Last Name must contain letters.")

#     while True:
#         email_address = input("Enter your Email Address: ").strip().lower()
#         if re.search(r"[a-zA-Z]", email_address):
#             if "@" in email_address and "." in email_address:
#                 break
#             else:
#                 print("❌ Invalid input! Email Address must contain @ and .")
#         else:
#             print("❌ Invalid input! Email Address must contain letters.")
            
#     return first_Name,last_Name,email_address

# def print_user_data():
#     first_Name,last_Name,email_address = get_user_data()
#     print(f"('{first_Name}' , '{last_Name}' , '{email_address}')")

    
# print_user_data()









# Example 2


# import re

# data_list =[]
# def get_user_data(first_Name,last_Name,email_address):
    
#     user_data = {
#         "firstName": first_Name,
#         "lastName": last_Name,
#         "email address": email_address,
#         }
#     data_list.append(user_data)

# def add_user_data():
#     while True:
#         first_Name = input("Enter your First Name: ").strip().capitalize()
#         if re.search(r"[a-zA-Z]", first_Name):
#             break
#         else:
#             print("❌ Invalid input! First Name must contain letters.")

#     while True:
#         last_Name = input("Enter your Last Name: ").strip().capitalize()
#         if re.search(r"[a-zA-Z]", last_Name):
#             break
#         else:
#             print("❌ Invalid input! Last Name must contain letters.")

#     while True:
#         email_address = input("Enter your Email Address: ").strip().lower()
#         if re.search(r"[a-zA-Z]", email_address):
#             if "@" in email_address and "." in email_address:
#                 break
#             else:
#                 print("❌ Invalid input! Email Address must contain @ and .")
#         else:
#             print("❌ Invalid input! Email Address must contain letters.")

#     # ✅ FIXED: Now saving the data correctly
#     get_user_data(first_Name ,last_Name ,email_address)


# def search_data():
#     if not data_list:
#         print("No data available")
#     search_term = input("Enter the (FirstName or lastName) to search data: ")
#     matching_data = [data for data in data_list if search_term.lower() in data["firstName"].lower() or search_term.lower() in data["lastName"].lower()]
#     if not matching_data:
#         print("No matching data found")
#         return
#     for index, data in enumerate(matching_data,start=1):
#         print(f"{index}. First Name = {data["firstName"]} Last Name = {data["lastName"]} Email Address = {data["email address"]}")
        
        
# def start_program():
#     while True:
#         print("1. Add User Data")
#         print("2. Search User Data")
#         print("3. Exit")
#         choice = input("Enter your choice: ").strip().lower()
#         if choice in ["1","a","add","ad"]:
#             add_user_data()
#         elif choice in ["2","se","s","search","searh",]:
#             search_data()
#         elif choice in ["3","","e","exit"]:
#             break
        
# start_program()