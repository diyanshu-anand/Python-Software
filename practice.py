# # from tkinter import *

# # from tkinter import *

# # root =Tk()
# # root.geometry("655x333")

# # def hello():
# #     print("Hello tkinter Buttons")

# # def name():
# #     print("Name is harry")

# # frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
# # frame.pack(side=LEFT, anchor="nw")

# # b1 = Button(frame, fg="red", text="Print now", command=hello)
# # b1.pack(side=LEFT, padx=23)

# # b2 = Button(frame, fg="red", text="Tell me name now", command=name)
# # b2.pack(side=LEFT, padx=23)

# # b3 = Button(frame, fg="red", text="Print now")
# # b3.pack(side=LEFT, padx=23)

# # b4 = Button(frame, fg="red", text="Print now")
# # b4.pack(side=LEFT, padx=23)
# # root.mainloop()


# #     # # get username and password 
# #     #         username3 = username_verify_login_courseord.get();
# #     #         password_courseord3 = password_verify_login_courseord.get();
        
# #     #     # below we will delete inputs from the functions 
# #     #         username_login_entry.delete(0, END)
# #     #         password_login_entry.delete(0, END)
        
# #     #     # this method list the names contained in the directory
# #     #         username_info_coord = 
# #     #         file = open(username_info_cord)
# #     #         list_of_files = os.listdir();

# #     #     # verification of username and password 
# #     #         if username3 in list_of_files:
# #     #             file1 = open(username3, "r")
# #     #             verify = file1.read().splitlines()
# #     #             login_success_coord()
# #     #         else:
# #     #             print("user_not_found");

# #     #     user_verification = username_verify_login_courseord.get();
# #     #     password_verification = password_verify_login_courseord.get();
# #     #     sql = "select * from userinfo where username = %s and Hashed_password = %s";
# #     #     courseodb.execute(sql,[(user_verification),(password_verification)])
# #     #     results = courseodb.fetchall();  
# #     #     if results:
# #     #         for i in results:
# #     #             login_success_coord();
# #     #             break
# #     #     else:
# #     #         print("login failed");

# print(1+'10');
from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Codemy.com - Learn To Code!')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x650")

# Read only r  
# Read and Write r+  (beginning of file)
# Write Only w   (over-written)
# Write and Read w+  (over written)
# Append Only a  (end of file)
# Append and Read a+  (end of file)


def open_txt():
	text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
	name = text_file
	name = name.replace("C:/gui/", "")
	name = name.replace(".txt", "")
	
	text_file = open(text_file, 'r')
	stuff = text_file.read()

	my_text.insert(END, stuff)
	text_file.close()

	root.title(f'{name} - Textpad')


def save_txt():
	text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
	text_file = open(text_file, 'w')
	text_file.write(my_text.get(1.0, END))

def add_image():
	# Add image
	global my_image
	my_image = PhotoImage(file="images/profile.png")
	position = my_text.index(INSERT)
	my_text.image_create(position, image=my_image)

	my_label.config(text=position)

def select():
	selected = my_text.selection_get()
	my_label.config(text=selected)

def bolder():
	bold_font = font.Font(my_text, my_text.cget("font"))
	bold_font.configure(weight="bold")

	my_text.tag_configure("bold", font=bold_font)

	current_tags = my_text.tag_names("sel.first")

	if "bold" in current_tags:
		my_text.tag_remove("bold", "sel.first", "sel.last" )
	else:
		my_text.tag_add("bold", "sel.first", "sel.last" )


def italics_it():
	italics_font = font.Font(my_text, my_text.cget("font"))
	italics_font.configure(slant="italic")

	my_text.tag_configure("italic", font=italics_font)
	current_tags = my_text.tag_names("sel.first")

	if "italic" in current_tags:
		my_text.tag_remove("italic", "sel.first", "sel.last" )
	else:
		my_text.tag_add("italic", "sel.first", "sel.last" )


my_frame = Frame(root)
my_frame.pack(pady=10)

# Create scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=40, height=10, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", yscrollcommand=text_scroll.set, undo=True)
my_text.pack()

# Configure our scrollbar
text_scroll.config(command=my_text.yview)


open_button = Button(root, text="Open Text File", command=open_txt)
open_button.pack(pady=20)

save_button = Button(root, text="Save File", command=save_txt)
save_button.pack(pady=20)

image_button = Button(root, text="Add Image", command=add_image)
image_button.pack(pady=5)

select_button = Button(root, text="Select Text", command=select)
select_button.pack(pady=5)

bold_button = Button(root, text="Bold", command=bolder)
bold_button.pack(pady=5)

italics_button = Button(root, text="Italics", command=italics_it)
italics_button.pack(pady=5)

my_label = Label(root, text="")
my_label.pack()

undo_button = Button(root, text="Undo", command=my_text.edit_undo)
undo_button.pack(pady=5)

