import tkinter as tk
from tkinter import ttk


# Conversion functions
def convert_volume():
    from_unit = from_combobox.get()
    to_unit = to_combobox.get()
    volume = float(entry.get())

    result = 0

    if from_unit == "Milliliter (mL)":
        if to_unit == "Milliliter (mL)":
            result = volume
        elif to_unit == "Liter (L)":
            result = volume / 1000
        elif to_unit == "Cubic Centimeter (cm^3)":
            result = volume
        elif to_unit == "Cubic Meter (m^3)":
            result = volume / 1000000
        elif to_unit == "Quart (qt)":
            result = volume * 0.00105669
        elif to_unit == "Ounce (oz)":
            result = volume * 0.033814
    elif from_unit == "Liter (L)":
        if to_unit == "Milliliter (mL)":
            result = volume * 1000
        elif to_unit == "Liter (L)":
            result = volume
        elif to_unit == "Cubic Centimeter (cm^3)":
            result = volume * 1000
        elif to_unit == "Cubic Meter (m^3)":
            result = volume / 1000
        elif to_unit == "Quart (qt)":
            result = volume * 1.05669
        elif to_unit == "Ounce (oz)":
            result = volume * 33.814
    elif from_unit == "Cubic Centimeter (cm^3)":
        if to_unit == "Milliliter (mL)":
            result = volume
        elif to_unit == "Liter (L)":
            result = volume / 1000
        elif to_unit == "Cubic Centimeter (cm^3)":
            result = volume
        elif to_unit == "Cubic Meter (m^3)":
            result = volume / 1000000
        elif to_unit == "Quart (qt)":
            result = volume * 0.00105669
        elif to_unit == "Ounce (oz)":
            result = volume * 0.033814
    elif from_unit == "Cubic Meter (m^3)":
        if to_unit == "Milliliter (mL)":
            result = volume * 1000000
        elif to_unit == "Liter (L)":
            result = volume * 1000
        elif to_unit == "Cubic Centimeter (cm^3)":
            result = volume * 1000000
        elif to_unit == "Cubic Meter (m^3)":
            result = volume
        elif to_unit == "Quart (qt)":
            result = volume * 1056.69
        elif to_unit == "Ounce (oz)":
            result = volume * 33814
    elif from_unit == "Quart (qt)":
        if to_unit == "Milliliter (mL)":
            result = volume * 946.353
        elif to_unit == "Liter (L)":
            result = volume * 0.946353
        elif to_unit == "Cubic Centimeter (cm^3)":
            result = volume * 946.353
        elif to_unit == "Cubic Meter (m^3)":
            result = volume * 0.000946353
        elif to_unit == "Quart (qt)":
            result = volume
        elif to_unit == "Ounce (oz)":
            result = volume * 32
    elif from_unit == "Ounce (oz)":
        if to_unit == "Milliliter (mL)":
            result = volume * 29.5735
        elif to_unit == "Liter (L)":
            result = volume * 0.0295735
        elif to_unit == "Cubic Centimeter (cm^3)":
            result = volume * 29.5735
        elif to_unit == "Cubic Meter (m^3)":
            result = volume * 2.95735e-5
        elif to_unit == "Quart (qt)":
            result = volume * 0.03125
        elif to_unit == "Ounce (oz)":
            result = volume

    result_label.config(text=f"Result: {result:.2f} {to_unit}")


# Create the main window
root = tk.Tk()
root.title("Volume Converter")

# Create widgets
entry_label = ttk.Label(root, text="Enter volume:")
entry_label.grid(row=0, column=0, padx=5, pady=5)

entry = ttk.Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)

from_label = ttk.Label(root, text="From:")
from_label.grid(row=1, column=0, padx=5, pady=5)

from_combobox = ttk.Combobox(root,
                             values=["Milliliter (mL)", "Liter (L)", "Cubic Centimeter (cm^3)", "Cubic Meter (m^3)",
                                     "Quart (qt)", "Ounce (oz)"])
from_combobox.grid(row=1, column=1, padx=5, pady=5)
from_combobox.current(0)

to_label = ttk.Label(root, text="To:")
to_label.grid(row=2, column=0, padx=5, pady=5)

to_combobox = ttk.Combobox(root, values=["Milliliter (mL)", "Liter (L)", "Cubic Centimeter (cm^3)", "Cubic Meter (m^3)",
                                         "Quart (qt)", "Ounce (oz)"])
to_combobox.grid(row=2, column=1, padx=5, pady=5)
to_combobox.current(1)

convert_button = ttk.Button(root, text="Convert", command=convert_volume)
convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
