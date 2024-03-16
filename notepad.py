from tkinter.filedialog import *
import tkinter as tk
from tkinter import * 
def saveFile():
    new_file = asksaveasfile(mode='w', filetype = [('text files', '.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()
    
def openFile():
    file = askopenfile(mode='r', filetype = [('text files', '*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)
    
def clearFile():
    entry.delete(1.0, END)
    
root = Tk()

root.geometry("400x600")
root.title("Smart Notepad TITE")
root.config(bg="white")
top = Frame(root)
top.pack(padx = 10, pady = 5, anchor= 'nw')

b1 = Button(root, text="Open", bg="white", command=openFile)
b1.pack(in_= top, side=LEFT) 

b2 = Button(root, text="Save", bg="white", command=saveFile)
b2.pack(in_= top, side=LEFT)

b3 = Button(root, text="Clear", bg="white", command=clearFile)
b3.pack(in_= top, side=LEFT)

b4 = Button(root, text="Exit", bg="white", command=exit)
b4.pack(in_= top, side=LEFT)

entry = Text(root, wrap=WORD, bg = "#87CEEB", font=("poppins", 15))
entry.pack(padx= 10, pady=5, expand=TRUE, fill=BOTH)

root.mainloop()