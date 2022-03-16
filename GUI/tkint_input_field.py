from tkinter import *

root = Tk()

# Makes an input field 
entry = Entry(root)
entry.pack()
# Getting the value in the input field
entry.get()
def label():
    mylabel=Label(root, text=entry.get())
    mylabel.pack()
button = Button(root, text="Click Me!!",command=label)  
button.pack()
root.mainloop()

    