# Import the required libraries
from tkinter import *
from tkinter import ttk
import mysql.connector


# Create an instance of tkinter frame
win = Tk()

# Databse connection 
connectiondb = mysql.connector.connect(host="localhost", username="root", password="divya_131203", database ="courseordinators");
my_conn = connectiondb.cursor();

# Set the size of the tkinter window
win.geometry("700x350")

# Create an object of Style widget
style = ttk.Style()
style.theme_use('clam')

# Using treeview widget
trv = ttk.Treeview(win, selectmode ='browse')
  
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
r_set=my_conn.execute('''SELECT * from gita''')
for dt in r_set: 
    trv.insert("", 'end',iid=dt[0], text=dt[0],
               values =(dt[0],dt[1],dt[2],dt[3],dt[4]))




win.mainloop()