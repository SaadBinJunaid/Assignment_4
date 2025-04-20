# # 🎢 Welcome message and explanation
print("🎡 Welcome to the FunLand Amusement Park! 🎠")
print("✨ Before you hop on the amazing rollercoaster ride... 🎢")
print("📏 We just need to check if you're tall enough to ride safely. Let's find out!\n")

# 🎢 Minimum height required to ride the rollercoaster
MINIMUM_HEIGHT = 50  # height in any unit (like cm, inches, etc.)

# 🧍 Ask the user how tall they are
user_height = int(input("📏 How tall are you? (in cm or your preferred unit): "))

# 🎯 Check if the user is tall enough to ride
if user_height >= MINIMUM_HEIGHT:
    # 🥳 User is tall enough!
    print("🎉 Woohoo! You're tall enough to ride the rollercoaster! Enjoy the thrill! 🎢")
else:
    # 😔 User is not tall enough yet
    print("😢 Aww! You're not tall enough to ride yet, but maybe next year! 💪 Keep growing!")
