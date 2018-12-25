from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

window2=Tk()
window2.title("Youth Voice Nepal -Operation Control System")
window2.geometry("1375x720+0+0")
window2.configure(width=200, height=72, bg="palegoldenrod")

#frame=Frame(window2,bg="sky blue").pack()
# canvas2 for left operation section
canvas2a = Canvas(window2, width=500, height=730, bg="orchid")
line1=canvas2a.create_line(0,0,500,0,fill="yellow",width=170)
canvas_Label1=Label(window2,text="     Operations :",font=("Arial Bold",40),bg="yellow").place(x=10,y=10)
withdraw_button=Button(window2,text=" Register account ",font=("Gadugi",40),bg="white",fg="midnightblue",width=15).place(x=15,y=94)
withdraw_button=Button(window2,text="    Withdraw    ",font=("Gadugi",40),bg="light pink",fg="midnightblue",width=15).place(x=15,y=217)
withdraw_button=Button(window2,text="      Deposit     ",font=("Gadugi",40),bg="aquamarine",fg="red",width=15).place(x=15,y=337)
withdraw_button=Button(window2,text="      Transfer    ",font=("Gadugi",40),bg="khaki1",fg="midnightblue",width=15).place(x=15,y=460)
withdraw_button=Button(window2,text="   Statements  ",font=("Gadugi",40),bg="brown1",fg="snow2",width=15).place(x=15,y=582)
canvas2a.place(x=0, y=0)

# canvas2b for right search operation
canvas2b=Canvas(window2,width=880,height=250,bg="OliveDrab2")
welcome=Label(window2,text="Welcome --------",font=("Verdana Bold",20),fg="white",bg="OliveDrab2").place(x=580,y=15)
search=Label(window2,text=" Search   ",font=("Verdana Bold",35),bg="OliveDrab2",fg="blue").place(x=540,y=50)
entry_search=ttk.Entry(window2,width=42,font=("Arial",12)).pack(side=RIGHT,ipady=10,anchor=NE,pady=65,padx=120)
search=Label(window2,text=" Search By  ",font=("Verdana",20)).place(x=555,y=130)
search_types=("Name","Account number","Address(permanent)","Mobile number","ID number")
combo=Combobox(window2,values=search_types,width=28,font=("Arial",18))
combo.set("select")
combo.place(x=860,y=130)

canvas2b.place(x=501,y=0)


canvas2c=Canvas(window2,width=880,height=450,bg="azure2")
canvas2c.place(x=501,y=260)
img2 = Image("photo", file="1.ico")
window2.call('wm', 'iconphoto', window2._w, img2)
window2.mainloop()