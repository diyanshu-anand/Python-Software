from cProfile import label
from cgitb import text;
import hashlib;
from lib2to3.pgen2.token import RIGHTSHIFT; 
import os;
from logging import root;
from msilib.schema import Font;
from login import Register, main;
from login import Login_Window;
from sre_parse import State;
from tkinter import *;
from tkinter import font;
from tkinter.tix import PopupMenu, Select
from tokenize import String;
from turtle import color, left, position;
import tkinter.messagebox;
from sqlalchemy import create_engine
import weakref;
import MySQLdb;
from tkcalendar import DateEntry, Calendar;
import webbrowser;
import customtkinter
import mysql.connector;
from sqlalchemy import create_engine; 


# app = Tk()
# Code will run from here
WIDTH = 780;
HEIGHT = 520;

root= customtkinter.CTk()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title("Krishna's Soul");


        # configure grid layout (2x1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
frame = customtkinter.CTkFrame(master =root, width=200,height = 200, corner_radius=10)
frame.pack(side=LEFT, anchor="nw")

# function for changing appearance mode 
def change_appearance_mode(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)



# Databse connection 
connectiondb = mysql.connector.connect(host="localhost", user="root", password="divya_131203", database ="courseordinators");
courseodb = connectiondb.cursor();


# function for click on the button 
def clickon():
    tkinter.messagebox.showinfo("Form is coming");
    print("Function Worked Successfully");
# function for menu
def myfunc():
    print("Working")
# function for login pages
    # function for login of director 
