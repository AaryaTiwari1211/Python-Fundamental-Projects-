from enum import auto
from re import L
from tkinter import *
import math

root = Tk()
root.title("Calculator")

def my_input():
    return
input = Entry(root, width=35, font=('Arial',16),borderwidth=5)
input.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


def button_clear():
    input.delete(0,END)

def button_add():
    first_num=input.get()
    global f_num
    global math 
    global sec_num
    math="addition"
    f_num = int(first_num)
    input.delete(0,END)
    
    
def nahidegi():
    sec_num=input.get()
    if  f_num==69 and int(sec_num)==69:
        input.insert(0,"nahi degi")
        
def button_equal():
    sec_num=input.get()
    input.delete(0,END)
    nahidegi()
    if math == "addition":
        input.insert(0,f_num + int(sec_num))
    elif math == "subtraction":
        input.insert(0,f_num - int(sec_num))
    elif math == "multiplication":
        input.insert(0,f_num * int(sec_num))
    else:
        input.insert(0,f_num/int(sec_num))
    
def button_subtract():
    first_num=input.get()
    global f_num
    global math 
    math="subtraction"
    f_num = int(first_num)
    input.delete(0,END)

def button_mulitply():
    first_num=input.get()
    global f_num
    global math 
    math="multiplication"
    f_num = int(first_num)
    input.delete(0,END)

def button_divide():
    first_num=input.get()
    global f_num
    global math 
    math="division"
    f_num = int(first_num)
    input.delete(0,END)


def my_buttons(number):
    current = input.get()
    input.delete(0,END)
    input.insert(0,str(current) + str(number))
buttonplus=Button(root,text="+",command= button_add,padx=40,pady=20)
buttonequals=Button(root,text="=",command= button_equal,padx=40,pady=20)
buttonsubtract=Button(root,text="-",command= button_subtract,padx=40,pady=20)
buttonmultiply=Button(root,text="*",command= button_mulitply,padx=40,pady=20)
buttondivide=Button(root,text="/",command= button_divide,padx=40,pady=20)
buttonclear=Button(root,text="Clear",command=button_clear,padx=40,pady=20)
button0=Button(root,text="0",command=lambda: my_buttons(0),padx=40,pady=20)
button1=Button(root,text="1",command=lambda: my_buttons(1),padx=40,pady=20)
button2=Button(root,text="2",command=lambda: my_buttons(2),padx=40,pady=20)
button3=Button(root,text="3",command=lambda: my_buttons(3),padx=40,pady=20)
button4=Button(root,text="4",command=lambda: my_buttons(4),padx=40,pady=20)
button5=Button(root,text="5",command=lambda: my_buttons(5),padx=40,pady=20)
button6=Button(root,text="6",command=lambda: my_buttons(6),padx=40,pady=20)
button7=Button(root,text="7",command=lambda: my_buttons(7),padx=40,pady=20)
button8=Button(root,text="8",command=lambda: my_buttons(8),padx=40,pady=20)
button9=Button(root,text="9",command=lambda: my_buttons(9),padx=40,pady=20)

button0.grid(row=4,column=1)
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
buttonplus.grid(row=4,column=2)
buttonequals.grid(row=4,column=3)
buttonsubtract.grid(row=3,column=3)
buttonmultiply.grid(row=2,column=3)
buttondivide.grid(row=1,column=3)
buttonclear.grid(row=4,column=0)


root.mainloop()



    
    

