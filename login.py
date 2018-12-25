
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import mysql.connector

my_database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2075project",
    database="Banking_login",
)
# to create cursor events
my_cursor=my_database.cursor()
# my_cursor.execute("CREATE DATABASE Banking_login")
#my_cursor.execute("CREATE TABLE Staff_data( id MEDIUMINT NOT NULL AUTO_INCREMENT,name VARCHAR(255),password VARCHAR(255),mobile_number VARCHAR(255),email VARCHAR(255),PRIMARY KEY(id))")

'''
staff_table_input="INSERT INTO staff_data(name,password,mobile_number,email) VALUES(%s,%s,%s,%s)"
input_records=[("Aswin Neupane","aswin123","9846634652","aswin44@gmail.com"),
    ("Ashok Neupane","ashok123","9846689899","ashok44@gmail.com"),
    ("Suraj Neupane","suraj123","9846667879","suraj44@gmail.com"),
    ("Bikash Panday","bikash123","9846639867","bikash44@gmail.com"),
    ("Sujan Gyawali","sujan123","9846634687","sujan44@gmail.com"),
    ("Upendra Dhamala","upendra123","9846667546","upendra44@gmail.com"),
    ("Hari neupane","hari123","9846638765","hari44@gmail.com"),
    ("Sujan Neupane","sujan123","9846687678","sujan44@gmail.com"),
    ("Khem Neupane","khem123","9846636872","khem44@gmail.com"),
    ("Naran Neupane","naran123","9846699652","naran44@gmail.com"),
    ("Netra Prasad Neupane ","netra123","9848778852","netra44@gmail.com"),
]
my_cursor.executemany(staff_table_input,input_records)
my_database.commit()
'''


root=tk.Tk()
def print_label():
    label3=Label(root,text="username or password is incorrect",fg="red")
    label3.place(x=298,y=80)


def entry_val(event=""):
    # inorder to delete entry
    # entry1.delete(0,"end")
    # entry2.delete(0,"end")

    count = 0
    my_cursor.execute("SELECT * FROM staff_data")
    staff_details = my_cursor.fetchall()
    for staff in staff_details:
        # print(staff[2])
        count = count + 1

    entry1_input=username_input.get().title()
    entry2_input = password_input.get()
    print(entry1_input)
    flag=True
    while(count>0  and flag==True):
       my_cursor.execute("SELECT * FROM staff_data")
       #staff_details = my_cursor.fetchall()
       for staff in staff_details:
           if(entry1_input== staff[1] and entry2_input==staff[2]):
               print("welcome to new window")
               flag=False
           else:
               count=count-1
               if(count==0):
                   print_label()
                   print("sorry your input is incorrect")




root.title("Welcome to Bank Management System")
#root.geometry("500x500") # sets the window width to 600 pixels and the height to 400 ixels.
# get maximum size of window
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d"%(width,height))
root.resizable(1,1)
canvas=tk.Canvas(root)
canvas.pack(fill="both",expand=True)

message=Label(root,text="Enter Valid username and password :",fg="green",font=("Arial Bold",16))
message.place(x=10,y=10)
name=Label(root,text="username",font=("Helvetica"))
name.place(x=50,y=50)
password=Label(root,text="password",font=("Helvetica"))
password.place(x=50,y=80)
username_input=StringVar()
password_input=StringVar()
entry1=ttk.Entry(root,textvariable=username_input)
entry1.bind("<Return>",entry_val)
entry1.place(x=160,y=50)

entry2=ttk.Entry(root,show="*",textvariable=password_input)
entry2.bind("<Return>",entry_val) # binding for entry key
entry2.place(x=160,y=80)
name=Label(root,text="Hello",font=("Helvetica Bold",20))
name.place(x=1000,y=400)
button=Button(root,text="Login",fg="green",command=entry_val)
button.place(x=140,y=160)
root.mainloop()



