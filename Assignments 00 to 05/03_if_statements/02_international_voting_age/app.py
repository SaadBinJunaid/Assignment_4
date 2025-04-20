# 🧠 Define the voting ages for each country
PETURKSBOUIPO_AGE = 16  # 🗳️ Voting age in Peturksbouipo
STANLAU_AGE = 25       # 🗳️ Voting age in Stanlau
MAYENGUA_AGE = 48      # 🗳️ Voting age in Mayengua

# 🚀 Ask the user for their age
user_prompt = int(input("How old are you? 🎂 Enter your age: "))  # 🧑‍🤝‍🧑 User input for age

# 🧑‍⚖️ Check if the user can vote in any country based on their age
if user_prompt >= PETURKSBOUIPO_AGE and user_prompt < STANLAU_AGE:
    # 💬 User can vote in Peturksbouipo, but not in Stanlau or Mayengua
    print(f"""\n🎉 Your Age Is {user_prompt} Years Old: 
    You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}. 🗳️ 
    But You cannot vote in Stanlau where the voting age is {STANLAU_AGE}. ❌
    And also, You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}. ❌""")

elif user_prompt >= STANLAU_AGE and user_prompt < MAYENGUA_AGE:
    # 💬 User can vote in Stanlau and Peturksbouipo, but not in Mayengua
    print(f"""\n🎉 Your Age Is {user_prompt} Years Old: 
    You can vote in Stanlau where the voting age is {STANLAU_AGE}. 🗳️
    You can also vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}. 🗳️
    But You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}. ❌""")

elif user_prompt >= MAYENGUA_AGE:
    # 💬 User can vote in all three countries
    print(f"""\n🎉 Your Age Is {user_prompt} Years Old: 
    You can vote in Mayengua where the voting age is {MAYENGUA_AGE}. 🗳️
    You can also vote in Stanlau where the voting age is {STANLAU_AGE}. 🗳️
    And you can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}. 🗳️""")

else:
    # 💬 User cannot vote in any country
    print(f"\n🚫 Age {user_prompt}: You cannot vote in any of the countries. ❌")

