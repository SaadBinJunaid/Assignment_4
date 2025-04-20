c = 299792458

mass = float(input("Enter kilos of mass: "))
energy_in_joules:float = mass * (c ** 2)

print("e = m * C^2...")
print(f"m mass in kilograms  = {mass} kg")
print(f"c speed of light  = {c} m/s")
print(f"e energy_in_joules = {energy_in_joules} J")