from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.iconbitmap('C:/Users/aarya/OneDrive/Desktop/Python Fundamental Projects/GUI/tkint_icon.ico')#Adds an icon in the top left of the prgram window
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

my_img = ImageTk.PhotoImage(Image.open("GUI\img_1.jpg"))
my_label = Label(root, image=my_img)
my_label.pack()
root.mainloop()