def login_director():
    def login_verification_director():
       user_director_verification = username_verify_director.get();
       password_director_verification = password_verify_director.get();
       sql = "select * from director where username = %s and password = %s";
    #    query = "SELECT password FROM userinfo2";
    #    courseodb.execute(query)
    #    passwords_right = courseodb.fetchall()
       courseodb.execute(sql,[(user_director_verification),(password_director_verification)])
       results = courseodb.fetchall();  
    #    if (hashlib.md5(password_verification.encode()).hexdigest() == passwords_right):
        # print("Authentication succesful");
    #    else:
            # print("BAD login attempt")
    #    if results:
       for i in results:
            logged_director();
            break
       else:
            failed_director();
    login_screen = customtkinter.CTkToplevel(root)
    login_screen.title("Login as Director")
    login_screen.geometry("400x200")
    customtkinter.CTkLabel(login_screen, text="Please eneter details below to login").pack()
    customtkinter.CTkLabel(login_screen, text="").pack()

    global username_verify_director;
    global password_verify_director;

    username_verify_director = StringVar();
    password_verify_director = StringVar();

    customtkinter.CTkLabel(login_screen, text="Username *").pack()
    username_login_entry = Entry(login_screen, textvariable = username_verify_director);
    username_login_entry.pack()
    customtkinter.CTkLabel(login_screen, text ="").pack()
    customtkinter.CTkLabel(login_screen, text="Password *").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify_director);
    password_login_entry.pack()
    

    customtkinter.CTkLabel(login_screen, text="").pack()
    customtkinter.CTkButton(login_screen, text="login", width=12, height=2, command= login_verification_director).pack()

    #====Register Button======
    register_btn=Button(login_screen,text="New User Register",command=register_window_main,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black")
    register_btn.pack()

def login_assistant_director():
    def login_verification_assitant_director():
       user_assistant_director_verification = username_verify_assistant_director.get();
       password_assistant_director_verification = password_verify_assistant_director.get();
       sql = "select * from assistantdirector where username = %s and password = %s";
    #    query = "SELECT password FROM userinfo2";
    #    courseodb.execute(query)
    #    passwords_right = courseodb.fetchall()
       courseodb.execute(sql,[(user_assistant_director_verification),(password_assistant_director_verification)])
       results = courseodb.fetchall();  
    #    if (hashlib.md5(password_verification.encode()).hexdigest() == passwords_right):
        # print("Authentication succesful");
    #    else:
            # print("BAD login attempt")
    #    if results:
       for i in results:
            logged_assistant_director();
            break
       else:
            failed_assistant_director();
    login_screen = customtkinter.CTkToplevel(root)
    login_screen.title("Login as assistant-director")
    login_screen.geometry("400x200")
    customtkinter.CTkLabel(login_screen, text="Please eneter details below to login").pack()
    customtkinter.CTkLabel(login_screen, text="").pack()

    global username_verify_assistant_director;
    global password_verify_assistant_director;

    username_verify_assistant_director = StringVar();
    password_verify_assistant_director = StringVar();

    customtkinter.CTkLabel(login_screen, text="Username *").pack()
    username_login_entry = Entry(login_screen, textvariable = username_verify_assistant_director);
    username_login_entry.pack()
    customtkinter.CTkLabel(login_screen, text ="").pack()
    customtkinter.CTkLabel(login_screen, text="Password *").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify_assistant_director);
    password_login_entry.pack()
    

    customtkinter.CTkLabel(login_screen, text="").pack()
    customtkinter.CTkButton(login_screen, text="login", width=12, height=2, command= login_verification_assitant_director).pack()

    #====Register Button======
    register_btn=Button(login_screen,text="New User Register",command=register_window_main,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black")
    register_btn.pack()

    # function for area leader login 
def login_area_leader():
    def login_verification_area_leader():
       user_area_leader = username_verify_area_leader.get();
       password_area_leader = password_verify_area_leader.get();
       sql = "select * from arealeader where username = %s and password = %s";
    #    query = "SELECT password FROM userinfo2";
    #    courseodb.execute(query)
    #    passwords_right = courseodb.fetchall()
       courseodb.execute(sql,[(user_area_leader),(password_area_leader)])
       results = courseodb.fetchall();  
    #    if (hashlib.md5(password_verification.encode()).hexdigest() == passwords_right):
        # print("Authentication succesful");
    #    else:
            # print("BAD login attempt")
    #    if results:
       for i in results:
            logged_admin();
            break
       else:
            failed_admin();
    login_screen = customtkinter.CTkToplevel(root)
    login_screen.title("Login as Area Leader")
    login_screen.geometry("400x200")
    customtkinter.CTkLabel(login_screen, text="Please eneter details below to login").pack()
    customtkinter.CTkLabel(login_screen, text="").pack()

    global username_verify_area_leader;
    global password_verify_area_leader;

    username_verify_area_leader = StringVar();
    password_verify_area_leader = StringVar();

    customtkinter.CTkLabel(login_screen, text="Username *").pack()
    username_login_entry = Entry(login_screen, textvariable = username_verify_area_leader);
    username_login_entry.pack()
    customtkinter.CTkLabel(login_screen, text ="").pack()
    customtkinter.CTkLabel(login_screen, text="Password *").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify_area_leader);
    password_login_entry.pack()
    

    customtkinter.CTkLabel(login_screen, text="").pack()
    customtkinter.CTkButton(login_screen, text="login", width=12, height=2, command= login_verification_area_leader).pack()

    #====Register Button======
    register_btn=Button(login_screen,text="New User Register",command=register_window_main,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black")
    register_btn.pack()
    
    # function for login of admin
def login_admin():
    # func for verification
    def login_verification_course_admin():
       user_verification = username_verify.get();
       password_verification = password_verify.get();
       sql = "select * from courseadmin where username = %s and password = %s";
    #    query = "SELECT password FROM userinfo2";
    #    courseodb.execute(query)
    #    passwords_right = courseodb.fetchall()
       courseodb.execute(sql,[(user_verification),(password_verification)])
       results = courseodb.fetchall();  
    #    if (hashlib.md5(password_verification.encode()).hexdigest() == passwords_right):
        # print("Authentication succesful");
    #    else:
            # print("BAD login attempt")
    #    if results:
       for i in results:
            logged_admin();
            break
       else:
            failed_admin();
    login_screen = customtkinter.CTkToplevel(root)
    login_screen.title("Login as admin")
    login_screen.geometry("400x200")
    customtkinter.CTkLabel(login_screen, text="Please eneter details below to login").pack()
    customtkinter.CTkLabel(login_screen, text="").pack()

    global username_verify;
    global password_verify;

    username_verify = StringVar();
    password_verify = StringVar();

    customtkinter.CTkLabel(login_screen, text="Username *").pack()
    username_login_entry = Entry(login_screen, textvariable = username_verify);
    username_login_entry.pack()
    customtkinter.CTkLabel(login_screen, text ="").pack()
    customtkinter.CTkLabel(login_screen, text="Password *").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify);
    password_login_entry.pack()
    

    customtkinter.CTkLabel(login_screen, text="").pack()
    customtkinter.CTkButton(login_screen, text="login", width=12, height=2, command= login_verification_course_admin).pack()

    #====Register Button======
    register_btn=Button(login_screen,text="New User Register",command=register_window_main,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black")
    register_btn.pack()

    
# function for login of course admin 
def logged_admin():
    global logged_admin_message;
    logged_admin_message = customtkinter.CTkToplevel(root);
    logged_admin_message.title("Log in as admin");
    logged_admin_message.geometry("350x100");
    customtkinter.CTkLabel(logged_admin_message, text="Login Successfully! ... Welcome {}".format(username_verify.get()),width=120,height=25,fg_color=("gray75", "blue"),corner_radius=8).pack()
    customtkinter.CTkLabel(logged_admin_message, text ="").pack()
    customtkinter.CTkButton(logged_admin_message, width=120,height=32,border_width=0,corner_radius=8, command=logged_admin_destroy).pack()

def logged_director():
    global logged_director_message;
    logged_director_message = customtkinter.CTkToplevel(root);
    logged_director_message.title("Logged in as director");
    logged_director_message.geometry("350x100");
    customtkinter.CTkLabel(logged_director_message, text="Login Successfully! ... Welcome {}".format(username_verify_director.get()),width=120,height=25,fg_color=("gray75", "blue"),corner_radius=8).pack()
    customtkinter.CTkLabel(logged_director_message, text ="").pack()
    customtkinter.CTkButton(logged_director_message, width=120,height=32,border_width=0,corner_radius=8, command=logged_director_destroy).pack()

def logged_assistant_director():
    global logged_assistant_director_message;
    logged_assistant_director_message = customtkinter.CTkToplevel(root);
    logged_assistant_director_message.title("Logged in as director");
    logged_assistant_director_message.geometry("350x100");
    customtkinter.CTkLabel(logged_assistant_director_message, text="Login Successfully! ... Welcome {}".format(username_verify_assistant_director.get()),width=120,height=25,fg_color=("gray75", "blue"),corner_radius=8).pack()
    customtkinter.CTkLabel(logged_assistant_director_message, text ="").pack()
    customtkinter.CTkButton(logged_assistant_director_message, width=120,height=32,border_width=0,corner_radius=8, command=lambda:[logged_assistant_director_destroy(), disable_menu_ad()]).pack()

def logged_assistant_director_destroy():
    logged_assistant_director_message.destroy();

def failed_assistant_director():
    global failed_assistant_director_message;
    failed_assistant_director_message = customtkinter.CTkToplevel(root);
    failed_assistant_director_message.title("Failed to Login");
    failed_assistant_director_message.geometry("350x100");
    customtkinter.CTkLabel(failed_assistant_director_message, text="Failed to login. Please enter valid details.",fg_color=("gray75", "blue"),corner_radius=8).pack();
    customtkinter.CTkLabel(failed_assistant_director_message, text="").pack()
    customtkinter.CTkButton(failed_assistant_director_message, text="Retry",fg_color=("gray75", "blue"),corner_radius=8 , command = failed_assistant_director_destroy).pack();

def failed_assistant_director_destroy():
    failed_assistant_director_message.destroy();

def logged_director_destroy():
    logged_director_message.destroy()

def failed_director():
    global failed_director_message;
    failed_director_message = customtkinter.CTkToplevel(root);
    failed_director_message.title("Failed to Login");
    failed_director_message.geometry("350x100");
    customtkinter.CTkLabel(failed_director_message, text="Failed to login. Please enter valid details.",fg_color=("gray75", "blue"),corner_radius=8).pack();
    customtkinter.CTkLabel(failed_director_message, text="").pack()
    customtkinter.CTkButton(failed_director_message, text="Retry",fg_color=("gray75", "blue"),corner_radius=8 , command = failed_director_destroy).pack();

def failed_director_destroy():
    failed_director_message.destroy();

def logged_admin_destroy():
    logged_admin_message.destroy()


def failed_admin():
    global failed_message_admin
    failed_message_admin = customtkinter.CTkToplevel(root)
    failed_message_admin.title("Failed to Login")
    failed_message_admin.geometry("500x100");
    customtkinter.CTkLabel(failed_message_admin, text="Failed to login. Please enter valid details.",width=120,height=25,fg_color=("gray75", "blue"),corner_radius=8).pack();
    customtkinter.CTkLabel(failed_message_admin, text="").pack()
    customtkinter.CTkButton(failed_message_admin, text="Retry", width=120,height=32,border_width=0,corner_radius=8, command = failed_destroy_admin).pack();

def failed_destroy_admin():
    failed_message_admin.destroy();

# function for  registering a user 
def register_window_main():
    global user_register_window
    user_register_window = customtkinter.CTkToplevel(root)
    register_user = Register(user_register_window)
    title_window = user_register_window.title()



# function for login of course ordinator
def logged():
    global logged_message
    logged_message = customtkinter.CTkToplevel(root);
    logged_message.title("Welcome");
    logged_message.geometry("500x100");
    customtkinter.CTkLabel(logged_message, text="Login Successfully!... Welcome {} ".format(username_verify_login_courseord.get()),fg_color=("gray75", "blue"),corner_radius=8 ).pack();
    customtkinter.CTkLabel(logged_message, text="").pack();
    customtkinter.CTkButton(logged_message, text="Let's Start the work",fg_color=("gray75", "blue"),corner_radius=8 , command=lambda:[logged_destroy(), disable_menu()]).pack();

# function for disabling items in menu ater login of assistant director adm director 
def disable_menu_ad():
    main_menu.entryconfig("Sign In", state="disabled")
    main_menu.entryconfig("Register User", state="disabled")

# function for disabling menu items after login of courseod. 
def disable_menu():
    print("Its working")
    main_menu.entryconfig("Forms", state ="disabled")
    m3.entryconfig("Record Attendance", state="disabled")
    m4.entryconfig("Track all Courses", state="disabled")
    main_menu.entryconfig("Sign In", state="disabled")


# function for closing the window on clicking the button. 
def logged_destroy():
    logged_message.destroy()



# function if login fails
def failed():
    global failed_message
    failed_message = customtkinter.CTkToplevel(root)
    failed_message.title("Failed to Login")
    failed_message.geometry("500x100");
    customtkinter.CTkLabel(failed_message, text="Failed to login. Please enter valid details.",fg_color=("gray75", "blue"),corner_radius=8).pack();
    customtkinter.CTkLabel(failed_message, text="").pack()
    customtkinter.CTkButton(failed_message, text="Retry",fg_color=("gray75", "blue"),corner_radius=8 , command = failed_destroy).pack();



# function for destroying failed window 
def failed_destroy():
    failed_message.destroy();



def logged_filler():
    global logged_filler_message;
    logged_filler_message = customtkinter.CTkToplevel(root);
    logged_filler_message.title("Welcome");
    logged_filler_message.geometry("350x100");
    customtkinter.CTkLabel(logged_filler_message, text = "Login successfully done as a filler... Welcome {}".format(username_verify_login_attendance.get()),fg_color=("gray75", "blue"),corner_radius=8).pack();
    customtkinter.CTkLabel(logged_filler_message, text="").pack();
    customtkinter.CTkButton(logged_filler_message, text="Let's fill it.", width=120,height=32,border_width=0,corner_radius=8 , command=lambda:[logged_destroy_filler(), disable_items()]).pack();
    
# function for disabling menu items after login of courseod. 
def disable_items():
    print("Its working")
    main_menu.entryconfig("Forms", state="disabled")
    main_menu.entryconfig("Courses", state="disabled")
    main_menu.entryconfig("Sign In", state="disabled")
    m3.entryconfig(" View Attendance", state="disabled")

def logged_destroy_filler():
    logged_filler_message.destroy();



def failed_message_filler():
    global failed_message_filler_attempt;
    failed_message_filler_attempt = customtkinter.CTkToplevel(root);
    failed_message_filler_attempt.title("Failed To login");
    failed_message_filler_attempt.geometry("350x100");
    customtkinter.CTkLabel(failed_message_filler_attempt, text="Failed to login. PLease check again.",fg_color=("gray75", "blue"),corner_radius=8).pack();
    customtkinter.CTkLabel(failed_message_filler_attempt, text="").pack();
    customtkinter.CTkButton(failed_message_filler_attempt, text="Retry", bg="blue", fg_color=("white","blue"), relief="groove", command= failed_destroy_filler).pack()


    
def failed_destroy_filler():
    failed_message_filler_attempt.destroy()

    
def login_courseord():
    # login success PopupMenu for coordinator 
    

    

    def login_verification():
       user_verification = username_verify_login_courseord.get();
       password_verification = password_verify_login_courseord.get();
       sql = "select * from userinfo2 where username = %s and password = %s";
    #    query = "SELECT password FROM userinfo2";
    #    courseodb.execute(query)
    #    passwords_right = courseodb.fetchall()
       courseodb.execute(sql,[(user_verification),(password_verification)])
       results = courseodb.fetchall();  
    #    if (hashlib.md5(password_verification.encode()).hexdigest() == passwords_right):
        # print("Authentication succesful");
    #    else:
            # print("BAD login attempt")
    #    if results:
       for i in results:
            logged();
            break
       else:
            failed();

    # making login screen 
    login_screen = customtkinter.CTkToplevel(root)
    login_screen.title("Login as a course ordinator")
    login_screen.geometry("300x250");
    customtkinter.CTkLabel(login_screen, text="Please enter details below to login").pack()
    customtkinter.CTkLabel(login_screen, text="").pack()
    # keeping names globally all over the code for futher uses
    global username_verify_login_courseord;
    global password_verify_login_courseord;

    username_verify_login_courseord = StringVar();
    password_verify_login_courseord = StringVar();
    # making the input form for user
    customtkinter.CTkLabel(login_screen, text="Username *").pack()
    username_login_entry = Entry(login_screen, textvariable = username_verify_login_courseord);
    username_login_entry.pack()
    customtkinter.CTkLabel(login_screen, text ="").pack()
    customtkinter.CTkLabel(login_screen, text="Password *").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify_login_courseord, show="*");
    password_login_entry.pack()

    customtkinter.CTkLabel(login_screen, text="").pack()
    # button for login
    customtkinter.CTkButton(login_screen, text="login", width=12, height=2, command= login_verification).pack()
