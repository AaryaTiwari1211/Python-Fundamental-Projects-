import json
from difflib import get_close_matches
from operator import inv
from tkinter import *
dict= json.load(open('Dictionary\data.json'))
root = Tk()

def search():
    search=Label(root,text="Search : ", font=('Arial',15))
    search.grid(row=2,column=3,)
search()
def input_word():
    word=Entry(root,width=50)
    word.grid(row=2,column=4)
    global key
    key = str(word.get())
input_word()
def search_button():
    button=Button(root,text="Find meaning",padx=30,pady=10,font=('Montserrat',15),command=lambda: working())
    button.grid(row=3,column=4)
search_button()

def label():
    label=Label(root,text="Meaning :- ",font=('Arial',15))
    label.grid(row=6,column=3)
label()
  
def meaning_label(dict_meaning):
    meaning_label=Label(root,text=dict_meaning)
    meaning_label.grid(row=6,column=4) 
    
def invalid(inv):
    inv=Label(root,text="Invalid input please recheck your word")
    inv.grid(row=8,column=9)
    global invalid_input
    invalid_input = str(inv)
    
def working():
    if key in dict:
        meaning_label(dict[key])
    else:
        invalid(invalid_input)
    
        
            
    
         
root.mainloop()
