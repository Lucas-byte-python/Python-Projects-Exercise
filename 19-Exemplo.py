#Using The Capture Move------------------------------------------------------------------------
import tkinter as tk

def update_the_Coordinate(event):
    x = event.x
    y = event.y
    label_coodinates["text"] = f'Mouse Coordinates: X={x}, Y={y}'


#The Window Create
window = tk.Tk()
window.title("Treatment of Events - Mouse Coodinates")

#Create The Widget of Label
label_coodinates = tk.Label(window, text = "Move of Mouse Over the Window to see the Cordinates!")
label_coodinates.pack(padx = 200, pady = 100)

#Binding mouse movement event to function
window.bind("<Motion>", update_the_Coordinate)

#Runnig the Main Loop
window.mainloop()

#02------------------------------------------------------------------------------------------
def capture_click(event):
    x = event.x
    y = event.y
    label_coodinates["text"] = f'Last Click: X={x}, Y={y}'

#The Window Create
window = tk.Tk()
window.title("Treatment of Events - Left Click Capture!")

#Create The Widget of Label
label_coodinates = tk.Label(window, text = "Click in any Place the Window!")
label_coodinates.pack(padx = 200, pady = 100)

#Binding mouse movement event to function
window.bind("<Button-1>", capture_click)

#Runnig the Main Loop
window.mainloop()
