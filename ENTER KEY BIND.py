from tkinter import *
import tkinter as tk

root=Tk()

def key_pressed(event= ''):
    value=entry.get()
    print(value)
    entry.delete(0,"end")

entry=Entry(root)
# enter key is bind only on entry widget
entry.bind("<Return>",key_pressed)
entry.pack()
root.mainloop()