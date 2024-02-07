import tkinter as tk
from tkinter import messagebox

def save_recipe():
    recipe_name = recipe_name_entry.get()
    ingredients = ingredients_text.get("1.0", "end-1c")
    instructions = instructions_text.get("1.0", "end-1c")

    if recipe_name.strip() == "" or ingredients.strip() == "" or instructions.strip() == "":
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    with open(f"{recipe_name}.txt", "w") as file:
        file.write(f"Recipe Name: {recipe_name}\n\n")
        file.write("Ingredients:\n")
        file.write(ingredients + "\n\n")
        file.write("Instructions:\n")
        file.write(instructions)

    messagebox.showinfo("Success", "Recipe saved successfully.")

def clear_fields():
    recipe_name_entry.delete(0, "end")
    ingredients_text.delete("1.0", "end")
    instructions_text.delete("1.0", "end")

# Create the main window
root = tk.Tk()
root.title("Baking Recipe Creator")

# Create labels
tk.Label(root, text="Recipe Name:").grid(row=0, column=0, sticky="w")
tk.Label(root, text="Ingredients:").grid(row=1, column=0, sticky="w")
tk.Label(root, text="Instructions:").grid(row=2, column=0, sticky="w")

# Create entry for recipe name
recipe_name_entry = tk.Entry(root)
recipe_name_entry.grid(row=0, column=1, padx=5, pady=5)

# Create text boxes for ingredients and instructions
ingredients_text = tk.Text(root, height=5, width=40)
ingredients_text.grid(row=1, column=1, padx=5, pady=5)

instructions_text = tk.Text(root, height=10, width=40)
instructions_text.grid(row=2, column=1, padx=5, pady=5)

# Create buttons for saving and clearing fields
save_button = tk.Button(root, text="Save Recipe", command=save_recipe)
save_button.grid(row=3, column=0, pady=10)

clear_button = tk.Button(root, text="Clear Fields", command=clear_fields)
clear_button.grid(row=3, column=1, pady=10)

root.mainloop()
