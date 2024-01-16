# def Question_screen_higher_level():
#     print("Its Working")
#     global Question_screen_higher;
#     global course_name;
#     global username_course;
    
#     Question_screen_higher = Toplevel(new_high_form_screen);
#     Question_screen_higher.title("Question Genrator");
#     Question_screen_higher.geometry("300x100");

#     username_course = StringVar()
#     course_name = StringVar()

#     username = Label(Question_screen_higher, text="Username *")
#     username.grid(row=1, column=2)
#     username_login_entry = Entry(Question_screen_higher, textvariable = username_course);
#     username_login_entry.grid(row=1, column=3, padx=40, pady=40)
    
#     course = Label(Question_screen_higher, text="Enter the course name you were enrolled previously")
#     course.grid(row=2, column=2)
#     course_name_entry = Entry(Question_screen_higher, textvariable=course_name);
#     course_name_entry.grid(row=2, column=3)




# Form Part begins here 
# #New Form Genration.
# def Question_screen():
#     global question_screen;
#     global untitled_form_input;
#     global untitled_description;
#     global untitled_form_question;
#     question_screen = Toplevel(new_form_screen);
#     question_screen.title("Question Genrator");
#     question_screen.geometry("300x100");
#     frame_question = Frame(question_screen, borderwidth=6, bg="white", relief=SUNKEN);
    
#     # Question Labels to be filled.
#     global untitled_question_01
#     global untitled_question_02
#     global untitled_question_03
#     global untitled_question_04
#     global untitled_form_input_01
#     global untitled_form_input_02
#     global untitled_form_input_03
#     global untitled_form_input_04

#     untitled_form_input_01 = StringVar()
#     untitled_form_input_02 = StringVar()
#     untitled_form_input_03 = StringVar()
#     untitled_form_input_04 = StringVar()

#     # Button icon 
    
#     icon_italic = PhotoImage(file="icons8-italic-16.png")

#     icon_underline = PhotoImage(file="icons8-underline-16.png")

#     icon_link = PhotoImage(file="icons8-add-link-16.png")

#     icon_img  = PhotoImage(file="icons8-images-24.png")

#     icon_duplicate = PhotoImage(file="icons8-duplicate-24.png")

#     icon_delete = PhotoImage(file="icons8-remove-24.png")

#     icon_bold = PhotoImage(file="bold.png")

	
#     # 
#     # # Create scrollbar
#     # text_scroll = Scrollbar(question_screen)
#     # text_scroll.pack(side=RIGHT, fill=Y)
    
    

#     number_of_questions = int(input("Enter the number of questions you want"));
    
#     def show(event):
#         mylabel.config(text=clicked.get())
#         if clicked.get() == "MCQ":
#             print("It's MCQ")
#             ref_mcq=[]
#             for i in range(6):
#                 e_mcq =Entry(question_screen, bg='lightyellow', borderwidth=0, width=20, font=('Arial', 24), cursor="arrow") 
#                 e_mcq.grid(row=i, column=1,padx=20,pady=30)

#                 ref_mcq.append(e_mcq)

#         elif clicked.get() == "SHORT ANSWER":
#             print("It's SA")
#             ref_short=[]
#             for i in range(3):
#                 e_short =Entry(question_screen, bg='lightyellow', borderwidth=0, width=20, font=('Arial', 24), cursor="arrow") 
#                 e_short.grid(row=i, column=1,padx=20,pady=30)

#                 ref_short.append(e_short)
            

        
#     clicked = StringVar()
#     clicked.set("MCQ")
    

#     ref =[] #to store refrences
#     for j in range(number_of_questions):
#         l=Label(question_screen,text='Question Number: '+str(j+1),font=20,fg='blue')
#         l.grid(row=j,column=0,padx=3)

#         e =Entry(question_screen, bg='lightyellow', borderwidth=1, width=20, font=('Arial', 24), cursor="arrow") 
#         e.grid(row=j, column=1,padx=20,pady=30)

#         image_button = Button(question_screen, image=icon_img);
#         image_button.grid(row=j, column=2, padx=10, pady=3)
#         options = [
#         "MCQ",
#         "SHORT ANSWER"]

#         # Create dropdown menu 
#         drop = OptionMenu(question_screen, clicked, *options, command = show )
#         drop.grid(row=j, column=3, padx=10, pady=3)

        
  

        

#         mylabel = Label(question_screen, text="")
#         mylabel.grid(row=3, column=3)

#         # drop_button = Button(question_screen, text="Submit", command=show)
#         # drop_button.grid(row=j, column=4, padx=10, pady=3)

#         bold_button = Button(question_screen, image=icon_bold);
#         bold_button.grid(row=j, column=5, padx=10, pady=3)

#         italic_button = Button(question_screen, image=icon_italic);
#         italic_button.grid(row=j, column=6, padx=10, pady=3)

#         underline_button = Button(question_screen, image=icon_underline);
#         underline_button.grid(row=j, column=7, padx=10, pady=3)

#         link_button = Button(question_screen, image=icon_link);
#         link_button.grid(row=j, column=8, padx=10, pady=3);

#         ref.append(e) # store references 



    
    
    
# def Response_screen_higher_level():
#     print("It's Working")



# def Response_screen():
    # print("Its Working")