# canvas
from tkinter import *
import time

window = Tk()
window.geometry("500x500")

redness = 244
greeness = 244
blueness = 244

position = 0

for i in range(10):
    for j in range(10):
        for k in range(10):
            color = f"#{redness:X}{greeness:X}{blueness:X}"
            label = Label(window, width=1, height=1, bg=color)
            label.place(x=0+position,y=0)
            blueness+=1
            position+=10
        greeness+=1
        blueness = 244
    redness+=1
    greeness = 244
    


window.mainloop()