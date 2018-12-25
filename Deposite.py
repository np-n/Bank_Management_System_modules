# this is for deposit layout and database
from tkinter import *
from tkinter import ttk
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
# Left to add image,signature,amount_to deposit
#my_cursor.execute("CREATE DATABASE customer_register")
# my_cursor.execute("CREATE TABLE customer_data(id MEDIUMINT NOT NULL AUTO_INCREMENT,Ac_holder_name VARCHAR(50),f_name VARCHAR(50),m_name VARCHAR(50),DOB VARCHAR(50),age INTEGER(25),mobile_no INTEGER(25),per_address VARCHAR(55),Tem_address VARCHAR(55),id_type VARCHAR(55),id_number VARCHAR(55),account_type VARCHAR(55),date_account_open VARCHAR(55),PRIMARY KEY(id))")
#table_input="INSERT INTO customer_data(Ac_holder_name,f_name,m_name,DOB,age,mobile_no,per_address,Tem_address,id_type,id_number,accout_type,date_account_open) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#customer_info= ("Netra Prasad Neupane","Peu Narayan Neupane","Tika Neupane","2055-01-30",20,9846626929,"Walling-12 Syangja","Lamachaur Pokhara","Citizenship","422045/740","saving","2075-09-04")

#my_cursor.execute(table_input,customer_info)
#my_database.commit()



def display_deposit():
    user_info1=Label(window1,text="Deposite perform succesfully,current data is").place(x=500,y=100)
    Name = Label(window1, text="Name : ").place(x=500, y=150)
    Name_display = Label(window1, text=holder_name).place(x=700, y=150)
    Account_display=Label(window1,text="Account number :").place(x=500,y=200)
    Account_no_display = Label(window1,text=account_num).place(x=700, y=200)
    Amountt_display = Label(window1, text="Current Balance :").place(x=500, y=250)
    # updating in to database
    withdraw_amt = k.get()
    p = (avl_bal + withdraw_amt) # amount after withdraw
    print(p)
    my_cursor.execute("UPDATE customer_data SET current_amount=%s WHERE account_number = %s ",(p,account_num,))
    my_database.commit()

    Amount_after_withdraw = Label(window1, text=p).place(x=700, y=250)


def display_content():
    global holder_name
    global account_num
    global mobile_num
    global id_num
    global avl_bal

    p_store=b.get()
    my_cursor.execute("SELECT * FROM customer_data where account_number LIKE %s ",(p_store,))
    result=my_cursor.fetchall()
    for db in result:
         holder_name=db[2]
         account_num=db[3]
         mobile_num=db[8]
         id_num=db[12]
         avl_bal=db[15]

    Name=Label(window1,text="Name : ").place(x=30,y=220)
    Name_display = Label(window1,text=holder_name).place(x=140, y=220)

    Account_No=Label(window1,text="Account_number :").place(x=30,y=280)
    Account_No_display = Label(window1, text=account_num).place(x=140, y=280)

    Mobile_No=Label(window1,text="Mobile number:").place(x=30,y=330)
    Mobile_No_display = Label(window1, text=mobile_num).place(x=140, y=330)

    Id_No = Label(window1, text="ID Number:").place(x=30, y=380)
    Id_No_display = Label(window1, text=id_num).place(x=140, y=380)

    Avl_balance = Label(window1, text="Current amount :").place(x=30, y=430)
    Avl_balance_display = Label(window1, text=avl_bal).place(x=140, y=430)

    user_info = Label(window1, text="Please read and enter carefully ").place(x=30, y=490)
    withdraw_message=Label(window1, text="Amount to Deposite").place(x=30, y=550)
    global k
    global withdraw_amt
    k=IntVar()
    Store_amount_withdraw = Entry(window1,textvariable=k).place(x=190, y=550)
    withdraw_button=Button(window1,text="Withdraw",command=display_deposit).place(x=300,y=600)


window1=Tk()
window1.geometry("1200x700+50+50")
a="global"
a = StringVar()
name=Label(window1,text="name").place(x=30,y=30)
name_entry=Entry(window1,textvariable=a).place(x=90,y=30)
b="global"
b = StringVar()
account_number=Label(window1,text="account number").place(x=270,y=30)
account_entry=Entry(window1,textvariable=b).place(x=380,y=30)
display_button=Button(window1,text="Display Info",command=display_content).place(x=250,y=80)

info_label=Label(window1,text="According to above input - current balance and other customer data  ").place(x=40,y=140)


window1.mainloop()
