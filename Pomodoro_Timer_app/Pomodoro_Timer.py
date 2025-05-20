# copyright [2025] [Phat Nguyen Cong] (Github: https://github.com/paht2005)

import tkinter as tk
from tkinter import messagebox

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("350x350")
        
        self.time_remaining = 0
        self.timer_active = False
        self.session_count = 0

        # --- UI Setup ---
        self.create_widgets()

    def create_widgets(self):
        # Time Input Section
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Hours").grid(row=0, column=0)
        tk.Label(input_frame, text="Minutes").grid(row=0, column=1)
        tk.Label(input_frame, text="Seconds").grid(row=0, column=2)

        self.hour_entry = tk.Entry(input_frame, width=5)
        self.minute_entry = tk.Entry(input_frame, width=5)
        self.second_entry = tk.Entry(input_frame, width=5)

        self.hour_entry.grid(row=1, column=0, padx=5)
        self.minute_entry.grid(row=1, column=1, padx=5)
        self.second_entry.grid(row=1, column=2, padx=5)

        # Timer Display
        self.display = tk.Label(self.root, text="00:00:00", font=("Arial", 40), fg="black")
        self.display.pack(pady=20)

        # Status Label
        self.status = tk.Label(self.root, text="Ready", font=("Arial", 16))
        self.status.pack()

        # Control Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        self.start_btn = tk.Button(btn_frame, text="Start", command=self.start_timer, font=("Arial", 14))
        self.start_btn.grid(row=0, column=0, padx=10)

        self.reset_btn = tk.Button(btn_frame, text="Reset", command=self.reset_timer, font=("Arial", 14))
        self.reset_btn.grid(row=0, column=1, padx=10)

    def start_timer(self):
        if not self.timer_active:
            try:
                hours = int(self.hour_entry.get() or 0)
                minutes = int(self.minute_entry.get() or 0)
                seconds = int(self.second_entry.get() or 0)
                total_seconds = hours * 3600 + minutes * 60 + seconds

                if total_seconds <= 0:
                    messagebox.showwarning("Invalid Input", "Please set a time greater than 0.")
                    return

                self.time_remaining = total_seconds
                self.timer_active = True
                self.status.config(text="Running...", fg="green")
                self.update_timer()
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid numbers.")

    def update_timer(self):
        if self.time_remaining >= 0 and self.timer_active:
            h, rem = divmod(self.time_remaining, 3600)
            m, s = divmod(rem, 60)
            self.display.config(text=f"{h:02}:{m:02}:{s:02}")
            self.time_remaining -= 1
            self.root.after(1000, self.update_timer)
        elif self.time_remaining < 0:
            self.status.config(text="Done!", fg="blue")
            self.timer_active = False

    def reset_timer(self):
        self.timer_active = False
        self.time_remaining = 0
        self.display.config(text="00:00:00")
        self.status.config(text="Ready", fg="black")
        self.hour_entry.delete(0, tk.END)
        self.minute_entry.delete(0, tk.END)
        self.second_entry.delete(0, tk.END)


# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
