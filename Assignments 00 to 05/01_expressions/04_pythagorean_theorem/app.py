import math

AB:float = float(input("Enter the length of AB: "))
AC:float = float(input("Enter the length of AC: "))

BC:float = math.sqrt(AB**2 + AC**2)
print(f"The length of BC (the hypotenuse) is: {BC:.2f}")

