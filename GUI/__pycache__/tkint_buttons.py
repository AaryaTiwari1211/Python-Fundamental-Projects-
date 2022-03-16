from tkinter import *
root = Tk()


def click():
    mylabel=Label(root,text="I clicked it for some fun!!",fg="white" )
    mylabel.pack()


# Creating a button using Button Widget 
my_button = Button(root , text="Click me for some fun!!",state=DISABLED) # state helps in enabling and disabling the button 
my_button1 = Button(root , text="Click me for some more fun!!" , padx=50 , pady=50,command=click,fg="green",bg="blue") 
# padx and pady help in resizing the button
# command function is applied to give the button a command to execute 
# fg and bg are used to change the text and background colour respectively 

my_button.pack()
my_button1.pack()

root.mainloop()
