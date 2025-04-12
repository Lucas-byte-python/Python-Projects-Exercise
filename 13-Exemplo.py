#Módulo de Data e Hora---------------------------------------------------
import time
from doctest import master
from tkinter.ttk import Label

print(time.time())
print(time.localtime())
x = time.time()
print(f'Local Time: {time.ctime()}')

#Tkinter------------------------------------------------------------------
from tkinter import *

windowMain = Tk()
windowMain.mainloop()

#Continuação---------------------------------------------------------------
windowMain = Tk()
text = Label(master = windowMain, text = "My window displayed!")
text.place(x = 50, y = 100)
windowMain.mainloop()

#Continuação Pt.2----------------------------------------------------------
def funcClick():
    print("Button Press!")
windowMain = Tk()
text = Label(master = windowMain, text = 'My Window Displayed!')
text.pack()

button = Button(master = windowMain, text = 'Click', command = funcClick)
button.pack()

windowMain.mainloop()

##Todos utilizão o import tkinter mesmo nas continuações. Porém eu fiz tudo no mesmo arquivo, por isso não precisou repetir o processo!