# function for login of attendance filler

def login_attendence():
    def login_verification():
        
        username_verify_filler = username_verify_login_attendance.get();
        
        password_verify_filler = password_verify_login_attendance.get();

        sql = "select * from frontliner where username= %s and password=%s";
        courseodb.execute(sql, [(username_verify_filler),(password_verify_filler)]);
        results = courseodb.fetchall()

        for i in results:
            logged_filler();
            break;
        else:
            failed_message_filler()

    # Making the login screen 
    login_screen = customtkinter.CTkToplevel(root)
    login_screen.title("Login for attendence record")
    login_screen.geometry("300x250");
    customtkinter.CTkLabel(login_screen, text="Please enter details for logging in", width=120,height=25,fg_color=("gray75", "blue"),corner_radius=8).pack()
    customtkinter.CTkLabel(login_screen, text="").pack()
    # Globally declaring the username and password 
    global username_verify_login_attendance;
    global password_verify_login_attendance;
    # Declaring their types 
    username_verify_login_attendance = StringVar();
    password_verify_login_attendance = StringVar();
    # Giving input field to the user 
    customtkinter.CTkLabel(master = login_screen, text="Username *", width=120,height=25,fg_color=("gray75", "blue"),corner_radius=8).pack()
    username_login_entry = customtkinter.CTkEntry(master = login_screen, textvariable = username_verify_login_attendance, width=120,height=25,border_width=2,corner_radius=10);
    username_login_entry.pack()
    customtkinter.CTkLabel(master = login_screen, text ="").pack()
    customtkinter.CTkLabel(master = login_screen, text="Password *", width=120,height=25,fg_color=("gray75", "blue"),corner_radius=8).pack()
    password_login_entry = customtkinter.CTkEntry(master = login_screen, textvariable=password_verify_login_attendance, width=120,height=25,border_width=2,corner_radius=10);
    password_login_entry.pack()

    customtkinter.CTkLabel(login_screen, text="").pack()
    # Button for submission or login
    customtkinter.CTkButton(login_screen,text="login",command= login_verification,width=120,height=32,border_width=0,corner_radius=8).pack();

