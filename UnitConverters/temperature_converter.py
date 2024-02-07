import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def convert_temperature():
    from_unit = from_combobox.get()
    to_unit = to_combobox.get()
    temperature = float(entry.get())
    
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = celsius_to_fahrenheit(temperature)
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = fahrenheit_to_celsius(temperature)
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        result = celsius_to_kelvin(temperature)
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        result = kelvin_to_celsius(temperature)
    
    result_label.config(text=f"{temperature} {from_unit} is equal to {result:.2f} {to_unit}.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create widgets
from_label = ttk.Label(root, text="From:")
from_label.grid(row=0, column=0, padx=5, pady=5)

from_combobox = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
from_combobox.grid(row=0, column=1, padx=5, pady=5)
from_combobox.current(0)

to_label = ttk.Label(root, text="To:")
to_label.grid(row=1, column=0, padx=5, pady=5)

to_combobox = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
to_combobox.grid(row=1, column=1, padx=5, pady=5)
to_combobox.current(1)

value_label = ttk.Label(root, text="Enter value:")
value_label.grid(row=2, column=0, padx=5, pady=5)

entry = ttk.Entry(root)
entry.grid(row=2, column=1, padx=5, pady=5)

convert_button = ttk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
