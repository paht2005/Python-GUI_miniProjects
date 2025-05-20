# copyright [2025] [Phat Nguyen Cong] (Github: https://github.com/paht2005)

import tkinter as tk
from tkinter import colorchooser

# Initialize the main window
app = tk.Tk()
app.title("Drawing Pad")
app.geometry("600x600")
app.config(bg="#f7f7f7")

# Initialize drawing settings
pen_color = "black"
pen_size = 2

# Create drawing area (canvas)
drawing_area = tk.Canvas(app, width=500, height=400, bg="white", bd=2, relief="solid")
drawing_area.pack(pady=20)

# Function to handle drawing
def sketch(event):
    x1, y1 = event.x, event.y
    drawing_area.create_oval(
        x1 - pen_size, y1 - pen_size,
        x1 + pen_size, y1 + pen_size,
        fill=pen_color, outline=pen_color
    )

# Function to clear the canvas
def reset_canvas():
    drawing_area.delete("all")

# Function to pick a new color
def pick_color():
    global pen_color
    color = colorchooser.askcolor()[1]
    if color:
        pen_color = color

# Function to adjust the pen size
def adjust_thickness(size):
    global pen_size
    pen_size = int(size)

# Bind the drawing function to mouse motion
drawing_area.bind("<B1-Motion>", sketch)

# Create the control panel with buttons and sliders
controls = tk.Frame(app, bg="#f7f7f7")
controls.pack(pady=10)

# Button for color selection
color_button = tk.Button(controls, text="Pick Color", command=pick_color, bg="#66bb6a", fg="black", font=("Arial", 10))
color_button.grid(row=0, column=0, padx=15)

# Button to clear the canvas
clear_button = tk.Button(controls, text="Clear", command=reset_canvas, bg="#e57373", fg="black", font=("Arial", 10))
clear_button.grid(row=0, column=1, padx=15)

# Label and slider for pen thickness
thickness_label = tk.Label(controls, text="Pen Size:", bg="#f7f7f7", font=("Arial", 10))
thickness_label.grid(row=0, column=2, padx=15)

pen_slider = tk.Scale(controls, from_=1, to=10, orient="horizontal", command=adjust_thickness, bg="#f7f7f7")
pen_slider.set(2)
pen_slider.grid(row=0, column=3, padx=15)

# Start the Tkinter event loop
app.mainloop()