#     

	
    
    

    

    
    
    


def form_for_new_course():
    global new_form_screen;
    # print("Its working");
    # Making new course form window 
    new_form_screen=customtkinter.CTkToplevel(root);
    new_form_screen.title("Genrate New form");
    new_form_screen.geometry("300x500");
    frame = customtkinter.CTkFrame( master = new_form_screen,width=700,height=200,corner_radius=10);
    frame.place(x=320);
    # new_form_screen.pack(side=LEFT, anchor = "nw")
    #Buttons for Questions and Response;
    # Button(frame, text="Questions", bg="blue", fg="white", relief="groove",   command= Question_screen).pack(side=LEFT, padx=24)
    # Button(frame, text="Responses", bg="blue", fg="white", relief="groove",   command= Response_screen).pack(side=RIGHT, padx=25);
    #Define a callback function
    def callback(url):
        webbrowser.open_new_tab(url)

    #Create a Label to display the link
    
    link = Label(new_form_screen, text="Click Here For Form For Sikharstakam Field",font=('Times', 15), fg="blue", cursor="hand2")
    link.pack(padx = 20, pady=20)
    link.bind("<Button-1>", lambda e:
    callback("https://docs.google.com/forms/u/0/"))
    
    link = Label(new_form_screen, text="Click Here For Form For Bilaspur Field",font=('Times', 15), fg="blue", cursor="hand2")
    link.pack(padx = 20, pady=20)
    link.bind("<Button-1>", lambda e:
    callback("https://docs.google.com/forms/u/0/"))

    link = Label(new_form_screen, text="Click Here For Form For Raipur Field",font=('Times', 15), fg="blue", cursor="hand2")
    link.pack(padx = 20, pady=20)
    link.bind("<Button-1>", lambda e:
    callback("https://docs.google.com/forms/u/0/"))

    # link = customtkinter.CTkLabel(master = new_form_screen, text="New Form for Bilaspur Field",width=120,height=25,fg_color=("white", "blue"),corner_radius=8)
    # link.pack(padx = 20, pady = 20)
    # link.bind("<Button-1>", lambda e:
    # callback("https://docs.google.com/forms/u/0/"))



