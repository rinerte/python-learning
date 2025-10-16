# GUI
from tkinter import *

main_backcolor = "#c4c4c4"
window = Tk()
window.geometry("800x700")
window.title("My cool custom title")
icon = PhotoImage(file='baldHogLogo.png')
window.iconphoto(True,icon)
window.config(background=main_backcolor)

#LABELS
# label = Label(window,
#               text="Hello Woeld", 
#               font=('Arial',40,'bold'),
#               bg=main_backcolor,
#               fg="black",
#               relief=RAISED,
#               bd=5,
#               image=icon,
#               compound='bottom')
# label.pack()
# label.place(x=200,y=0)

#BUTTONS
# count = 0

# def click():
#     global count
#     print(count)
#     count+=1

# button = Button(window,
#                 text="CLICK ME",
#                 command=click)
# button.pack()




window.mainloop() #place window on computer screen, listen for events