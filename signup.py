import os
from subprocess import call

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True




#BEST WORKING CODE
from tkinter import *
import sqlite3
from tkinter import messagebox
import random
    
    
    
root=Tk()
root.configure(background="red")
root.geometry("800x700")

u=StringVar()
p=StringVar()


def home():
    def click_checkinn():
        call(["python", "checkin_gui_and_program.py"])

    def click_list():
        call(["python", "listgui.py"])

    def click_checkout():
        call(["python", "checkoutgui.py"])

    def click_getinfo():
        call(["python", "getinfoui.py"])

    class PLAYGROUND_MANAGEMENT:
        def __init__(self):
            root = Tk()
            '''This class configures and populates the toplevel window.
               top is the toplevel containing window.'''
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#ffffff'  # X11 color: 'white'
            _ana1color = '#ffffff'  # X11 color: 'white'
            _ana2color = '#ffffff'  # X11 color: 'white'
            font14 = "-family {Segoe UI} -size 15 -weight bold -slant " \
                     "roman -underline 0 -overstrike 0"
            font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold " \
                     "-slant roman -underline 0 -overstrike 0"
            font9 = "-family {Segoe UI} -size 9 -weight normal -slant " \
                    "roman -underline 0 -overstrike 0"

            root.geometry("963x749+540+110")
            root.title("Playground MANAGEMENT")
            root.configure(background="#d9d9d9")
            root.configure(highlightbackground="#d9d9d9")
            root.configure(highlightcolor="black")

            self.menubar = Menu(root, font=font9, bg=_bgcolor, fg=_fgcolor)
            root.configure(menu=self.menubar)

            self.Frame1 = Frame(root)
            self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
            self.Frame1.configure(relief=GROOVE)
            self.Frame1.configure(borderwidth="2")
            self.Frame1.configure(relief=GROOVE)
            self.Frame1.configure(background="#d9d9d9")
            self.Frame1.configure(highlightbackground="#d9d9d9")
            self.Frame1.configure(highlightcolor="black")
            self.Frame1.configure(width=925)

            self.Message6 = Message(self.Frame1)
            self.Message6.place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)
            self.Message6.configure(background="#d9d9d9")
            self.Message6.configure(font=font16)
            self.Message6.configure(foreground="#000000")
            self.Message6.configure(highlightbackground="#d9d9d9")
            self.Message6.configure(highlightcolor="black")
            self.Message6.configure(text='''WELCOME''')
            self.Message6.configure(width=791)

            self.Button2 = Button(self.Frame1)
            self.Button2.place(relx=0.18, rely=0.17, height=103, width=566)
            self.Button2.configure(activebackground="#d9d9d9")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#bfbfbf")
            self.Button2.configure(font=font14)
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''1.BOOK A PLAYGROUND''')
            self.Button2.configure(width=566)
            self.Button2.configure(command=click_checkinn)

            self.Button3 = Button(self.Frame1)
            self.Button3.place(relx=0.18, rely=0.33, height=93, width=566)
            self.Button3.configure(activebackground="#d9d9d9")
            self.Button3.configure(activeforeground="#000000")
            self.Button3.configure(background="#d9d9d9")
            self.Button3.configure(disabledforeground="#bfbfbf")
            self.Button3.configure(font=font14)
            self.Button3.configure(foreground="#000000")
            self.Button3.configure(highlightbackground="#d9d9d9")
            self.Button3.configure(highlightcolor="black")
            self.Button3.configure(pady="0")
            self.Button3.configure(text='''2.SHOW BOOKED LIST''')
            self.Button3.configure(width=566)
            self.Button3.configure(command=click_list)

            self.Button4 = Button(self.Frame1)
            self.Button4.place(relx=0.18, rely=0.47, height=93, width=566)
            self.Button4.configure(activebackground="#d9d9d9")
            self.Button4.configure(activeforeground="#000000")
            self.Button4.configure(background="#d9d9d9")
            self.Button4.configure(disabledforeground="#bfbfbf")
            self.Button4.configure(font=font14)
            self.Button4.configure(foreground="#000000")
            self.Button4.configure(highlightbackground="#d9d9d9")
            self.Button4.configure(highlightcolor="black")
            self.Button4.configure(pady="0")
            self.Button4.configure(text='''3.CANCEL BOOKING''')
            self.Button4.configure(width=566)
            self.Button4.configure(command=click_checkout)

            self.Button5 = Button(self.Frame1)
            self.Button5.place(relx=0.18, rely=0.61, height=103, width=566)
            self.Button5.configure(activebackground="#d9d9d9")
            self.Button5.configure(activeforeground="#000000")
            self.Button5.configure(background="#d9d9d9")
            self.Button5.configure(disabledforeground="#bfbfbf")
            self.Button5.configure(font=font14)
            self.Button5.configure(foreground="#000000")
            self.Button5.configure(highlightbackground="#d9d9d9")
            self.Button5.configure(highlightcolor="black")
            self.Button5.configure(pady="0")
            self.Button5.configure(text='''4.GET INFO OF ANY BOOKING''')
            self.Button5.configure(width=566)
            self.Button5.configure(command=click_getinfo)

            self.Button6 = Button(self.Frame1)
            self.Button6.place(relx=0.18, rely=0.77, height=103, width=566)
            self.Button6.configure(activebackground="#d9d9d9")
            self.Button6.configure(activeforeground="#000000")
            self.Button6.configure(background="#d9d9d9")
            self.Button6.configure(disabledforeground="#bfbfbf")
            self.Button6.configure(font=font14)
            self.Button6.configure(foreground="#000000")
            self.Button6.configure(highlightbackground="#d9d9d9")
            self.Button6.configure(highlightcolor="black")
            self.Button6.configure(pady="0")
            self.Button6.configure(text='''5.LOGOUT''')
            self.Button6.configure(width=566)
            self.Button6.configure(command=quit)
            root.mainloop()

    if __name__ == '__main__':
        GUUEST = PLAYGROUND_MANAGEMENT()


def save():
    u_info=u.get()
    p_info=p.get()
    conn=sqlite3.connect("DAT.db")
    c=conn.cursor()
    c.execute("Select * from da")
    a=c.fetchall()
    if (u_info,p_info) not in a:
        messagebox.showinfo("ALERT!","Wrong Username/Password")
    else:
        messagebox.showinfo("SUCCESS!","Welcome to our website")
        home()
        root.destroy()
    conn.commit()
    conn.close()








#def signa():
 #   root.destroy()
    
    

def sign():
    #signa()
    root.destroy()
    window=Tk()
    window.title("Sign-Up Page")
    window.configure(background="#c9aa88")
    window.geometry("1600x1600")

    
    def save_info():
        firstname_info = firstname.get()
        lastname_info = lastname.get()
        age_info = age.get()
        nation_info=nationality.get()
        mobile_info=mobile.get()
        mobile_info=mobile_info
        mail_info=mail.get()
        user_info=user.get()
        pass1_info=pass1.get()
        pass2_info=pass2.get()
        post_info=post.get()
        cap1_info=cap1.get()
        cap2_info=cap2.get()
        s=['indian','Indian','INDIA','INDIAN','India','india']
        #age_info=float(age_info)
        if(firstname_info==lastname_info):
            messagebox.showinfo("WRONG DETAILS!","First and Last Name should be different!")
        elif(age_info<18):
            messagebox.showinfo("ALERT","Minimum age should be 18 to create a account!")
        elif(nation_info not in s):
            messagebox.showinfo("ALERT","Only Indian Citizens are allowed to have an account here!")
        elif(len(mobile_info)<10):
            messagebox.showinfo("WRONG DETAILS","Mobile Number should contain 10 digits")
        elif('@' not in mail_info):
            messagebox.showinfo("WRONG DETAILS","Enter a Valid Mail-Id")
        elif(len(post_info)!=6):
            messagebox.showinfo("WRONG DETAILS","Enter a valid Postal Code")
        elif(len(user_info)<8):
            messagebox.showinfo("WRONG DETAILS","Username should have atleast 8 characters")
        elif(pass1_info.isupper() or pass1_info.islower() or pass1_info.isdigit() or pass1_info.isspace()):
            messagebox.showinfo("WRONG DETAILS","Your Password is too weak\nHint: USE SPECIAL SYMBOLS LIKE'!@#$%^&*")
        elif(pass1_info!=pass2_info):
            messagebox.showinfo("WRONG DETAILS","Please enter same password while conforming the password")
        elif(cap1_info!=cap2_info):
            messagebox.showinfo("WRONG DETAILS","You entered wrong captcha")
        else:
            messagebox.showinfo("SUCCESS","User registered successfully\n Please open the application again to login")
            window.destroy()
            print("Remember Your Username and Passsword")
            print("Username  :  ",user_info)
            print("Password  :  ",pass1_info)
            
        
        
    
        age_info = str(age_info)
    
        conn=sqlite3.connect("DAT.db")
        #conn.execute("create table da(User text, Password text);")
        conn.execute("insert into da(User,Password)values(?,?)",(user_info,pass1_info))
        conn.execute("delete from da where User==''")
        c=conn.execute("select * from da")
        #for i in c:
         #   print("Username",i[0])
         #   print("Password",i[1])
        conn.commit()
        conn.close()
    
    
    
        
        
        
    

   # Label(window,text="SIGN-IN FORM",width=30,fg="Red",bg="lightgreen",font=("Times", 14,"bold")).grid(row=0,column=3)
#Label(window,text="______________________________",width=10,fg="red",bg="lightgreen").grid(row=1,column=1)
#Label(window,text="______________________________",width=20,fg="red",bg="lightgreen").grid(row=1,column=2)
    Label(window,text="Personal Details:",width=30,fg="red",bg="#c9aa88",font=("Times", 14,"bold")).grid(row=1,column=3)

    firstname=StringVar()
    lastname=StringVar()
    age=IntVar()
    dob=StringVar()
    nationality=StringVar()

    Label(window,text="First Name",width=10,bg="#c9aa88",fg="black",font=("Times", 14,"bold")).grid(row=2,column=1)
    Label(window,text="Last Name",width=10,bg="#c9aa88",fg="black",font=("Times", 14,"bold")).grid(row=2,column=4)
    Label(window,text="Age",width=10,bg="#c9aa88",fg="black",font=("Times", 14,"bold")).grid(row=4,column=1)
    Label(window,text="Date Of Birth",width=10,bg="#c9aa88",fg="black",font=("Times", 14,"bold")).grid(row=4,column=4)
    Label(window,text="Nationality",width=10,bg="#c9aa88",fg="black",font=("Times", 14,"bold")).grid(row=6,column=1)
    Label(window,text="Gender",width=10,bg="#c9aa88",fg="black",font=("Times", 14,"bold")).grid(row=6,column=4)


    e1=Entry(window,textvariable=firstname,width=20,bg="lightblue",fg="black",bd=7,font=("Times", 10,"bold"))
    e2=Entry(window,textvariable=lastname,width=20,bg="lightblue",fg="black",bd=7,font=("Times", 10,"bold"))
    e3=Entry(window,textvariable=age,width=20,bg="lightblue",fg="black",bd=7,font=("Times", 10,"bold"))
    e4=Entry(window,textvariable=dob,width=20,bg="lightblue",fg="black",bd=7,font=("Times", 10,"bold"))
    e5=Entry(window,textvariable=nationality,width=20,bg="lightblue",fg="black",bd=7,font=("Times", 10,"bold"))
    Radiobutton(window,text="Male",width=10,bg="#c9aa88",fg="black",value=0).grid(row=6,column=5)
    Radiobutton(window,text="Female",width=10,bg="#c9aa88",fg="black",value=-2).grid(row=6,column=6)
    dob.set('DD-MM-YY')


    Label(window,text=" ",width=20,fg="#c9aa88",bg="#c9aa88").grid(row=2,column=3)
    Label(window,text=" ",width=20,fg="#c9aa88",bg="#c9aa88").grid(row=4,column=3)
    Label(window,text=" ",width=20,fg="#c9aa88",bg="#c9aa88").grid(row=6,column=3)
    Label(window,text=" ",width=20,fg="#c9aa88",bg="#c9aa88").grid(row=7,column=3)
    Label(window,text=" ",width=20,fg="#c9aa88",bg="#c9aa88").grid(row=8,column=3)
    Label(window,text=" ",width=20,fg="#c9aa88",bg="#c9aa88").grid(row=3,column=3)
    Label(window,text=" ",width=20,fg="#c9aa88",bg="#c9aa88").grid(row=5,column=3)
    Label(window,text=" ",width=20,fg="#c9aa88",bg="#c9aa88").grid(row=9,column=3)
    


    e1.grid(row=2,column=2)
    e2.grid(row=2,column=5)
    e3.grid(row=4,column=2)
    e4.grid(row=4,column=5)
    e5.grid(row=6,column=2)



#CONTACT DETAILS
#Label(window,text="_______________________________________",width=10,fg="red",bg="lightgreen").grid(row=9,column=1)
#Label(window,text="_______________________________________",width=20,fg="red",bg="lightgreen").grid(row=9,column=2)
    Label(window,text="Contact Details :",width=20,fg="red",bg="#c9aa88",font=("Times", 14,"bold")).grid(row=9,column=3)
    Label(window,text=" ",width=10,fg="#c9aa88",bg="#c9aa88").grid(row=10,column=1)




    mobile=StringVar()
    mail=StringVar()
    add=StringVar()
    state=StringVar()
    city=StringVar()
    post=StringVar()

    Label(window,text="Mobile",fg="black",bg="#c9aa88",font=("Times", 14,"bold")).grid(row=11,column=1)
    Label(window,text="Mail-ID",fg="black",bg="#c9aa88",font=("Times", 14,"bold")).grid(row=11,column=4)
    Label(window,text="Address",fg="black",bg="#c9aa88",font=("Times", 14,"bold")).grid(row=15,column=1)
    Label(window,text="State",fg="black",bg="#c9aa88",font=("Times", 14,"bold")).grid(row=17,column=1)
    Label(window,text="City",fg="black",bg="#c9aa88",font=("Times", 14,"bold")).grid(row=17,column=3)
    Label(window,text="Postal Code",fg="black",bg="#c9aa88",font=("Times", 14,"bold")).grid(row=17,column=5)



    e6=Entry(window,textvariable=mobile,width=30,fg="black",bg="lightblue",bd=7,font=("Times", 10,"bold"))
    e7=Entry(window,textvariable=mail,width=30,fg="black",bg="lightblue",bd=7,font=("Times", 10,"bold"))
    e8=Entry(window,textvariable=add,width=30,fg="black",bg="lightblue",bd=7,font=("Times", 10,"bold"))
    e9=Entry(window,textvariable=state,width=10,fg="black",bg="lightblue",bd=7,font=("Times", 10,"bold"))
    e10=Entry(window,textvariable=city,width=10,fg="black",bg="lightblue",bd=7,font=("Times", 10,"bold"))
    e11=Entry(window,textvariable=post,width=6,fg="black",bg="lightblue",bd=7,font=("Times", 10,"bold"))


    e6.grid(row=11,column=3)
    e7.grid(row=11,column=5)
    e8.grid(row=15,column=3)
    e9.grid(row=17,column=2)
    e10.grid(row=17,column=4)
    e11.grid(row=17,column=6)





    Label(window,text=" ",width=10,fg="#c9aa88",bg="#c9aa88").grid(row=12,column=1)
    Label(window,text=" ",width=10,fg="#c9aa88",bg="#c9aa88").grid(row=14,column=1)
    Label(window,text=" ",width=10,fg="#c9aa88",bg="#c9aa88").grid(row=16,column=1)
    Label(window,text=" ",width=10,fg="#c9aa88",bg="#c9aa88").grid(row=18,column=1)
    Label(window,text=" ",width=10,fg="#c9aa88",bg="#c9aa88").grid(row=20,column=1)
    Label(window,text=" ",fg="#c9aa88",bg="#c9aa88",width=10).grid(row=22,column=1)
    Label(window,text="Login Details",fg="red",bg="#c9aa88",width=10,font=("Times", 14,"bold")).grid(row=23,column=3)
#Label(window,text="_______________________________________________________________________",width=10,fg="red",bg="lightgreen").grid(row=23,column=1)
#Label(window,text="_______________________________________",width=20,fg="red",bg="lightgreen").grid(row=23,column=2)
    Label(window,text=" ",fg="#c9aa88",bg="#c9aa88",width=10).grid(row=24,column=1)
    Label(window,text=" ",fg="#c9aa88",bg="#c9aa88",width=10).grid(row=26,column=1)


    Label(window,text="Username",width=10,fg="black",bg="#c9aa88",font=("Times", 14,"bold")).grid(row=25,column=1)
    Label(window,text="Password",width=10,fg="black",bg="#c9aa88",font=("Times", 14,"bold")).grid(row=27,column=1)
    Label(window,text="Confirm Password",width=15,fg="black",bg="#c9aa88",font=("Times", 14,"bold")).grid(row=27,column=4)
    



    user=StringVar()
    pass1=StringVar()
    pass2=StringVar()
    a=random.randint(100001,999999)
    cap1=StringVar()
    cap2=StringVar()
    
    
    e12=Entry(window,textvariable=user,width=20,fg="black",bg="lightblue",bd=7,font=("Times New Roman", 10,"bold"))
    e13=Entry(window,textvariable=pass1,width=20,fg="black",bg="lightblue",bd=7,font=("Times", 10,"bold"))
    e14=Entry(window,textvariable=pass2,width=20,fg="black",bg="lightblue",bd=7,font=("Times", 10,"bold"))
    
    e12.grid(row=25,column=2)
    e13.grid(row=27,column=2)
    e14.grid(row=27,column=5)
    
    Label(window,text=" ",width=10,fg="#c9aa88",bg="#c9aa88").grid(row=28)
    Label(window,text=" ",width=10,fg="#c9aa88",bg="#c9aa88").grid(row=29)
    Label(window,text=" ",width=10,fg="#c9aa88",bg="#c9aa88").grid(row=30)
    Label(window,text=" ",width=10,fg="#c9aa88",bg="#c9aa88").grid(row=31,column=1)
    Label(window,text=" ",width=10,fg="#c9aa88",bg="#c9aa88").grid(row=32,column=1)
    
    def terms():
        messagebox.showinfo("TERMS AND CONDIDITIONS","1)We will be able to access your chrome\n2)We send our notifications to you through messages and cookies\n3)We don't involve in your privacy of other apps. ")

    Checkbutton(window,fg="green",bg="#c9aa88").grid(row=31,column=2)
    Button(window,text="'Terms and Conditions'",fg="Black",bg="#c9aa88",bd=0,font=("Times", 14,"bold","underline"),command=terms).grid(row=31,column=4)
    Label(window,text="I here by confirm that I have read to all the",fg="black",bg="#c9aa88",font=("Times", 14,"bold")).grid(row=31,column=3)
    Button(window,text="Submit",command=save_info,fg="Black",bg="red",font=("Times", 14,"bold"),bd=10).grid(row=33,column=3)
    
    Label(window,text="Captcha Code",fg="black",bg="#c9aa88",font=("Times", 14,"bold")).grid(row=29,column=1)
    e15=Entry(window,width=20,textvariable=cap1,fg="Black",bg="lightblue",bd=7,font=("Times", 10,"bold"))
    e15.grid(row=29,column=2)
    cap1.set(a)
    
    Label(window,text="Enter Captcha",width=15,fg="black",bg="#c9aa88",font=("Times", 14,"bold")).grid(row=29,column=4)
    e16=Entry(window,textvariable=cap2,width=20,fg="black",bg="lightblue",bd=7,font=("Times", 10,"bold"))
    e16.grid(row=29,column=5)
    
    window.mainloop()

Label(root,text=" ",width=10,fg="red",bg="red").grid(row=1,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=2,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=3,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=4,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=5,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=6,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=7,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=8,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=9,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=10,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=11,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=16,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=17,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=19,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=20,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=15,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=25,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=26,column=1)
Label(root,text=" ",width=10,fg="red",bg="red").grid(row=28,column=1)

Label(root,text=" ",width=20,fg="red",bg="red").grid(row=11,column=3)
Label(root,text=" ",width=20,fg="red",bg="red").grid(row=22,column=3)
Label(root,text=" ",width=20,fg="red",bg="red").grid(row=23,column=3)

Label(root,text=" ",width=1,fg="red",bg="red").grid(row=23,column=3)


Label(root,text="USER-LOGIN",fg="black",bg="red",font=("Times", 14,"bold"),width=10).grid(row=15,column=4)
Label(root,text="Username",fg="black",bg="red",font=("Times", 14,"bold"),width=10).grid(row=18,column=2)
Label(root,text="Password",fg="black",bg="red",font=("Times", 14,"bold"),width=10).grid(row=21,column=2)

#u=StrVar()
#p=StrVar()

e1=Entry(root,fg="Black",textvariable=u,bg="goldenrod",font=("Times", 14,"bold"),width=20,border=10)
e2=Entry(root,fg="Black",textvariable=p,bg="goldenrod",font=("Times", 14,"bold"),width=20,border=10)

e1.grid(row=18,column=5)
e2.grid(row=21,column=5)

Label(root,text="    ",width=10,fg="red",bg="red").grid(row=24,column=1)
Label(root,text="    ",width=10,fg="red",bg="red").grid(row=24,column=2)


Checkbutton(root,bg="red",width=1).grid(row=24,column=3)
Label(root,text="Save Password",fg="Black",bg="red",font=("Times", 14,"bold")).grid(row=24,column=4)
Button(root,text="Login",fg="Red",bg="Black",width=10,bd=10,font=("Times", 14,"bold"),command=save).grid(row=27,column=4)
Label(root,text="Don't have an account?",fg="black",bg="red",font=("Times", 14,"bold")).grid(row=29,column=4)
Button(root,text="Signin",fg="black",bg="red",width=10,bd=0,font=("Times", 14,"underline","bold"),command=sign).grid(row=30,column=4)




root.mainloop()