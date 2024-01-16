from atexit import register
from logging import root
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector     

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=PhotoImage(file="bg_image_s.png")
       # self.bg=
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=560,y=170,width=340,height=450)

        img1=Image.open("profile.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=685,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=105,y=100)

        username=lbl=Label(frame,text="Username",font=("times new roman",20,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=190,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",20,"bold"),fg="white",bg="black")
        password.place(x=70,y=230)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=265,width=270)

        #============Icon Images====================
        img2=Image.open("profile_s.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=600,y=330,width=25,height=25)

        img3=Image.open("pwd.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=600,y=405,width=25,height=25)

        #=====Login Button===========
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
        loginbtn.place(x=110,y=310,width=120,height=35)

        #====Register Button======
        register_btn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black")
        register_btn.place(x=30,y=360,width=180,height=35)

        #=======Forget Password===========
        fgtPwd_btn=Button(frame,text="Forget Password",font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black")
        fgtPwd_btn.place(x=30,y=390,width=160,height=35)
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error, all fields are required!")
        elif self.txtuser.get()=="Dhamsevak" and self.txtpass.get()=="ILoveKrishna@1":
            messagebox.showinfo("Logged in Sucessfully!")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="siksharthkam")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where eamil=%s and password=%s",(
                                                                                       self.var_eamil.get(),
                                                                                       self.var_eamil.get()

            ))
            row=my_cursor.fetchone()
            if(row==None):
                messagebox.showerror("Error","Invalif Username or Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=mainPage(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close() 

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


        #======variables=======
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_Q=StringVar()
        self.var_security_A=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()



        #=======bg image=========
        self.bg=ImageTk.PhotoImage(file="simp_bgpng.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        #=====left image======
        self.bg1=ImageTk.PhotoImage(file="lord-krdihna.png")
        left_lbl1=Label(self.root,image=self.bg1)
        left_lbl1.place(x=60,y=100,width=660,height=535)

        #====main frame=====
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=535)


        register_lb=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green")
        register_lb.place(x=20,y=20)


        #==========label and entry==========

        #-------row-1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=400,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=400,y=130,width=250)

        #----------row-2

        conatct=Label(frame,text="Contact no.",font=("times new roman",15,"bold"),bg="white",fg="black")
        conatct.place(x=50,y=200)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=230,width=250)

        email=Label(frame,text="Email Id",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=400,y=200)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=400,y=230,width=250)

        #----------row-3

        security_Q=Label(frame,text="Select your Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=300)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_security_Q,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your birth place","Your DOB")
        self.combo_security_Q.place(x=50,y=330,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=400,y=300)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_security_A,font=("times new roman",15))
        self.txt_security.place(x=400,y=330,width=250)

        #----------row-4

        pwsd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pwsd.place(x=50,y=400)

        self.txt_pwsd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pwsd.place(x=50,y=430,width=250)

        con_pwsd=Label(frame,text="Confirme Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        con_pwsd.place(x=400,y=400)

        self.txt_con_pwsd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_con_pwsd.place(x=400,y=430,width=250)

        #======check button=========
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the Terms and conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=490)

        #=======buttons=======
        img=Image.open("regimg.png")
        img=img.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=380,y=480)

        # img1=Image.open("login2.png")
        # img1=img1.resize((200,50),Image.Resampling.LANCZOS)
        # self.photoimage1=ImageTk.PhotoImage(img1)
        # b2=Button(frame,image=self.photoimage1,command=self.register_data,borderwidth=0,cursor="hand2")
        # b2.place(x=600,y=480)

    
    #=========Function Decleration============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_Q.get()=="Select":
            messagebox.showerror("Error, All fields are required!")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error, Re-Enter your Password!")
        elif self.var_check.get()==0:
            messagebox.showerror("Accpting our terms and conditions are necessary!")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="divya_131203",database="courseordinators")
            my_cursor=conn.cursor()
            query=("select * from registered where email=%s")
            value=(self.var_email.get())
            #my_cursor.execute(query,value)
            my_cursor.execute(query,(value,))
            row=my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error, User already exist!")
            else:
                my_cursor.execute("insert into registered values(%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_fname.get(),
                                        self.var_lname.get(),
                                        self.var_contact.get(),
                                        self.var_email.get(),
                                        self.var_security_Q.get(),
                                        self.var_security_A.get(),
                                        self.var_pass.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Register Successfully!")







        

    



if __name__=="__main__":
    main()
