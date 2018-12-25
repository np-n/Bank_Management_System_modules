
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
import mysql.connector


my_database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2075project",
    database="customer_register",
)
# to create cursor events
my_cursor=my_database.cursor()
#my_cursor.execute("CREATE DATABASE customer_register")
# my_cursor.execute("CREATE TABLE customer_data(id MEDIUMINT NOT NULL AUTO_INCREMENT,Ac_holder_name VARCHAR(50),f_name VARCHAR(50),m_name VARCHAR(50),DOB VARCHAR(50),age INTEGER(25),mobile_no INTEGER(25),per_address VARCHAR(55),Tem_address VARCHAR(55),id_type VARCHAR(55),id_number VARCHAR(55),account_type VARCHAR(55),date_account_open VARCHAR(55),PRIMARY KEY(id))")
#table_input="INSERT INTO customer_data(Ac_holder_name,f_name,m_name,DOB,age,mobile_no,per_address,Tem_address,id_type,id_number,accout_type,date_account_open) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#customer_info= ("Netra Prasad Neupane","Peu Narayan Neupane","Tika Neupane","2055-01-30",20,9846626929,"Walling-12 Syangja","Lamachaur Pokhara","Citizenship","422045/740","saving","2075-09-04")

#my_cursor.execute(table_input,customer_info)
#my_database.commit()


def print_data(event=""):
    entry_value=input.get()
    combo_input=combo.get()
    if(combo_input=="name"):
        my_cursor.execute("SELECT * FROM customer_data WHERE Ac_holder_name ={entry_value%}")
        result=my_cursor.fetchall()
        for db in result:
            print(db)


root=Tk()
font1="arial",12,"bold","underline"
font2="helvetica",12

search_types=("name","account number","address(permanent)","mobile number","ID number")
combo=Combobox(root,values=search_types,width=20)
combo.set("select")
combo.place(x=130,y=50)
input=StringVar()
label=Label(root,text="Search",font=font1).place(x=30,y=50)
entry1=Entry(root,font=font2,textvariable=input)
entry1.bind("<Return>",print_data)
entry1.place(x=300,y=50)
root.geometry("500x500")
root.mainloop()


