from tkinter import ttk
import tkinter as tk
from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://root:divya_131203@localhost/courseordinators")  

# Creating tkinter my_w
my_w = tk.Tk()
my_w.geometry("400x280") 
my_w.title("www.plus2net.com")  
# Using treeview widget
trv = ttk.Treeview(my_w, selectmode ='browse')
  
trv.grid(row=1,column=1,padx=20,pady=20)
# number of columns
trv["columns"] = ("1", "2", "3","4","5")
  
# Defining heading
trv['show'] = 'headings'
  
# width of columns and alignment 
trv.column("1", width = 30, anchor ='c')
trv.column("2", width = 80, anchor ='c')
trv.column("3", width = 80, anchor ='c')
trv.column("4", width = 80, anchor ='c')
trv.column("5", width = 80, anchor ='c')
  
# Headings  
# respective columns
trv.heading("1", text ="id")
trv.heading("2", text ="Name")
trv.heading("3", text ="Class")
trv.heading("4", text ="Mark")  
trv.heading("5", text ="Gender")

# getting data from MySQL student table 
r_set=my_conn.execute('''SELECT * from student LIMIT 0,10''')
for dt in r_set: 
    trv.insert("", 'end',iid=dt[0], text=dt[0],
               values =(dt[0],dt[1],dt[2],dt[3],dt[4]))
my_w.mainloop()