import tkinter as tk
from tkinter import ttk


# Conversion functions
def convert_baking():
    from_unit = from_combobox.get()
    to_unit = to_combobox.get()
    ingredient = ingredient_combobox.get()
    amount = float(entry.get())

    result = 0

    if ingredient == "Flour":
        if from_unit == "Cup":
            if to_unit == "Grams":
                result = amount * 120
            elif to_unit == "Ounces":
                result = amount * 4.23
        elif from_unit == "Grams":
            if to_unit == "Cup":
                result = amount / 120
            elif to_unit == "Ounces":
                result = amount / 28.35
        elif from_unit == "Ounces":
            if to_unit == "Cup":
                result = amount / 4.23
            elif to_unit == "Grams":
                result = amount * 28.35
    elif ingredient == "Sugar":
        if from_unit == "Cup":
            if to_unit == "Grams":
                result = amount * 200
            elif to_unit == "Ounces":
                result = amount * 7.05
        elif from_unit == "Grams":
            if to_unit == "Cup":
                result = amount / 200
            elif to_unit == "Ounces":
                result = amount / 28.35
        elif from_unit == "Ounces":
            if to_unit == "Cup":
                result = amount / 7.05
            elif to_unit == "Grams":
                result = amount * 28.35
    elif ingredient == "Butter":
        if from_unit == "Cup":
            if to_unit == "Grams":
                result = amount * 227
            elif to_unit == "Ounces":
                result = amount * 8
        elif from_unit == "Grams":
            if to_unit == "Cup":
                result = amount / 227
            elif to_unit == "Ounces":
                result = amount / 28.35
        elif from_unit == "Ounces":
            if to_unit == "Cup":
                result = amount / 8
            elif to_unit == "Grams":
                result = amount * 28.35
    elif ingredient == "Milk":
        if from_unit == "Cup":
            if to_unit == "Grams":
                result = amount * 240
            elif to_unit == "Ounces":
                result = amount * 8.45
        elif from_unit == "Grams":
            if to_unit == "Cup":
                result = amount / 240
            elif to_unit == "Ounces":
                result = amount / 28.35
        elif from_unit == "Ounces":
            if to_unit == "Cup":
                result = amount / 8.45
            elif to_unit == "Grams":
                result = amount * 28.35

    result_label.config(text=f"Result: {result:.2f} {to_unit}")


# Create the main window
root = tk.Tk()
root.title("Baking Converter")

# Create widgets
entry_label = ttk.Label(root, text="Enter amount:")
entry_label.grid(row=0, column=0, padx=5, pady=5)

entry = ttk.Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)

ingredient_label = ttk.Label(root, text="Select ingredient:")
ingredient_label.grid(row=1, column=0, padx=5, pady=5)

ingredient_combobox = ttk.Combobox(root, values=["Flour", "Sugar", "Butter", "Milk"])
ingredient_combobox.grid(row=1, column=1, padx=5, pady=5)
ingredient_combobox.current(0)

from_label = ttk.Label(root, text="From:")
from_label.grid(row=2, column=0, padx=5, pady=5)

from_combobox = ttk.Combobox(root, values=["Cup", "Grams", "Ounces"])
from_combobox.grid(row=2, column=1, padx=5, pady=5)
from_combobox.current(0)

to_label = ttk.Label(root, text="To:")
to_label.grid(row=3, column=0, padx=5, pady=5)

to_combobox = ttk.Combobox(root, values=["Cup", "Grams", "Ounces"])
to_combobox.grid(row=3, column=1, padx=5, pady=5)
to_combobox.current(1)

convert_button = ttk.Button(root, text="Convert", command=convert_baking)
convert_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

result_label = ttk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
