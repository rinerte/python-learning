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

# ENTRYBOX

# def submit():
#     username = entry.get()
#     print(f'Hello {username}')

# def delete():
#     entry.delete(0,END)

# def bckspace():
#     entry.delete(len(entry.get())-1,END)

# entry = Entry(window,
#               font=("Arial",20))
# entry.pack(side=LEFT)

# submit_button = Button(window, text="submit", command=submit)
# submit_button.pack(side=RIGHT)

# delete_button = Button(window, text="delete", command=delete)
# delete_button.pack(side=RIGHT)

# bck_button = Button(window, text="bckspace", command=bckspace)
# bck_button.pack(side=RIGHT)


# CHECKBOX

x = IntVar()

def Display():
    if(x.get() == 1):
        print("You agree")
    else:
        print("You don")



check_btn = Checkbutton(window,
                        text = "I agree",
                        variable=x,
                        onvalue=1,
                        offvalue=0,
                        command=Display)

check_btn.pack()
window.mainloop() #place window on computer screen, listen for events