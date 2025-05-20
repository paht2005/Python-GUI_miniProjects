# copyright [2025] [Phat Nguyen Cong] (Github: https://github.com/paht2005)

import tkinter as tk
from datetime import datetime

# Initial theme colors
LIGHT_THEME = {
    "bg": "#e6f2ff",
    "fg": "#000000",
    "button_bg": "#cce5ff",
    "button_fg": "#000000"
}

DARK_THEME = {
    "bg": "#2e2e2e",
    "fg": "#ffffff",
    "button_bg": "#4d4d4d",
    "button_fg": "#ffffff"
}

# Create main application window
app = tk.Tk()
app.title("Greeting App")
app.geometry("500x400")

current_theme = LIGHT_THEME
app.configure(bg=current_theme["bg"])

# Function to apply current theme
def apply_theme():
    app.configure(bg=current_theme["bg"])
    for widget in app.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(bg=current_theme["bg"], fg=current_theme["fg"])
        elif isinstance(widget, tk.Button):
            widget.config(bg=current_theme["button_bg"], fg=current_theme["button_fg"])
        elif isinstance(widget, tk.Entry):
            widget.config(bg="white" if current_theme == LIGHT_THEME else "#555", fg=current_theme["fg"])

# Header label
header = tk.Label(app, text="👋 Welcome!", font=("Helvetica", 18, "bold"))
header.pack(pady=10)

# Time label
time_label = tk.Label(app, text="", font=("Helvetica", 10))
time_label.pack()

def update_time():
    now = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")
    time_label.config(text=f"Current Time: {now}")
    app.after(1000, update_time)  # Update every second

# Name input
prompt = tk.Label(app, text="What's your name?", font=("Helvetica", 12))
prompt.pack()

input_name = tk.Entry(app, font=("Helvetica", 12), width=30)
input_name.pack(pady=5)

# Greeting label
message = tk.Label(app, text="", font=("Helvetica", 14))
message.pack(pady=10)

# Greeting history
history_label = tk.Label(app, text="Greeting History:", font=("Helvetica", 12, "bold"))
history_label.pack()

history_box = tk.Text(app, height=5, width=45, font=("Helvetica", 10))
history_box.pack(pady=5)
history_box.config(state="disabled")

# Function to greet the user
def say_hello():
    user = input_name.get().strip()
    if user:
        greeting = f"Hi {user}! 👋"
        message.config(text=greeting, fg="green")
        add_to_history(greeting)
    else:
        message.config(text="Please enter your name!", fg="crimson")

# Function to add to greeting history
def add_to_history(text):
    history_box.config(state="normal")
    timestamp = datetime.now().strftime("%H:%M:%S")
    history_box.insert(tk.END, f"[{timestamp}] {text}\n")
    history_box.config(state="disabled")
    history_box.see(tk.END)

# Function to clear input and greeting
def clear_input():
    input_name.delete(0, tk.END)
    message.config(text="")

# Theme toggle
def toggle_theme():
    global current_theme
    current_theme = DARK_THEME if current_theme == LIGHT_THEME else LIGHT_THEME
    apply_theme()

# Buttons
btn_frame = tk.Frame(app, bg=current_theme["bg"])
btn_frame.pack(pady=10)

greet_btn = tk.Button(btn_frame, text="Greet", command=say_hello, font=("Helvetica", 11))
greet_btn.grid(row=0, column=0, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear", command=clear_input, font=("Helvetica", 11))
clear_btn.grid(row=0, column=1, padx=5)

theme_btn = tk.Button(btn_frame, text="Toggle Theme", command=toggle_theme, font=("Helvetica", 11))
theme_btn.grid(row=0, column=2, padx=5)

# Initialize theme and time
apply_theme()
update_time()

# Run the app
app.mainloop()