def form_for_higher_level():
    global new_high_form_screen;
    # print("Its working");
    # Making new course form window 
    new_high_form_screen=customtkinter.CTkToplevel(root);
    new_high_form_screen.title("Genrate Next Level New form");
    new_high_form_screen.geometry("300x500");
    frame = customtkinter.CTkFrame( master = new_high_form_screen, width=700,height=200,corner_radius=10);
    frame.place(x=320);
    # new_form_screen.pack(side=LEFT, anchor = "nw")
    #Buttons for Questions and Response;
    # Button(frame, text="Questions", bg="blue", fg="white", relief="groove",   command= Question_screen_higher_level).pack(side=LEFT, padx=24)
    # Button(frame, text="Responses", bg="blue", fg="white", relief="groove",   command= Response_screen_higher_level).pack(side=RIGHT, padx=25);

    #Define a callback function
    def callback(url):
        webbrowser.open_new_tab(url)

    #Create a Label to display the link
    
    link = Label(new_high_form_screen, text="Click Here For Form For Sikharstakam Field",font=('Times', 15), fg="blue", cursor="hand2")
    link.pack(padx = 20, pady=20)
    link.bind("<Button-1>", lambda e:
    callback("https://docs.google.com/forms/u/0/"))
    
    link = Label(new_high_form_screen, text="Click Here For Form For Bilaspur Field",font=('Times', 15), fg="blue", cursor="hand2")
    link.pack(padx = 20, pady=20)
    link.bind("<Button-1>", lambda e:
    callback("https://docs.google.com/forms/u/0/"))

    link = Label(new_high_form_screen, text="Click Here For Form For Raipur Field",font=('Times', 15), fg="blue", cursor="hand2")
    link.pack(padx = 20, pady=20)
    link.bind("<Button-1>", lambda e:
    callback("https://docs.google.com/forms/u/0/"))