redo_button = Button(root, text="Redo", command=my_text.edit_redo)
redo_button.pack(pady=5)


root.mainloop()

# Question formation
    # def select():
    #     selected = untitled_form_input_01.selection_get()
    #     question_screen.config(text=selected)
    # def boldon():
    #     bold_font = font.Font(untitled_form_input_01, untitled_form_input_01.get("font"))
    #     bold_font.configure(weight="bold");

    #     untitled_form_input_01.tag_configure("bold", font=bold_font)

    #     current_tag = untitled_form_input_01.tag_names('sel.first')

    #     if "bold" in current_tag:
    #         untitled_form_input_01.tag_remove("bold", "sel.first", "sel.last")
    #     else:
    #         untitled_form_input_01.tag_add("bold", "sel.first", "sel.last")
    # def addon():
    #         untitled_question_02 = Entry(question_screen, textvariable= untitled_form_input_02, borderwidth=1, width=20, font=('Arial', 24), cursor="arrow")
    #         untitled_question_02.place(y=400, x=380)

    #         image_button = Button(question_screen, image=icon_img);
    #         image_button.place(x=750, y=400)

    #         # Dropdown menu 
    #         menu = StringVar()
    #         menu.set("Select Type of question")

    #         # Create dropdown menu 
    #         drop = OptionMenu(question_screen, menu,"MCQ","sINGLe aNSWER" )
    #         drop.place(x=800, y=400)
            
    #         bold_button = Button(question_screen, image=icon_bold);
    #         bold_button.place(x=380, y=440)
            
    #         italic_button = Button(question_screen, image=icon_italic);
    #         italic_button.place(x=410, y=440)
            
    #         underline_button = Button(question_screen, image=icon_underline);
    #         underline_button.place(x=440, y=440)

    #         link_button = Button(question_screen, image=icon_link);
    #         link_button.place(x=470, y=440)

    #         duplicate_button = Button(question_screen, image = icon_duplicate);
    #         duplicate_button.place(x=750, y=520)

    #         remove_button = Button(question_screen, image=icon_delete);
    #         remove_button.place(x=800, y=520)
            
    #         add_button = Button(question_screen, image=icon_add, width=30, height=30, command=addon2)
    #         add_button.place(x=1050, y=400)
    #         add_button = PhotoImage(file='add.png')
    # def addon2():
    #     untitled_question_03 = Entry(question_screen, textvariable= untitled_form_input_03, borderwidth=1, width=20, font=('Arial', 24), cursor="arrow")
    #     untitled_question_03.place(y=480, x=380)
    #     untitled_question_03.insert("0","Untitled Question")

    #     image_button = Button(question_screen, image=icon_img);
    #     image_button.place(x=750, y=480)

    #     # Dropdown menu 
    #     menu = StringVar()
    #     menu.set("Select Type of question")

    #     # Create dropdown menu 
    #     drop = OptionMenu(question_screen, menu,"MCQ","sINGLe aNSWER" )
    #     drop.place(x=800, y=480)
        
    #     bold_button = Button(question_screen, image=icon_bold);
    #     bold_button.place(x=380, y=520)
        
    #     italic_button = Button(question_screen, image=icon_italic);
    #     italic_button.place(x=410, y=520)
        
    #     underline_button = Button(question_screen, image=icon_underline);
    #     underline_button.place(x=440, y=520)

    #     link_button = Button(question_screen, image=icon_link);
    #     link_button.place(x=470, y=520)
        
    #     add_button = Button(question_screen, image=icon_add, width=30, height=30, command=addon3)
    #     add_button.place(x=1050, y=480)
    #     add_button = PhotoImage(file='add.png')
    # def addon3():

	# icon_italic = PhotoImage(file="icons8-italic-16.png")

    # icon_underline = PhotoImage(file="icons8-underline-16.png")

    # icon_link = PhotoImage(file="icons8-add-link-16.png")

    # icon_img  = PhotoImage(file="icons8-images-24.png")

    # icon_duplicate = PhotoImage(file="icons8-duplicate-24.png")

    # icon_delete = PhotoImage(file="icons8-remove-24.png")

	# icon_bold = PhotoImage(file="bold.png")
    
    # icon_add = PhotoImage(file="add.png");

	# frame_question.place(x=600)
    # untitled_form_input = StringVar();
    # untitled_form_question = StringVar();
    # untitled_description = StringVar();
    # #LABELs To be filled.
    # untitled_question_entry = Entry(question_screen, textvariable= untitled_form_input, borderwidth=1, width=20, font=('Arial', 42), cursor="arrow");
    # untitled_question_entry.place(y=220, x=380);
    # untitled_question_entry.insert("0", "Untitled Form");
    # untitled_description = Entry(question_screen, textvariable = untitled_description, borderwidth=0, width=69,font=('Arial', 12));
    # untitled_description.place(y=290, x=380);
    # untitled_description.insert("0","Untitled Description");
