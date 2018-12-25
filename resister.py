
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
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



def enter_value():
    name_input = a.get()
    father_input = b.get()
    mother_input = c.get()
    age_input = d.get()
    dob_input = e.get()
    mobile_input = f.get()
    permanent_address_input = g.get()
    temporary_address_input = h.get()
    id_type_input = i.get()
    id_number_input = j.get()
    account_type_input = k.get()
    date_account_input = l.get()
    combo_input=combo_value.get()
    print(combo_input)

    data_input="INSERT INTO customer_data(Ac_holder_name,gender,f_name,m_name,DOB,age,mobile_no,per_address,Tem_address,id_type,id_number,account_type,date_account_open) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    append_record=(name_input,combo_input,father_input,mother_input,age_input,dob_input,mobile_input,permanent_address_input,temporary_address_input,id_type_input,id_number_input,account_type_input,date_account_input)
    my_cursor.execute(data_input,append_record)
    my_database.commit()

window1=Tk()
window1.geometry("1200x700+50+50")
a=StringVar()
name=Label(window1,text="name").place(x=30,y=30)
name_entry=Entry(window1,textvariable=a).place(x=120,y=30)

b=StringVar()
label_f_name=Label(window1,text="father name").place(x=30,y=70)
father_entry=Entry(window1,textvariable=b).place(x=120,y=70)

c=StringVar()
label_m_name=Label(window1,text="mother name").place(x=30,y=110)
mother_entry=Entry(window1,textvariable=c).place(x=120,y=110)

d=IntVar()
age=Label(window1,text="age").place(x=30,y=160)
age_entry=Entry(window1,textvariable=d).place(x=120,y=160)

e=StringVar()
label_dob=Label(window1,text="Date of birth").place(x=30,y=200)
dob_entry=Entry(window1,textvariable=e).place(x=120,y=200)

f=IntVar()
label_mobile_number=Label(window1,text="mobile number").place(x=30,y=240)
mobile_number_entry=Entry(window1,textvariable=f).place(x=120,y=240)

gender=Label(window1,text="sex").place(x=30,y=280)
combo_value=StringVar()
gender_value=("male","female","other")
combo=Combobox(window1,values=gender_value,textvariable=combo_value,state="readonly") # state prevent change in combo value
combo.set("select")
combo.place(x=120,y=280)

g=StringVar()
permanent_address=Label(window1,text="permanent address").place(x=350,y=30)
peramnent_address_entry=Entry(window1,textvariable=g).place(x=460,y=30)

h=StringVar()
temporary_address=Label(window1,text="temporary address").place(x=350,y=70)
temporary_address_entry=Entry(window1,textvariable=h).place(x=460,y=70)

i=StringVar()
id_type=Label(window1,text="id type").place(x=350,y=110)
id_type_entry=Entry(window1,textvariable=i).place(x=460,y=110)

j=StringVar()
id_number=Label(window1,text="id number").place(x=350,y=150)
id_number_entry=Entry(window1,textvariable=j).place(x=460,y=150)

k=StringVar()
account_type=Label(window1,text="account type").place(x=350,y=200)
account_type_entry=Entry(window1,textvariable=k).place(x=460,y=200)

l=StringVar()
date_account_open=Label(window1,text="date").place(x=350,y=240)
date_account_open_entry=Entry(window1,textvariable=l).place(x=460,y=240)

button=Button(window1,text="Create account",command=enter_value).place(x=250,y=350)




window1.mainloop()