def record_attendance():
    global record_attendance_screen
    record_attendance_screen = customtkinter.CTkToplevel(root);
    record_attendance_screen.title("Fill attendance")
    record_attendance_screen.geometry("300x500")
    frame = customtkinter.CTkFrame( master= record_attendance_screen,borderwidth=6, bg="grey", relief=SUNKEN)
    my_conn = create_engine("mysql+mysqldb://root:divya_131203@localhost/courseordinators")
    #my_conn = create_engine("sqlite:///D:\\testing\\sqlite\\my_db.db")

    query="SELECT DISTINCT(coursename) as coursename FROM courses"
    query_level = "SELECT DISTINCT(level) as level FROM ramayana"
                
    my_data=my_conn.execute(query) # SQLAlchem engine result
    my_level = my_conn.execute(query_level)

    my_list = [r for r, in my_data] # create a  list 
    my_level_list = [r for r, in my_level]

    # function for sending the data 
    def send_data():
        print("I am going right")
        # sql_command = """UPDATE Gita SET  Topic=%s, Present=%s,Date=%s WHERE username=%s"""
        sql_command = """INSERT INTO gita (username, Present, Topic, Date) VALUES(%s,%s, %s, %s)"""
        username_entry_box = username_entry.get()
        present_data = "Present"
        topic_name_box = topic_entry_input.get()
        date_entry_input_box = date_entry_input.get_date()


        inputs = (username_entry_box, present_data, topic_name_box,  date_entry_input_box )

        courseodb.execute(sql_command, inputs)
        connectiondb.commit()
        
        print("Executed Successfully")

           

    course_name = StringVar();
    username_course = StringVar();
    topic_name = StringVar();

    
    
    def pick_level(e):
        if course_name_entry.get() == "Gita":
            level_entry.config(values =my_list)
    course = customtkinter.CTkLabel(record_attendance_screen, text="Enter course name", width=120,height=25,fg_color=("white", "blue"),corner_radius=8)
    course.grid(row=1, column=2)
    
    global course_name_entry
    course_name_entry = customtkinter.CTkComboBox(master = record_attendance_screen, values= my_list)
    
    course_name_entry.grid(row = 1, column=3,  padx=40, pady=40)
    #for dependent dropdown
    course_name_entry.bind("<<Combobox Selected>>", pick_level)
    
    level = customtkinter.CTkLabel(record_attendance_screen, text="Enter course name", width=120,height=25,fg_color=("white", "blue"),corner_radius=8)
    level.grid(row=2, column=2)
    
    global level_entry
    level_entry = customtkinter.CTkComboBox(master = record_attendance_screen, values=my_level_list)
    level_entry.grid(row = 2, column=3, padx=40, pady=40)
    

    username_course = customtkinter.CTkLabel(master = record_attendance_screen, text="Enter username", width=120,height=25,fg_color=("white", "blue"),corner_radius=8);
    username_course.grid(row=3, column=2)
    
    username_entry = customtkinter.CTkEntry(master = record_attendance_screen, textvariable=username_course);
    username_entry.grid(row=3, column=3)
     
    
    # username_entry = customtkinter.CTkEntry(master = record_attendance_screen, textvariable=username_course);
    # username_entry.grid(row=2, column=3)

    date_entry = customtkinter.CTkLabel(master = record_attendance_screen, text="Enter the date of the class", width=120,height=25,fg_color=("white", "blue"),corner_radius=8);
    date_entry.grid(row=4, column=2)
    global date_entry_input
    date_entry_input = DateEntry(record_attendance_screen,width= 16, background= "magenta3", foreground= "white",bd=2)
    date_entry_input.grid(row=4, column=3, padx = 40, pady = 40)

    topic_entry = customtkinter.CTkLabel(master = record_attendance_screen,text="Topic Name", width=120,height=25,fg_color=("white", "blue"),corner_radius=8)
    topic_entry.grid(row = 5, column=2)
    global topic_entry_input
    topic_entry_input = customtkinter.CTkEntry(master = record_attendance_screen, textvariable = topic_name,)
    topic_entry_input.grid(row =5,  column = 3)

    submit_button_attendance = customtkinter.CTkButton(record_attendance_screen, text="Submit", command=send_data)
    submit_button_attendance.grid(row=6, column=3, padx = 40, pady = 40)
    
    
        
    
    

