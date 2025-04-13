#01-----------------------------------------
def my_function(msg):
    print(msg)

if True:
    print("True Condition!")

n = 0
try:
    result = 10 / n
    my_function(result)
except ZeroDivisionError:
    print("Error: Division by zero.")
print()

def minha_funcao(msg):
    print(msg)

if True:
    print("Condição verdadeira")

n = 2
resultado = 10 / n
minha_funcao(resultado)

#02---------------------------------------
import tkinter as tk
from tkinter import messagebox

def comp_numbers():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num1 > num2 :
            messagebox.showinfo("Resul", f"The Number {num1} It's bigger than {num2}")
        elif num1 == num2 :
            messagebox.showinfo("Result", f"The Number {num1} It's same as {num2}")
        else:
            messagebox.showinfo("Result", f"The Number {num1} It's less than {num2}")
    except ValueError:
            messagebox.showerror("Error", "Please, Enter Valid Numbers!")

# Create The Window
window = tk.Tk()
window.title("Comparing Numbers")

# Create The Widget
label_num1 = tk.Label(window, text = "Number 1:")
label_num1.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = "e")

entry_num1 = tk.Entry(window)
entry_num1.grid(row = 0, column = 1, padx = 10, pady = 5)

label_num2 = tk.Label(window, text = "Number 2:")
label_num2.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = "e")

entry_num2 = tk.Entry(window)
entry_num2.grid(row = 1, column = 1, padx = 10, pady = 5)

button_comp = tk.Button(window, text="Compare", command = comp_numbers)
button_comp.grid(row = 2, columnspan = 2, padx = 10, pady = 5)

# Running The Loop Main
window.mainloop()