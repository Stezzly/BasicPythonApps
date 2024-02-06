def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius



# Print the fucntions
celsius_input = 20
fahrenheit_output = celsius_to_fahrenheit(celsius_input)
print(f"{celsius_input} degrees Celsius is equal to {fahrenheit_output:.2f} degrees Fahrenheit.")

fahrenheit_input = 68
celsius_output = fahrenheit_to_celsius(fahrenheit_input)
print(f"{fahrenheit_input} degrees Fahrenheit is equal to {celsius_output:.2f} degrees Celsius.")



celsius_input = 20
kelvin_output = celsius_to_kelvin(celsius_input)
print(f"{celsius_input} degrees Celsius is equal to {kelvin_output:.2f} Kelvin.")

kelvin_input = 293.15
celsius_output = kelvin_to_celsius(kelvin_input)
print(f"{kelvin_input} Kelvin is equal to {celsius_output:.2f} degrees Celsius.")
