import tkinter as tk
from tkinter import ttk

def meters_to_kilometers():
    meters = float(entry.get())
    kilometers = meters / 1000
    result_label.config(text=f"{meters} meters is equal to {kilometers:.2f} kilometers.")

def kilometers_to_meters():
    kilometers = float(entry.get())
    meters = kilometers * 1000
    result_label.config(text=f"{kilometers} kilometers is equal to {meters:.2f} meters.")

def meters_to_miles():
    meters = float(entry.get())
    miles = meters * 0.000621371
    result_label.config(text=f"{meters} meters is equal to {miles:.2f} miles.")

def miles_to_meters():
    miles = float(entry.get())
    meters = miles / 0.000621371
    result_label.config(text=f"{miles} miles is equal to {meters:.2f} meters.")

def kilometers_to_miles():
    kilometers = float(entry.get())
    miles = kilometers * 0.621371
    result_label.config(text=f"{kilometers} kilometers is equal to {miles:.2f} miles.")

def miles_to_kilometers():
    miles = float(entry.get())
    kilometers = miles / 0.621371
    result_label.config(text=f"{miles} miles is equal to {kilometers:.2f} kilometers.")

def meters_to_feet():
    meters = float(entry.get())
    feet = meters * 3.28084
    result_label.config(text=f"{meters} meters is equal to {feet:.2f} feet.")

def feet_to_meters():
    feet = float(entry.get())
    meters = feet / 3.28084
    result_label.config(text=f"{feet} feet is equal to {meters:.2f} meters.")

def feet_to_inches():
    feet = float(entry.get())
    inches = feet * 12
    result_label.config(text=f"{feet} feet is equal to {inches:.2f} inches.")

def inches_to_feet():
    inches = float(entry.get())
    feet = inches / 12
    result_label.config(text=f"{inches} inches is equal to {feet:.2f} feet.")

# Create the main window
root = tk.Tk()
root.title("Distance Converter")

# Create widgets
method_label = ttk.Label(root, text="Select conversion method:")
method_label.grid(row=0, column=0, padx=5, pady=5)

method_combobox = ttk.Combobox(root, values=[
    "Meters to Kilometers", "Kilometers to Meters", "Meters to Miles", "Miles to Meters",
    "Kilometers to Miles", "Miles to Kilometers", "Meters to Feet", "Feet to Meters",
    "Feet to Inches", "Inches to Feet"
])
method_combobox.grid(row=0, column=1, padx=5, pady=5)

value_label = ttk.Label(root, text="Enter value:")
value_label.grid(row=1, column=0, padx=5, pady=5)

entry = ttk.Entry(root)
entry.grid(row=1, column=1, padx=5, pady=5)

convert_button = ttk.Button(root, text="Convert", command=lambda: eval(method_combobox.get().lower().replace(" ", "_"))())
convert_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
