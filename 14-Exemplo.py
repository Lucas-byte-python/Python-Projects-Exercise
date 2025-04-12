#Task using the Tkinter----------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox

def sum_number():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 + num2
    messagebox.showinfo("Result", f"The sum of the numbers is: {result}")

#Create the Window---------------------------------------------------------------------
window = tk.Tk()
window.title("Sum Calculator")

#Create is widgets---------------------------------------------------------------------
label_num1 = tk.Label(window, text="Number 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_num1 = tk.Entry(window)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(window, text="Number 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_num2 = tk.Entry(window)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

button_sum = tk.Button(window, text="Sum", command=sum_number())
button_sum.grid(row=2, columnspan=2, padx=10, pady=5)

#Running a Loop Main-------------------------------------------------------------------
window.mainloop()