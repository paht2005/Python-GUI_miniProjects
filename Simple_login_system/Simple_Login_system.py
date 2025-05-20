# copyright [2025] [Phat Nguyen Cong] (Github: https://github.com/paht2005)

import tkinter as tk
from tkinter import messagebox

# Initialize the main window
app = tk.Tk()
app.title("User Authentication")
app.geometry("400x300")
app.config(bg="#e3f2fd")

# Predefined users and passwords
user_data = {
    "admin": "adminpass",
    "guest": "guestpass"
}

# Title label
header = tk.Label(app, text="User Login", font=("Helvetica", 20), bg="#e3f2fd")
header.pack(pady=20)

# Username entry
username_label = tk.Label(app, text="Enter Username:", font=("Helvetica", 12), bg="#e3f2fd")
username_label.pack()
username_input = tk.Entry(app, font=("Helvetica", 12))
username_input.pack(pady=5)

# Password entry
password_label = tk.Label(app, text="Enter Password:", font=("Helvetica", 12), bg="#e3f2fd")
password_label.pack()
password_input = tk.Entry(app, font=("Helvetica", 12), show="*")
password_input.pack(pady=5)

# Function to handle login
def authenticate_user():
    username = username_input.get()
    password = password_input.get()
    if username in user_data and user_data[username] == password:
        messagebox.showinfo("Login Successful", f"Hello, {username}!")
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")

# Function to reset the fields
def reset_fields():
    username_input.delete(0, tk.END)
    password_input.delete(0, tk.END)

# Buttons for actions
login_button = tk.Button(app, text="Login", command=authenticate_user, font=("Helvetica", 12), bg="#81c784", fg="black")
login_button.pack(pady=10)

reset_button = tk.Button(app, text="Reset", command=reset_fields, font=("Helvetica", 12), bg="#f44336", fg="black")
reset_button.pack(pady=5)

exit_button = tk.Button(app, text="Exit", command=app.quit, font=("Helvetica", 12), bg="#78909c", fg="black")
exit_button.pack(pady=10)

# Start the application
app.mainloop()
