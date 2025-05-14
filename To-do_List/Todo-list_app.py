import tkinter as tk
from tkinter import messagebox

# Main Window Setup
app = tk.Tk()
app.title("Simple To-Do App")
app.geometry("420x550")
app.config(bg="#f8f9fa")

# Global Task List
task_items = []

# Task Management Functions
def add_task_to_list():
    task = task_entry.get()
    if task.strip():
        task_items.append(task)
        refresh_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a task before adding.")

def remove_selected_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_items.pop(selected_index)
        refresh_task_list()
    except IndexError:
        messagebox.showerror("Error", "No task selected to delete.")

def clear_all_tasks():
    task_items.clear()
    refresh_task_list()

def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for task in task_items:
        task_listbox.insert(tk.END, task)

# UI Elements
header = tk.Label(app, text="To-Do List", font=("Arial", 22, "bold"), bg="#f8f9fa")
header.pack(pady=15)

# Task Entry
task_entry = tk.Entry(app, font=("Arial", 14), width=35)
task_entry.pack(pady=10)

# Buttons for Task Operations
button_frame = tk.Frame(app, bg="#f8f9fa")
button_frame.pack(pady=15)

add_button = tk.Button(button_frame, text="Add Task", command=add_task_to_list, font=("Arial", 12), bg="#4CAF50", fg="white")
add_button.grid(row=0, column=0, padx=8)

remove_button = tk.Button(button_frame, text="Remove Task", command=remove_selected_task, font=("Arial", 12), bg="#F44336", fg="white")
remove_button.grid(row=0, column=1, padx=8)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_all_tasks, font=("Arial", 12), bg="#607D8B", fg="white")
clear_button.grid(row=0, column=2, padx=8)

# Task Listbox with Scrollbar
listbox_frame = tk.Frame(app)
listbox_frame.pack(pady=15)

scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(listbox_frame, width=50, height=15, yscrollcommand=scrollbar.set, font=("Arial", 12))
task_listbox.pack()

scrollbar.config(command=task_listbox.yview)

# Exit Button
exit_button = tk.Button(app, text="Exit", command=app.quit, font=("Arial", 12), bg="#9E9E9E", fg="white")
exit_button.pack(pady=10)

# Run the Application
app.mainloop()
