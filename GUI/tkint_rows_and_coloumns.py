from tkinter import *

root = Tk()


# Using the gid system to locate some of the text in the GUI
mylabel1 = Label(root, text= "Hello world").grid(row=0 , column=1)
mylabel2 = Label(root,text="My name is Aarya Tiwari!!").grid(row=0,column=0)

root.mainloop()