# from cProfile import label
# from cgitb import text;
# import hashlib;
# from lib2to3.pgen2.token import RIGHTSHIFT; 
# import os;
# from logging import root;
# from msilib.schema import Font
# from sre_parse import State;
# from tkinter import *;
# from tkinter import font;
# from tkinter.tix import PopupMenu, Select
# from tokenize import String;
# from turtle import color, left, position;
# import tkinter.messagebox
# import weakref;
# from tkcalendar import DateEntry, Calendar;
# import webbrowser
# import customtkinter
# import mysql.connector;
# # from main import username_verify_filler;
# # from main import logged_destroy_filler;
# from main import disable_items;
# from sqlalchemy import create_engine;
# WIDTH = 780;
# HEIGHT = 520;

# root= customtkinter.CTk()
# root.geometry(f"{WIDTH}x{HEIGHT}")
# root.title("Krishna's Soul");


#         # configure grid layout (2x1)
# root.grid_columnconfigure(1, weight=1)
# root.grid_rowconfigure(0, weight=1)
# frame = customtkinter.CTkFrame(master =root, width=200,height = 200, corner_radius=10)
# frame.pack(side=LEFT, anchor="nw")
# global username_verify_login_attendance

# root.mainloop()




# # customtkinter.CTkLabel(frame, text = "Login successfully done as a filler... Welcome {}".format(username_verify_login_attendance.get()),fg_color=("gray75", "blue"),corner_radius=8).pack();
# #     customtkinter.CTkLabel(frame, text="").pack();
# #     customtkinter.CTkButton(frame, text="Let's fill it.", width=120,height=32,border_width=0,corner_radius=8 , command=lambda:[logged_destroy_filler(), disable_items()]).pack();




from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://root:divya_131203@localhost/courseordinators")
#my_conn = create_engine("sqlite:///D:\\testing\\sqlite\\my_db.db")

query="SELECT DISTINCT(class) as class FROM student"
                
my_data=my_conn.execute(query) # SQLAlchem engine result
my_list = [r for r, in my_data] # create a  list 

import tkinter as tk
from tkinter import ttk
my_w = tk.Tk()
my_w.geometry("300x150")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title

cb1 = ttk.Combobox(my_w, values=my_list,width=15)
cb1.grid(row=1,column=1,padx=30,pady=30)
cb1.current(2) # default selected option
my_w.mainloop()  # Keep the window open