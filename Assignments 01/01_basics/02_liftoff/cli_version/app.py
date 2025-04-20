import pyttsx3
import pygame
import time

engine = pyttsx3.init()

# 🎤 Adjust Voice Energy Settings
engine.setProperty("rate", 200)  # 🔥 Increase speed (default is around 150)
engine.setProperty("volume", 1.0)  # 🔊 Full volume (range: 0.0 to 1.0)

# 🗣️ Use Female Voice (Optional)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

for i in range(10 ,0,-1):
        print(f"⏳ {i}", end=" ", flush=True)
        engine.say(str(i))
        engine.runAndWait()

print("🔥🚀 Liftoff! 🎉")
engine.say("Liftoff!")
engine.runAndWait()

# ✅ Initialize pygame mixer
pygame.mixer.init()

# ✅ Load and play sound
pygame.mixer.music.load("liftoff.wav")  # Make sure liftoff.wav is in the same folder
pygame.mixer.music.play()

# ✅ Wait for the sound to finish
while pygame.mixer.music.get_busy():
    time.sleep(1)