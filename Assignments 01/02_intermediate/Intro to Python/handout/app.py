all_planets = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14,
}

while True:
    print("\n🌍 Here is the list of planets you can check your weight on:")
    for planet in all_planets.keys():
        print(f"👉 {planet}")
    
    # ✅ VALIDATE EARTH WEIGHT
    while True:
        Earth_weight = input("\nEnter your Earth weight (in numbers): ").strip()
        
        if Earth_weight == "":
            print("👋 Bye bye! Stay light in space 🚀")
            exit()  # Exit the entire program immediately
        
        try:
            Earth_weight = float(Earth_weight)
            if Earth_weight <= 0:
                print("⚠️ Please enter a positive number.")
                continue
            break  # Valid input, break the loop
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

    # ✅ VALIDATE PLANET NAME
    while True:
        planet = input("Enter the planet name to check your weight: ").strip().capitalize()
        
        if planet.isdigit():
            print("❌ Please enter a planet name, not a number.")
            continue

        if planet not in all_planets:
            print("⚠️ Invalid planet name. Please choose from the list.")
            continue
        break  # Valid planet name

    # ✅ CALCULATE & DISPLAY WEIGHT
    converted_weight = round(Earth_weight * all_planets[planet], 2)
    print(f"\n🪐 Your weight on {planet} is {converted_weight} kg.")

    # ✅ ASK TO CONTINUE
    cont = input("Do you want to check another planet? (yes/no): ").strip().lower()
    if cont != "yes":
        print("👋 Bye bye! Stay light in space 🚀")
        break