def view_attendance():
    print("Enter attendance")
    # Here Data of attendance will be shown 
# menu bar 
main_menu = Menu(root)
# Submenu for Home
m1 = Menu(main_menu, tearoff=0)
m1.add_command(label="Profile");
m1.add_separator()
m1.add_command(label="About Us", command= myfunc)
m1.add_command(label="Contact Us", command= myfunc)

main_menu.add_cascade(label="Home", menu=m1)
# Submenu for forms genration
m2 = Menu(main_menu, tearoff=0)
m2.add_command(label="Genrate Form for new Course", command=form_for_new_course);
m2.add_command(label="Gnerate Form for Next Level", command = form_for_higher_level);

main_menu.add_cascade(label = "Forms", menu = m2)
# Submenu for Attendance
m3 = Menu(main_menu, tearoff=0)
m3.add_command(label = " View Attendance", command=view_attendance)
m3.add_command(label="Record Attendance", command=record_attendance)

main_menu.add_cascade(label='Attendance', menu=m3);
# Submenu for Courses
m4 = Menu(main_menu, tearoff=0);
m4.add_command(label="Track all Courses");
m4.add_command(label="Track only one course");

main_menu.add_cascade(label="Courses", menu=m4);
# Submenu for Sign IN 
m5 = Menu(main_menu, tearoff = 0);
m5.add_command(label="Login as Director", command= login_director);
m5.add_command(label="Login as Assistant Director", command= login_assistant_director);
m5.add_command(label="Login as an Area Leader", command= login_admin);
m5.add_command(label="Login as a Course Ordinator", command= login_courseord);
m5.add_command(label="Login as a Frontliner", command = login_attendence);

