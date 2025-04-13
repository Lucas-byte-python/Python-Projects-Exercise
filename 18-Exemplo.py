#Tkinter Used-----------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox

def div_numbers():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 / num2
        messagebox.showinfo("Result: ", f"The Quotient is: {result}")
    except ValueError:
        messagebox.showinfo("Error","Please, Enter Valid Numbers")
    except ZeroDivisionError:
        messagebox.showinfo("Error", "Division by Zero is Not Allowed!")

#Create The Window------------------------------------------------------------------------
window = tk.Tk()
window.title("Division Calculator")

#Create The Widgets-----------------------------------------------------------------------
label_num1 = tk.Label(window, text = "Dividend:")
label_num1.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = 'e')

entry_num1 = tk.Entry(window)
entry_num1.grid(row = 0, column = 1, padx = 10, pady = 5)

label_num2 = tk.Label(window, text = "Divider:")
label_num2.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = 'e')

entry_num2 = tk.Entry(window)
entry_num2.grid(row = 1, column = 1, padx = 10, pady = 5)

button_div = tk.Button(window, text = "To Divide", command = div_numbers)
button_div.grid(row = 2, columnspan = 2, padx = 100, pady = 50)

#Running The Loop Main---------------------------------------------------------------------
window.mainloop()
