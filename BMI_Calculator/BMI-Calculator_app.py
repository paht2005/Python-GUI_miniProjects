import tkinter as tk
from tkinter import messagebox

# Theme definitions
LIGHT = {
    "bg": "#f1f8e9",
    "fg": "#000000",
    "entry_bg": "#ffffff",
    "button_bg": "#aed581",
    "button_fg": "#000000",
    "chart_colors": {
        "Underweight": "#81d4fa",
        "Normal": "#a5d6a7",
        "Overweight": "#fff176",
        "Obese": "#ef9a9a"
    }
}

DARK = {
    "bg": "#263238",
    "fg": "#ffffff",
    "entry_bg": "#37474f",
    "button_bg": "#4db6ac",
    "button_fg": "#ffffff",
    "chart_colors": {
        "Underweight": "#4fc3f7",
        "Normal": "#66bb6a",
        "Overweight": "#fbc02d",
        "Obese": "#e57373"
    }
}

# Start with LIGHT theme
theme = LIGHT

# Initialize app window
app = tk.Tk()
app.title("BMI Calculator with Chart")
app.geometry("500x500")
app.configure(bg=theme["bg"])

# Theme toggle function
def toggle_theme():
    global theme
    theme = DARK if theme == LIGHT else LIGHT
    apply_theme()

def apply_theme():
    app.configure(bg=theme["bg"])
    for widget in app.winfo_children():
        cls = widget.__class__.__name__

        if cls == "Label":
            widget.configure(bg=theme["bg"], fg=theme["fg"])
        elif cls == "Frame":
            widget.configure(bg=theme["bg"]) 
        elif cls == "Entry":
            widget.configure(bg=theme["entry_bg"], fg=theme["fg"])
        elif cls == "Button":
            widget.configure(bg=theme["button_bg"], fg=theme["button_fg"])
        elif cls == "Canvas":
            widget.configure(bg=theme["bg"])

# Widgets
header = tk.Label(app, text="🧮 BMI Calculator", font=("Helvetica", 20, "bold"))
header.pack(pady=15)

weight_label = tk.Label(app, text="Weight (kg):", font=("Helvetica", 12))
weight_label.pack()
weight_entry = tk.Entry(app, font=("Helvetica", 12), width=25)
weight_entry.pack(pady=5)

height_label = tk.Label(app, text="Height (m):", font=("Helvetica", 12))
height_label.pack()
height_entry = tk.Entry(app, font=("Helvetica", 12), width=25)
height_entry.pack(pady=5)

result_label = tk.Label(app, text="", font=("Helvetica", 14, "bold"))
result_label.pack(pady=15)

# Chart canvas
chart = tk.Canvas(app, width=400, height=50, highlightthickness=0)
chart.pack(pady=10)

# Draw BMI range chart
def draw_chart(active_category=None):
    chart.delete("all")
    ranges = [
        ("Underweight", 0, 18.5),
        ("Normal", 18.5, 24.9),
        ("Overweight", 25, 29.9),
        ("Obese", 30, 40)
    ]
    full_width = 400
    for i, (label, start, end) in enumerate(ranges):
        x0 = int(start / 40 * full_width)
        x1 = int(end / 40 * full_width)
        color = theme["chart_colors"][label]
        border = 3 if label == active_category else 1
        chart.create_rectangle(x0, 0, x1, 50, fill=color, width=border)
        chart.create_text((x0 + x1) // 2, 25, text=label, font=("Helvetica", 10, "bold"))

# BMI calculation
def calculate_bmi():
    try:
        w = float(weight_entry.get())
        h = float(height_entry.get())
        if w <= 0 or h <= 0:
            raise ValueError
        bmi = w / (h ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"Your BMI: {bmi:.2f} ({category})",
            fg=theme["chart_colors"][category]
        )
        draw_chart(active_category=category)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid positive numbers.")

# Reset fields
def reset_all():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")
    draw_chart()

# Button group
btn_frame = tk.Frame(app, bg=theme["bg"])
btn_frame.pack(pady=10)

calc_btn = tk.Button(btn_frame, text="Calculate", command=calculate_bmi, font=("Helvetica", 11), width=12)
calc_btn.grid(row=0, column=0, padx=5)

reset_btn = tk.Button(btn_frame, text="Reset", command=reset_all, font=("Helvetica", 11), width=12)
reset_btn.grid(row=0, column=1, padx=5)

theme_btn = tk.Button(btn_frame, text="Toggle Theme", command=toggle_theme, font=("Helvetica", 11), width=12)
theme_btn.grid(row=0, column=2, padx=5)

# Initial rendering
apply_theme()
draw_chart()

# Start GUI loop
app.mainloop()
