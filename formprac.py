from cProfile import label
from tkinter import *

from tkinter import *

root =Tk()
root.geometry("655x333")



frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

number_of_inputs = int(input("Enter the number of questions you want"))
def my_check():
    my_flag=False
    for w in ref:
        if(len(w.get())<3):
            #print(w.get())
            my_flag=True
    if(my_flag==False):
        l1.config(text="Form can be submitted",fg='green')
    else:
        l1.config(text="Fill all the entries",fg='red' )
    l1.after(3000, lambda: l1.config(text=''))
ref=[] # to store the references 
for j in range(number_of_inputs):
    
    l=Label(frame,text='Question Number: '+str(j+1),font=20,fg='blue')
    l.grid(row=j,column=0,padx=3)

    e =Entry(frame, bg='lightyellow', borderwidth=1, width=20, font=('Arial', 24), cursor="arrow") 
    e.grid(row=j, column=1,padx=10,pady=3)

    image_button = Button(frame, text="image");
    image_button.grid(row=j, column=2, padx=40, pady=3)

        # Dropdown menu 
    menu = StringVar()
    menu.set("Select Type of question")

    # Create dropdown menu 
    drop = OptionMenu(frame, menu,"MCQ","sINGLe aNSWER" )
    drop.grid(row=j, column=3, padx=10, pady=3)

    ref.append(e) # store references 
b1=Button(frame,text='Submit',
bg='lightgreen',command=lambda: my_check(),font=18)
b1.grid(row=j+1,column=0,padx=3,pady=5)

l1=Label(frame,text='Output here',font=20) # display message
l1.grid(row=j+1,column=1)


root.mainloop()

# untitled_question_01 = Entry(question_screen, textvariable= untitled_form_input_01, borderwidth=1, width=20, font=('Arial', 24), cursor="arrow")  
#         untitled_question_01.grid(row=j, column=1,padx=10,pady=3) 
#         untitled_question_01.insert("0","Untitled Question")
#         image_button = Button(question_screen, image=icon_img);
#         image_button.place(x=750, y=320)
    
#         # Dropdown menu 
#         menu = StringVar()
#         menu.set("Select Type of question")

#         # Create dropdown menu 
#         drop = OptionMenu(question_screen, menu,"MCQ","sINGLe aNSWER" )
#         drop.place(x=800, y=320)
    
#         bold_button = Button(question_screen, image=icon_bold);
#         bold_button.place(x=380, y=360)
    
#         italic_button = Button(question_screen, image=icon_italic);
#         italic_button.place(x=410, y=360)

#         underline_button = Button(question_screen, image=icon_underline);
#         underline_button.place(x=440, y=360)

#         link_button = Button(question_screen, image=icon_link);
#         link_button.place(x=470, y=360)

#         duplicate_button = Button(question_screen, image = icon_duplicate);
#         duplicate_button.place(x=750, y=500)

#         remove_button = Button(question_screen, image=icon_delete);
#         remove_button.place(x=800, y=500)