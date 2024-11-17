def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def km_to_miles(km):
    return km * 0.621371

def unit_converter():
    print("Unit Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Kilometers to Miles")
    choice = input("Choose conversion (1 or 2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius is {fahrenheit} Fahrenheit.")
    elif choice == '2':
        km = float(input("Enter distance in kilometers: "))
        miles = km_to_miles(km)
        print(f"{km} kilometers is {miles} miles.")
    else:
        print("Invalid choice!")

# Run the converter
if __name__ == "__main__":
    unit_converter()