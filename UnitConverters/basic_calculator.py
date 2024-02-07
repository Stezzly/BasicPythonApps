import tkinter as tk
from tkinter import ttk


def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_combobox.get()

    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            result = "Error: Division by zero"
        else:
            result = num1 / num2

    result_label.config(text=f"Result: {result}")


# Create the main window
root = tk.Tk()
root.title("Basic Calculator")

# Create widgets
entry1_label = ttk.Label(root, text="Number 1:")
entry1_label.grid(row=0, column=0, padx=5, pady=5)

entry1 = ttk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

entry2_label = ttk.Label(root, text="Number 2:")
entry2_label.grid(row=1, column=0, padx=5, pady=5)

entry2 = ttk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

operation_label = ttk.Label(root, text="Operation:")
operation_label.grid(row=2, column=0, padx=5, pady=5)

operation_combobox = ttk.Combobox(root, values=["Addition", "Subtraction", "Multiplication", "Division"])
operation_combobox.grid(row=2, column=1, padx=5, pady=5)
operation_combobox.current(0)

calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
