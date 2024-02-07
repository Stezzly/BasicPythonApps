import tkinter as tk
from tkinter import ttk


# Update options based on conversion type
def update_options(*args):
    conversion_type = conversion_combobox.get()
    if conversion_type == "Imperial to Imperial":
        from_combobox.config(values=["Pound (lb)", "Ounce (oz)"])
        to_combobox.config(values=["Pound (lb)", "Ounce (oz)"])
    elif conversion_type == "Imperial to Metric":
        from_combobox.config(values=["Pound (lb)", "Ounce (oz)"])
        to_combobox.config(values=["Kilogram (kg)", "Gram (g)"])
    elif conversion_type == "Metric to Imperial":
        from_combobox.config(values=["Kilogram (kg)", "Gram (g)"])
        to_combobox.config(values=["Pound (lb)", "Ounce (oz)"])
    elif conversion_type == "Metric to Metric":
        from_combobox.config(values=["Pound (lb)", "Ounce (oz)"])
        to_combobox.config(values=["Pound (lb)", "Ounce (oz)"])


# Conversion functions
def convert_weight():
    from_unit = from_combobox.get()
    to_unit = to_combobox.get()
    conversion_type = conversion_combobox.get()
    weight = float(entry.get())

    result = 0

    if conversion_type == "Imperial to Imperial":
        if from_unit == "Pound (lb)":
            if to_unit == "Pound (lb)":
                result = weight
            elif to_unit == "Ounce (oz)":
                result = weight * 16
        elif from_unit == "Ounce (oz)":
            if to_unit == "Pound (lb)":
                result = weight / 16
            elif to_unit == "Ounce (oz)":
                result = weight
    elif conversion_type == "Imperial to Metric":
        if from_unit == "Pound (lb)":
            if to_unit == "Kilogram (kg)":
                result = weight * 0.453592
            elif to_unit == "Gram (g)":
                result = weight * 453.592
        elif from_unit == "Ounce (oz)":
            if to_unit == "Kilogram (kg)":
                result = weight * 0.0283495
            elif to_unit == "Gram (g)":
                result = weight * 28.3495
    elif conversion_type == "Metric to Imperial":
        if from_unit == "Kilogram (kg)":
            if to_unit == "Pound (lb)":
                result = weight * 2.20462
        elif from_unit == "Gram (g)":
            if to_unit == "Pound (lb)":
                result = weight * 0.00220462
    elif conversion_type == "Metric to Metric":
        if from_unit == "Kilogram (kg)" and to_unit == "Gram (g)":
            result = weight * 1000
        elif from_unit == "Gram (g)" and to_unit == "Kilogram (kg)":
            result = weight / 1000

    result_label.config(text=f"Result: {result:.2f} {to_unit}")


# Create the main window
root = tk.Tk()
root.title("Weight Converter")

# Create widgets
entry_label = ttk.Label(root, text="Enter weight:")
entry_label.grid(row=0, column=0, padx=5, pady=5)

entry = ttk.Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)

from_label = ttk.Label(root, text="From:")
from_label.grid(row=1, column=0, padx=5, pady=5)

from_combobox = ttk.Combobox(root)
from_combobox.grid(row=1, column=1, padx=5, pady=5)

to_label = ttk.Label(root, text="To:")
to_label.grid(row=2, column=0, padx=5, pady=5)

to_combobox = ttk.Combobox(root)
to_combobox.grid(row=2, column=1, padx=5, pady=5)

conversion_label = ttk.Label(root, text="Conversion type:")
conversion_label.grid(row=3, column=0, padx=5, pady=5)

conversion_combobox = ttk.Combobox(root, values=["Imperial to Imperial", "Imperial to Metric", "Metric to Imperial",
                                                 "Metric to Metric"])
conversion_combobox.grid(row=3, column=1, padx=5, pady=5)
conversion_combobox.current(0)

# Bind update_options function to the conversion_combobox
conversion_combobox.bind("<<ComboboxSelected>>", update_options)

convert_button = ttk.Button(root, text="Convert", command=convert_weight)
convert_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

result_label = ttk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
