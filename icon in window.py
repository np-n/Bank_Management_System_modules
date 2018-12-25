from tkinter import *
from tkinter import ttk

window1 = Tk()
window1.title("Bank Management Login")
# Canvas setup
window1.configure(width=200,height=72,bg="#C0C0C0")
canvas1=Canvas(window1,width=400,height=720,bg="#90EE90")
line=canvas1.create_line(370,0,370,720,fill="purple",width=50)
line=canvas1.create_line(390,0,390,720,fill="white",width=30)
canvas1.place(x=0,y=0)

# for initial label to window 1
window1_label1=Label(window1,text="Welcome to ",font=("Verdana Bold",35),bg="#C0C0C0",fg="#00008B").place(x=460,y=100)
window1_label2=Label(window1,text="Youth Voice Nepal Bank Limited",font=("Verdana Bold",30),bg="#C0C0C0",fg="#191970").place(x=560,y=150)
window1_label2=Label(window1,text="Pokhara,Nepal",font=("Arial Bold",20),bg="#C0C0C0",fg="#B22222").place(x=850,y=210)

# function call for second window
def get_window2():
    window2=Tk()
    window1.quit()
    window2.title("Youth Voice Nepal -Operation Control System")
    window2.geometry("1375x720+1+1")
    window2.configure(width=200, height=72, bg="#C0C0C0")
    canvas2 = Canvas(window2, width=400, height=720, bg="#90EE90")
    line = canvas2.create_line(370, 0, 370, 720, fill="purple", width=50)
    line = canvas2.create_line(390, 0, 390, 720, fill="white", width=30)
    canvas2.place(x=0, y=0)
    img2 = Image("photo", file="1.ico")
    window2.call('wm', 'iconphoto', window2._w, img2)
    window2.mainloop()

# Login form  and button in window 1
window1_form_userinfo=Label(window1,text="Enter the following details appropriately inorder to perform banking operation",font=("Calibri Bold",18),bg="#C0C0C0",fg="midnight blue").place(x=500,y=400)
window1_form_labe1=Label(window1,text="Username",font=("Calibri Bold",16),bg="#C0C0C0").place(x=550,y=450)
window_form_entry1=ttk.Entry(window1,font=("Verdana",12),width=30).place(x=700,y=450)
window1_form_labe2=Label(window1,text="Password",font=("Calibri Bold",16),bg="#C0C0C0").place(x=550,y=500)
window1_form_entry2=ttk.Entry(window1,font=("Verdana",12),width=30,show="*").place(x=700,y=500)
window1_checkbutton=Checkbutton(window1,text="keep logged in ",bg="#C0C0C0",font=("Verdana",12)).place(x=630,y=530)
window1_button1=Button(window1,text="  login  ",fg="red",bg="yellow",font=("Calibri Bold",14),command= get_window2 ).place(x=770,y=560)

img1 = Image("photo", file="1.ico")
window1.call('wm','iconphoto',window1._w,img1)
window1.geometry("1375x720+1+1")
window1.mainloop()