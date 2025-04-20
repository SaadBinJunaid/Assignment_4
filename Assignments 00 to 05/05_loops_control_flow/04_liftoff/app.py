import time  # ⏱️ To add delay between countdown numbers

# 🚀 Title: Spaceship Launch Countdown
print("🚀 Preparing for Launch!")
print("🔢 Countdown starting from 10...\n")
time.sleep(1)

# 🔄 Countdown from 10 to 1
for i in range(10, 0, -1):
    print(f"⏳ {i}...")  # 🖨️ Print the countdown number with suspense
    time.sleep(1)  # ⌛ Wait 1 second before the next number

# 🎉 Liftoff!
print("\n🌟 Liftoff! 🚀 The spaceship has launched! 🌌")
