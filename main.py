import math

with open("planets.txt", "r") as file:
    for line in file:
        data = line.strip().split()

        if len(data) < 5:
            line.strip()
            continue

        name = data[0]
        temperature_str = data[2]
        luminosity_str = data[4].strip(",")

        luminosity_str = luminosity_str.replace("x10", "e")

        try:
            temperature = float(temperature_str)
            luminosity = float(luminosity_str)
        except ValueError:
            print(f"Error parsing values for {name}")
            continue

        solar_radius = math.sqrt(luminosity) * (5800 / temperature) ** 2

        if solar_radius <= 10:
            classification = "Dwarf"
        elif 10 < solar_radius < 100:
            classification = "Giant"
        else:
            classification = "Supergiant"

        print(f"{name} has a solar radius of {solar_radius:.2f}, and is classified as a {classification}.")