main_menu.add_cascade(label="Sign In", menu=m5);
m6 = Menu(main_menu, tearoff=0)
m6.add_command(label="Register as a new user", command= register_window_main);
main_menu.add_cascade(label="Register User", menu=m6)



# Left frame 
frame_left = customtkinter.CTkFrame(master = frame, width=180,corner_radius=0)
frame_left.grid(row=0, column=0,  sticky = "nswe")

# Right Frame 
frame_right = customtkinter.CTkFrame(master= frame)
frame_right.grid(row=0, column=1, sticky="nswe", padx = 20, pady=20)
#Left Frame structure ready
frame_left.grid_rowconfigure(0, minsize=10)
frame_left.grid_rowconfigure(5, weight=1)
frame_left.grid_rowconfigure(8, minsize=20)
frame_left.grid_rowconfigure(11, minsize=10)

label_1 = customtkinter.CTkLabel(master=frame_left, text="Krishna's Soul", font=("Roboto Medium", -16))
label_1.grid(row=1, column=0, pady=10, padx =10)

button_1 = customtkinter.CTkButton(master=frame_left, text="Director Window", command=login_director)
button_1.grid(row=2, column=0, pady=10, padx=20)

button_2 = customtkinter.CTkButton(master=frame_left, text="Assistant Director Window", command=login_assistant_director)
button_2.grid(row=3, column=0, pady=10, padx=20)

button_3 = customtkinter.CTkButton(master=frame_left, text="Area Leader Window", command=login_area_leader)
button_3.grid(row=4, column=0, pady=10, padx=20)


button_4 = customtkinter.CTkButton(master=frame_left, text="Course ordinator Window", command=login_courseord)
button_4.grid(row=5, column=0, pady=10, padx=20)

button_5 = customtkinter.CTkButton(master=frame_left, text="Frontliner Window")
button_5.grid(row=6, column=0, pady=10, padx=20)
label_mode = customtkinter.CTkLabel(master=frame_left, text="Appearance Mode:")
label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

optionmenu_1 = customtkinter.CTkOptionMenu(master = frame_left,values=["Light", "Dark", "System"],command=change_appearance_mode )
optionmenu_1.grid(row=10, column=0, pady=10, padx=20,sticky = "w")


# Right Frame 
# configure grid layout
frame_right.rowconfigure((0, 1, 2, 3), weight=1)
frame_right.rowconfigure(7, weight=10)
frame_right.columnconfigure((0, 1), weight=1)
frame_right.columnconfigure(2, weight=0)

frame_info = customtkinter.CTkFrame(master= frame_right)
frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

# frame_info 
frame_info.rowconfigure(0, weight=1)
frame_info.columnconfigure(0, weight=1)

label_info_1 = customtkinter.CTkLabel(master=frame_info,
                                      text="Ongoing Courses will be displayed here ",
                                      height=100,
                                      corner_radius=6,  # <- custom corner radius
                                      fg_color=("white", "gray38"),  # <- custom tuple-color
                                      justify=LEFT)
label_info_1.grid(column=0, row=0, sticky="nwe",padx=15, pady=15)
root.config(menu = main_menu)
root.mainloop()