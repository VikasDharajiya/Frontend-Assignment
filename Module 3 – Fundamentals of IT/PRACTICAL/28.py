# LAB EXERCISE: Build a Simple Desktop Calculator Application

# Steps:

# Choose a GUI library (e.g., Tkinter for Python, JavaFX for Java, or Windows Forms for C#).
# Design the calculator interface with buttons for numbers and operations (+, -, ×, ÷).
# Implement functionality for addition, subtraction, multiplication, and division.
# Test the application for correct calculations.
# Save and run the application locally on your computer.

import tkinter as tk

def add_number(num):
    entry.insert(tk.END, str(num))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

root = tk.Tk()
root.title("Calculator")
entry = tk.Entry(root, width=16)
entry.grid(row=0, column=0, columnspan=4)

# Add buttons and link to functions here...

root.mainloop()
