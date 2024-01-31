def main():
    # Ask for mass
    mass = int(input("Mass of the object: "))
    const = int(300000000)
    # convert mass to energy
    energy = mass * (const*const)
    print(f"Energy: {energy}")


main()
