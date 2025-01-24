import tkinter as tk
from math import sqrt, log

# Function to append text to the display
def append_value(value):
    display_var.set(display_var.get() + value)

# Function to clear the display
def clear_display():
    display_var.set("")

# Function to calculate the result
def calculate():
    try:
        # Replace percentage with its equivalent calculation
        expression = display_var.get().replace('%', '/100')
        result = eval(expression)
        display_var.set(result)
    except Exception:
        display_var.set("Error")

# Function to calculate square root
def calculate_sqrt():
    try:
        result = sqrt(float(display_var.get()))
        display_var.set(result)
    except Exception:
        display_var.set("Error")

# Function to calculate logarithm
def calculate_log():
    try:
        result = log(float(display_var.get()))
        display_var.set(result)
    except Exception:
        display_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x600")
root.configure(bg="#222")

# Display field
display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=("Roboto", 24), bg="#333", fg="#0f0", justify="right", bd=10, relief="flat")
display.pack(fill="both", padx=10, pady=10)

# Button grid
buttons = [
    ("C", clear_display, "#d63031"),
    ("(", lambda: append_value("("), "#2980b9"),
    (")", lambda: append_value(")"), "#2980b9"),
    ("÷", lambda: append_value("/"), "#f7931e"),
    ("log", calculate_log, "#2980b9"),
    ("√", calculate_sqrt, "#2980b9"),
    ("%", lambda: append_value("%"), "#2980b9"),
    ("×", lambda: append_value("*"), "#f7931e"),
    ("7", lambda: append_value("7"), "#444"),
    ("8", lambda: append_value("8"), "#444"),
    ("9", lambda: append_value("9"), "#444"),
    ("−", lambda: append_value("-"), "#f7931e"),
    ("4", lambda: append_value("4"), "#444"),
    ("5", lambda: append_value("5"), "#444"),
    ("6", lambda: append_value("6"), "#444"),
    ("+", lambda: append_value("+"), "#f7931e"),
    ("1", lambda: append_value("1"), "#444"),
    ("2", lambda: append_value("2"), "#444"),
    ("3", lambda: append_value("3"), "#444"),
    ("=", calculate, "#27ae60"),
    ("0", lambda: append_value("0"), "#444"),
    (".", lambda: append_value("."), "#444"),
]

# Create buttons
button_frame = tk.Frame(root, bg="#222")
button_frame.pack(expand=True, fill="both", padx=10, pady=10)

row, col = 0, 0
for text, command, color in buttons:
    button = tk.Button(
        button_frame,
        text=text,
        command=command,
        bg=color,
        fg="white",
        font=("Roboto", 18),
        bd=0,
        relief="flat",
        highlightthickness=0,
    )
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    col += 1
    if col == 4:  # New row after 4 buttons
        col = 0
        row += 1

# Adjust button sizes
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

# Run the main loop
root.mainloop()
