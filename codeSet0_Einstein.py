SPEED_OF_LIGHT = 300000000

def calculate_energy(mass):
    return int(mass) * SPEED_OF_LIGHT ** 2

def main():
    mass = input("Enter the mass of the object in kilograms: ")
    energy = calculate_energy(mass)
    print(f"The energy equivalent of the mass is: {energy} joules")

main()