import tkinter as tk


def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

def update_task():
    selected = listbox.curselection()
    if selected:
        updated_task = task_entry.get()
        listbox.delete(selected)
        listbox.insert(selected, updated_task)
        task_entry.delete(0, tk.END)

def save_tasks():
    with open('tasks.txt', 'w') as file:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + '\n')

root = tk.Tk()
root.title("Todo List")

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack()

save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()


root.mainloop()
