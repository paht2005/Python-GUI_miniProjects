# copyright [2025] [Phat Nguyen Cong] (Github: https://github.com/paht2005)

# Objective: Build a GUI-based Personal Expense Tracker App that allows users to:

# - Add new expenses with category, amount, and description.
# - Display the history of expenses in a Listbox.
# - Remove selected expenses from the list.
# - Save and load expenses from a CSV file for data persistence.
# - Calculate and display the total of all expenses.

# Core Features:
# - User-friendly GUI using Tkinter widgets for input and display.
# - Input validation to ensure correct data entry (e.g., numeric validation).
# - Persistent data storage by saving and loading expenses from a CSV file.
# - Real-time calculation of total expenses.
# - Ability to delete specific expenses from the displayed list.

# Key GUI Components:
# - Entry Widgets: For entering the amount and description of the expense.
# - Dropdown (Combobox): For selecting an expense category (e.g., Food, Rent).
# - Listbox: To display the added expenses with category, amount, and description.
# - Labels: To dynamically show information such as the total expenses.
# - Buttons: For adding new expenses, removing selected expenses, clearing inputs, and clearing all data.

import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os


# Expense Tracker App

# File for storing expenses
EXPENSE_FILE = "expenses_data.csv"

# Create Main Application Window
app_window = tk.Tk()
app_window.title("Personal Expense Tracker")
app_window.geometry("600x600")
app_window.configure(bg="#f0f4c3")

# List to hold all expenses
expense_records = []

# Load Existing Expenses from CSV File
def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            for record in reader:
                expense_records.append(record)
                expenses_display.insert(tk.END, f"{record[0]} | ${record[1]} | {record[2]}")

# Save Expenses to CSV
def save_expenses():
    with open(EXPENSE_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for record in expense_records:
            writer.writerow(record)

# Add a New Expense
def add_expense():
    category = category_selection.get()
    amount = amount_input.get()
    description = description_input.get()
    
    if not amount.isdigit() or not category or not description:
        messagebox.showerror("Invalid Input", "Please ensure all fields are valid.")
        return
    
    expense_records.append([category, amount, description])
    expenses_display.insert(tk.END, f"{category} | ${amount} | {description}")
    update_total()
    clear_inputs()
    save_expenses()

# Remove Selected Expense
def remove_expense():
    selected = expenses_display.curselection()
    if not selected:
        messagebox.showerror("Error", "Select an expense to delete.")
        return
    
    index = selected[0]
    del expense_records[index]
    expenses_display.delete(index)
    update_total()
    save_expenses()

# Clear All Input Fields
def clear_inputs():
    category_selection.set("Select Category")
    amount_input.delete(0, tk.END)
    description_input.delete(0, tk.END)

# Update Total Expenses
def update_total():
    total = sum(float(record[1]) for record in expense_records)
    total_label.config(text=f"Total Expenses: ${total:.2f}")

# Clear All Expenses
def clear_all_expenses():
    if messagebox.askyesno("Confirm", "Do you want to delete all expenses?"):
        expense_records.clear()
        expenses_display.delete(0, tk.END)
        update_total()
        save_expenses()

# --- GUI Layout ---

# Header Title
header_label = tk.Label(app_window, text="Expense Tracker", font=("Arial", 24), bg="#f0f4c3")
header_label.pack(pady=10)

# Expense Entry Frame
entry_frame = tk.Frame(app_window, bg="#f0f4c3")
entry_frame.pack(pady=10)

# Category Dropdown
category_label = tk.Label(entry_frame, text="Category:", font=("Arial", 12), bg="#f0f4c3")
category_label.grid(row=0, column=0, padx=5, pady=5)
category_selection = tk.StringVar(value="Select Category")
category_dropdown = ttk.Combobox(entry_frame, textvariable=category_selection, values=["Food", "Transport", "Rent", "Utilities", "Miscellaneous"])
category_dropdown.grid(row=0, column=1, padx=5, pady=5)

# Amount Entry
amount_label = tk.Label(entry_frame, text="Amount ($):", font=("Arial", 12), bg="#f0f4c3")
amount_label.grid(row=1, column=0, padx=5, pady=5)
amount_input = tk.Entry(entry_frame, font=("Arial", 12))
amount_input.grid(row=1, column=1, padx=5, pady=5)

# Description Entry
description_label = tk.Label(entry_frame, text="Description:", font=("Arial", 12), bg="#f0f4c3")
description_label.grid(row=2, column=0, padx=5, pady=5)
description_input = tk.Entry(entry_frame, font=("Arial", 12))
description_input.grid(row=2, column=1, padx=5, pady=5)

# Control Buttons
button_frame = tk.Frame(app_window, bg="#f0f4c3")
button_frame.pack(pady=10)

add_btn = tk.Button(button_frame, text="Add Expense", command=add_expense, bg="#4CAF50", fg="black")
add_btn.grid(row=0, column=0, padx=5)

remove_btn = tk.Button(button_frame, text="Remove Expense", command=remove_expense, bg="#F44336", fg="black")
remove_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(button_frame, text="Clear All", command=clear_all_expenses, bg="#607D8B", fg="black")
clear_btn.grid(row=0, column=2, padx=5)

# Expense List Display with Scrollbar
display_frame = tk.Frame(app_window)
display_frame.pack(pady=10)

scrollbar = tk.Scrollbar(display_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

expenses_display = tk.Listbox(display_frame, width=50, height=15, yscrollcommand=scrollbar.set, font=("Arial", 12))
expenses_display.pack()

scrollbar.config(command=expenses_display.yview)

# Total Expense Label
total_label = tk.Label(app_window, text="Total Expenses: $0.00", font=("Arial", 14), bg="#f0f4c3")
total_label.pack(pady=10)

# Load Existing Expenses
load_expenses()
update_total()

# Exit Button
exit_btn = tk.Button(app_window, text="Exit", command=app_window.quit, bg="#D32F2F", fg="black")
exit_btn.pack(pady=10)

# Run Application
app_window.mainloop()
