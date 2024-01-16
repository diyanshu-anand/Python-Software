from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import customtkinter
from main import login_director;
from main import login_area_leader;
from main import login_courseord;
from main import login_attendence;
from main import myfunc;
from main import form_for_new_course;
from main import form_for_higher_level;
from main import view_attendance;
from main import record_attendance;
from main import login_admin;
from main import register_window_main;
from main import change_appearance_mode;
import mysql.connector;

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
connectiondb = mysql.connector.connect(host="localhost", username="root", password="divya_131203", database ="courseordinators");
courseodb = connectiondb.cursor();

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
label_1 = customtkinter.CTkLabel(master=frame_left, text="Krishna's Soul", text_font=("Roboto Medium", -16))
label_1.grid(row=1, column=0, pady=10, padx =10)
button_2 = customtkinter.CTkButton(master=frame_left, text="Assign Area Leader")
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