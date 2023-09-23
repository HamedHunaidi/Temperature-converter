import tkinter as tk
import math
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Label
from tkinter.ttk import Button


# functions
def CtoF():
    # formula
    b1_answer = (float(b1_entry.get()) * (9 / 5)) + 32
    # answer label
    result1 = Label(root, text=b1_answer, font=("Helvetica", 14)).grid(
        row=1, column=2, sticky=N, pady=2
    )


def FtoC():
    # formula
    b2_answer = (float(b2_entry.get()) - 32) * (5 / 9)
    # answer label
    result2 = Label(root, text=b2_answer, font=("Helvetica", 14)).grid(
        row=2, column=2, sticky=N, pady=2
    )


# window
root = tk.Tk()
root.title("Temp Converter")
root.geometry("400x130")

# grid geometry
root.columnconfigure((0, 1, 2, 3), weight=1)
root.rowconfigure((0, 1, 2, 3), weight=1)

# main label
label = Label(root, text="Temp Converter", font=("Helvetica", 14))
label.grid(row=0, column=1, sticky=N, pady=2)

# variables
b1_entry = tk.StringVar(root)
b1_answer = tk.StringVar(root)
b2_entry = tk.StringVar(root)
b2_answer = tk.StringVar(root)

# 2 buttons
button1 = tk.Button(root, text=" Celsius to Fahrenheit", command=CtoF).grid(
    row=1, column=0, sticky=W, pady=2
)
button2 = tk.Button(root, text="Fahrenheit to Celsius", command=FtoC).grid(
    row=2, column=0, sticky=W, pady=2
)


# 2 entries
ttk.Entry(root, textvariable=b1_entry).grid(row=1, column=1)
ttk.Entry(root, textvariable=b2_entry).grid(row=2, column=1)


# functionality
root.mainloop()
