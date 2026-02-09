# main file to run for the console
from conversions.temperature import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius
)
from conversions.length import (
    meters_to_kilometers,
    kilometers_to_meters,
    meters_to_feet,
    feet_to_meters
)


def temperature_menu():
    print("\nTemperature conversions:")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")

    choice = input("Choose an option: ")
    value = float(input("Enter value: "))

    if choice == "1":
        print(f"Result: {celsius_to_fahrenheit(value):.2f} °F")
    elif choice == "2":
        print(f"Result: {fahrenheit_to_celsius(value):.2f} °C")
    elif choice == "3":
        print(f"Result: {celsius_to_kelvin(value):.2f} K")
    elif choice == "4":
        print(f"Result: {kelvin_to_celsius(value):.2f} °C")
    else:
        print("Invalid option")


def length_menu():
    print("\nLength conversions:")
    print("1. Meters → Kilometers")
    print("2. Kilometers → Meters")
    print("3. Meters → Feet")
    print("4. Feet → Meters")

    choice = input("Choose an option: ")
    value = float(input("Enter value: "))

    if choice == "1":
        print(f"Result: {meters_to_kilometers(value):.4f} km")
    elif choice == "2":
        print(f"Result: {kilometers_to_meters(value):.2f} m")
    elif choice == "3":
        print(f"Result: {meters_to_feet(value):.2f} ft")
    elif choice == "4":
        print(f"Result: {feet_to_meters(value):.2f} m")
    else:
        print("Invalid option")


def main():
    while True:
        print("\n=== Conversion Tool ===")
        print("1. Temperature")
        print("2. Length")
        print("0. Exit")

        choice = input("Choose a category: ")

        if choice == "1":
            temperature_menu()
        elif choice == "2":
            length_menu()
        elif choice == "0":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
