from tkinter import *
import tkinter as tk

root=Tk()

def key_pressed(event= ''):
    print("left button")

button=Button(root,text="login",command=key_pressed)
'''
# button using event 
button.bind("<Button-1>",key_pressed)
button.pack()
'''
root.mainloop()