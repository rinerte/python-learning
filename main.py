# GUI
from tkinter import *


window = Tk()
window.geometry("420x1000")
window.title("My cool custom title")

icon = PhotoImage(file='baldHogLogo.png')
window.iconphoto(True,icon)
window.config(background="#c49029")
window.mainloop() #place window on computer screen, listen for events