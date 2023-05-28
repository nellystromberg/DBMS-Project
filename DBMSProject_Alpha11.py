import os
from PIL import Image
from sys import platform
import customtkinter
import ctypes
from tkinter import messagebox

root = customtkinter.CTk()
root.title("Library of Alexandria")
#root.iconify()
root.iconbitmap('./Login-System/book.ico')
root.geometry("800x500")

main_frame=customtkinter.CTkFrame(root,
                                  width=1600,
                                  height=1000, 
                                  fg_color="white"
                                  )
main_frame.place(x=0,y=0)

# Canvas
main_canvas=customtkinter.CTkCanvas(root,
                                    width=2000,
                                    height=1000
                                    )
main_canvas.place(x=0,y=0)

# Load user image
header = customtkinter.CTkImage(Image.open("./Login-System/The_Library.png"),
                                        size=(300, 80))

# Header Label 
labelA = customtkinter.CTkLabel(main_canvas, 
                                   width=1600, 
                                   height=150, 
                                   fg_color="#385B43", 
                                   text=""
                                   )
labelA.place(x=0, y=0)

labelA_logo = customtkinter.CTkLabel(labelA, 
                                   width=300, 
                                   height=80, 
                                   fg_color="#385B43", 
                                   text=""
                                   )
labelA_logo.place(x=0, y=0)


def combobox_callback(choice):

    if choice =="My pages":
        my_pages()
    if choice == "Borrow a book":
        borrowing()
    if choice == "Return a book":
        returning()
    if choice == "Extend a loan":
        extending()
    if choice == "Customer info":
        customers()
    if choice == "Home":
        home()

combobox_var = customtkinter.StringVar()

combobox = customtkinter.CTkComboBox(labelA, 
                                     values=["My pages", "Borrow a book", "Return a book","Extend a loan", "Customer info", "Home"],
                                     width=1300,
                                     height=30,
                                     command=combobox_callback, 
                                     variable=combobox_var,
                                     justify="center",
                                     font=("Robot bold", 20),
                                     dropdown_font=("Robot bold", 20),
                                     hover=True,
                                     border_color="black",
                                     fg_color="#385B43",
                                     button_color="light grey",
                                     button_hover_color="grey",
                                     dropdown_hover_color="light grey",
                                     
                                     )

combobox_var.set("My pages")
combobox.place(x=115, y=100)


def home():
    labelB=customtkinter.CTkLabel(main_canvas, 
                             width=1600, 
                             height=1000, 
                             fg_color="white", 
                             text=" "
                             )
    labelB.place(x=0, y=150)
    # Opening hours and events Label 
    label_open_time=customtkinter.CTkLabel(labelB, 
                             width=380, 
                             height=350, 
                             fg_color="white", 
                             text="",
                             corner_radius=7,
                             
                             )
    label_open_time.place(x=1100, y=300)
    # Opening hours and events Frame
    open_time_frame = customtkinter.CTkFrame(label_open_time, 
                                         width=380,
                                        height=350, 
                                         fg_color="white",
                                         bg_color="white",
                                         border_color="white",
                                         border_width=10
                                         )
    open_time_frame.place(x=0, y=0)
    # Opening hours and events Canvas 
    open_time_canvas= customtkinter.CTkCanvas(open_time_frame, 
                                          width=420, 
                                          height=420, 
                                          bg="white",
                                          
                                          )
    open_time_canvas.place(x=5,y=5)
    # Opening hours and events Scroll 
    open_time_scroll = customtkinter.CTkScrollbar(open_time_frame, 
                                               orientation="vertical", 
                                               command=open_time_canvas.yview, 
                                               height=235,
                                               corner_radius=7,
                                               fg_color="white",
                                               bg_color="white"
                                               )
    open_time_scroll.place(x=340,y=5)
    open_time_canvas.configure(yscrollcommand=open_time_scroll.set)
    open_time_canvas.bind('<Configure>', lambda e: open_time_canvas.configure(scrollregion=open_time_canvas.bbox("all")))
    # Opening hours and events second Frame
    second_open_time_frame = customtkinter.CTkFrame(open_time_canvas,
                                                fg_color="white",
                                                corner_radius=7,
                                                bg_color="white",
                                                border_color="white",
                                                border_width=10
                                                )
    open_time_canvas.create_window((0,0), 
                               window=second_open_time_frame, 
                               anchor="nw",
                               width=420,
                               height=1000,
                               
                               )
    #open_time_title=customtkinter.CTkLabel(labelB, text="Opening hours and events. \n For the library of alexandria.") 
    #open_time_title.place(x=1190, y=80)

    def tuesday_button_function():
        tuesday_button.destroy()
    def create_tuesday_button():
        global tuesday_button
        tuesday_button = customtkinter.CTkButton(second_open_time_frame,
                                                 text="The kid's Book Club \n Ages:8-13\n 16.00-17.30",
                                                 font=("robot bold", 15),
                                                 fg_color="#547B60",
                                                 hover_color="#547B60",
                                                 command=tuesday_button_function)
        tuesday_button.grid(row=2, column=1, pady=5, padx=1, sticky="nsew")

    def thursday_button_function():
        thursday_button.destroy()
    def create_thursday_button():
        global thursday_button
        thursday_button = customtkinter.CTkButton(second_open_time_frame,
                                                 text="Book reading by Local authors \n For further information \n contact liza@alexandria.nl ",
                                                 font=("robot bold", 15),
                                                 fg_color="#547B60",
                                                 hover_color="#547B60",
                                                 command=thursday_button_function)
        thursday_button.grid(row=5, column=1, pady=5, padx=1, sticky="nsew")



    for thing in range(12):
        if thing == 0:
            customtkinter.CTkButton(second_open_time_frame,
                                text="Monday \n 10.00-20.00", 
                                font=("robot bold", 15),
                                fg_color="#547B60",
                                hover_color="#547B60",
                                width=300 ).grid(row=thing,
                                                            column=1, 
                                                            pady=5,
                                                            padx=1,
                                                            sticky="nsew"
                                                            )
        if thing == 1:
            customtkinter.CTkButton(second_open_time_frame,
                                text="Tuesday \n 10.00-20.00", 
                                font=("robot bold", 15),
                                fg_color="#547B60",
                                hover_color="#547B60",
                                command=create_tuesday_button).grid(row=thing,
                                                            column=1, 
                                                            pady=5,
                                                            padx=1,
                                                            sticky="nsew" 
                                                            )

        if thing == 3:
            customtkinter.CTkButton(second_open_time_frame,
                                text="Wednesday \n 10.00-21.00", 
                                font=("robot bold", 15),
                                fg_color="#547B60",
                                hover_color="#547B60").grid(row=thing,
                                                            column=1, 
                                                            pady=5,
                                                            padx=1,
                                                            sticky="nsew"
                                                            )                                                                   
        if thing == 4:
            customtkinter.CTkButton(second_open_time_frame,text="Thursday \n 10.00-20.00", 
                                font=("robot bold", 15),
                                fg_color="#547B60",
                                hover_color="#547B60",
                                command=create_thursday_button).grid(row=thing,
                                                            column=1, 
                                                            pady=5,
                                                            padx=1,
                                                            sticky="nsew"
                                                            )    
  
        if thing == 6:
            customtkinter.CTkButton(second_open_time_frame,
                                text="Friday \n 10.00-21.00", 
                                font=("robot bold", 15),
                                fg_color="#547B60",
                                hover_color="#547B60").grid(row=thing,
                                                            column=1, 
                                                            pady=5,
                                                            padx=1,
                                                            sticky="nsew"
                                                            )
        if thing == 7:
            customtkinter.CTkButton(second_open_time_frame,
                                text="Saturday \n 12.00-20.00", 
                                font=("robot bold", 15),
                                fg_color="#547B60",
                                hover_color="#547B60").grid(row=thing,
                                                            column=1, 
                                                            pady=5,
                                                            padx=1,
                                                            sticky="nsew"
                                                            )
        if thing == 8:
            customtkinter.CTkButton(second_open_time_frame,
                                text="Sunday \n 12.00-18.00", 
                                font=("robot bold", 15),
                                fg_color="#547B60",
                                hover_color="#547B60").grid(row=thing,
                                                            column=1, 
                                                            pady=5,
                                                            padx=1,
                                                            sticky="nsew"
                                                            
                                                        )
        if thing == 9:
            customtkinter.CTkButton(second_open_time_frame,
                       text="New Button", 
                       font=("robot bold", 15),
                       fg_color="#547B60",
                       hover_color="#547B60",
                       command=create_thursday_button).grid(row=thing + 1,
                                                       column=1, 
                                                       pady=5,
                                                       padx=1,
                                                       sticky="nsew")

    #Home screen Images
    img1 = customtkinter.CTkImage(Image.open("./Login-System/1D.png"),
                                        size=(900, 550))
    img2 = customtkinter.CTkImage(Image.open("./Login-System/2D.png"),
                                        size=(900, 550))
    img3 = customtkinter.CTkImage(Image.open("./Login-System/3D.png"),
                                        size=(900, 550))
    img4 = customtkinter.CTkImage(Image.open("./Login-System/4D.png"),
                                        size=(900, 550))
    img5 = customtkinter.CTkImage(Image.open("./Login-System/5D.png"),
                                        size=(900, 550))
    info=customtkinter.CTkLabel(labelB, 
                             width=900, 
                             height=600, 
                             fg_color="white", 
                             text=""
                             )
    info.place(x=110, y=100)
    info2=customtkinter.CTkLabel(info, 
                             width=900, 
                             height=550, 
                             fg_color="white", 
                             text="",
                             image=img1
                             )
    info2.place(x=0, y=0)
    info_radio=customtkinter.CTkLabel(info, 
                             width=900, 
                             height=30, 
                             fg_color="light grey", 
                             text=" ",
                             bg_color="white"
                             )
    info_radio.place(x=0,y=520)

    var=customtkinter.IntVar()
    def section():
        choice = var.get()
        if choice == 0:
            info2.configure(image=img1)
        elif choice == 1:
            info2.configure(image=img2)
            radiobutton1.configure(state="normal")
        elif choice == 2:
            info2.configure(image=img3)
        elif choice == 3:
            info2.configure(image=img4)
        elif choice == 4:
            info2.configure(image=img5)
        else:
            info2.configure(image=img1)

    def increment_var():
        var.set(var.get() + 1)
        if var.get() == 6:
            var.set(1)
        section()

    def decrement_var():
        var.set(var.get() - 1)
        if var.get() == 0:
            var.set(5)
        section()

    # Radio Button 
    #1
    radiobutton1 = customtkinter.CTkRadioButton(info_radio, text="", variable=var, value=1, command=section, corner_radius=10, state="disabeled")
    radiobutton1.place(x=360,y=3)
    #2
    radiobutton2 = customtkinter.CTkRadioButton(info_radio, text="", variable=var, value=2, command=section, corner_radius=10)
    radiobutton2.place(x=390,y=3)
    #3
    radiobutton3 = customtkinter.CTkRadioButton(info_radio, text="", variable=var, value=3, command=section, corner_radius=10)
    radiobutton3.place(x=420,y=3)
    #4
    radiobutton4 = customtkinter.CTkRadioButton(info_radio, text="", variable=var, value=4, command=section, corner_radius=10)
    radiobutton4.place(x=450,y=3)
    #5
    radiobutton5 = customtkinter.CTkRadioButton(info_radio, text="", variable=var, value=5, command=section, corner_radius=10)
    radiobutton5.place(x=480,y=3)
    section()

    # fix these buttons
    right_radio_button =customtkinter.CTkButton(info_radio, 
                                            width=30,
                                            height=1,
                                            fg_color="light grey", 
                                            hover_color="grey",
                                            text=">",
                                            font=("Robot Bold", 20),
                                            command=increment_var,
                                            corner_radius=0,
                                            text_color="black"
                                            )
    right_radio_button.place(x=530, y=0)
    left_radio_button =customtkinter.CTkButton(info_radio, 
                                            width=30,
                                            height=1,
                                            fg_color="light grey", 
                                            hover_color="grey",
                                            text="<",
                                            command=decrement_var,
                                            font=("Robot Bold", 20),
                                            corner_radius=0,
                                            text_color="black"
                                            )
    left_radio_button.place(x=300, y=0)

    # Entry
    search_bar = customtkinter.CTkEntry(labelB, 
                                    width=1300,
                                    fg_color="white", 
                                    height=30, 
                                    font=("Robot bold",30),
                                    placeholder_text="Look up diffrent titles or authors here.",
                                    border_width=2,
                                    border_color="black"
                                    )
    search_bar.place(x=115, y=10)
    img6 = customtkinter.CTkImage(Image.open("./Login-System/frame2.png"),
                                        size=(360, 200))
    book_of_week=customtkinter.CTkLabel(labelB, 
                             width=300, 
                             height=200, 
                             fg_color="white", 
                             text=" ",
                             corner_radius=7,
                             image=img6
                             )
    book_of_week.place(x=1050, y=100)

    book_of_week_text=customtkinter.CTkLabel(book_of_week, 
                             width=255, 
                             height=106,
                             bg_color="white",
                             text="Book of the Week: \n The Communist Manifesto.", 
                             font=("Robot bold",20),
                             )
    book_of_week_text.place(x=60, y=46)
    home_button = customtkinter.CTkButton(labelA, 
                                        width=300, 
                                        height=80, 
                                        text="", 
                                        font=("Robot bold",24), 
                                        text_color="#385B43", 
                                        hover_color="grey",
                                        border_width=0,
                                        image=header,
                                        fg_color="#385B43",
                                        command=home
                                        )
    home_button.place(x=85, y=0)

    # Search Image 
    search_img = customtkinter.CTkImage(Image.open("./Login-System/search.png"),
                                        size=(29, 29))
    
    # Button
    search_button = customtkinter.CTkButton(search_bar, 
                                        width=30, 
                                        height=30, 
                                        fg_color="light grey", 
                                        text="", 
                                        font=("Robot bold",24), 
                                        text_color="#385B43", 
                                        hover_color="grey",
                                        border_width=0,
                                        image=search_img, 
                                        )
    search_button.place(x=1252, y=2)

# Function
def borrowing():
    def borrowing_button_command():
        customer=customer_id.get()
        book=book_id.get()
        print(customer, book)
        home()

    labelC=customtkinter.CTkLabel(main_canvas, 
                                 width=1600, 
                                 height=1000, 
                                 fg_color="white", 
                                 text=" "
                                 )
    labelC.place(x=0, y=150)
    labelC2=customtkinter.CTkLabel(labelC, 
                                 width=1300, 
                                 height=1000, 
                                 fg_color="#E2CFCF", 
                                 text=" "
                                 )
    labelC2.place(x=115, y=50)
    labelC_text=customtkinter.CTkLabel(labelC2, 
                                 width=50, 
                                 height=100, 
                                 fg_color="#E2CFCF", 
                                 text="To borrow a book you first need to enter your \ncustomer ID, then the book ID.\n \nThe book ID can be found on the back of the book. \nThen press the button Enter.",
                                 font=("Robot bold", 25),
                                 justify="left"
                                 )
    labelC_text.place(x=120, y=20)
    customer_id = customtkinter.CTkEntry(labelC2, 
                                         width=300, 
                                         font=("Robot bold",15)
                                         )
    customer_id_text = customtkinter.CTkLabel(labelC2, 
                                              text="Customer ID:", 
                                              font=("Robot bold",15)
                                              )
    customer_id.place(x=220, y=200)
    customer_id_text.place(x=120, y=200)
    book_id = customtkinter.CTkEntry(labelC2, 
                                     width=300,
                                     font=("Robot bold",15)
                                     )
    book_id_text = customtkinter.CTkLabel(labelC2, 
                                          text="Book ID:",
                                          font=("Robot bold", 15)
                                          )
    book_id.place(x=220, y=300)
    book_id_text.place(x=120, y=300)
    enter_button = customtkinter.CTkButton(labelC2, 
                                           text="Enter",
                                           font=("Robot bold",15),
                                           command=borrowing_button_command ,
                                           bg_color="#E2CFCF",
                                           fg_color="#385B43",
                                           hover="#5F9970",
                                           corner_radius=7
                                           )
    enter_button.place(x=220,y=350)

def returning():
    def returning_button_command():
        home()
    labelD=customtkinter.CTkLabel(main_canvas, 
                                 width=1600, 
                                 height=1000, 
                                 fg_color="white", 
                                 text=" "
                                 )
    labelD.place(x=0, y=150)
    labelD2=customtkinter.CTkLabel(labelD, 
                                 width=1300, 
                                 height=1000, 
                                 fg_color="#D6AF67", 
                                 text=" "
                                 )
    labelD2.place(x=115, y=50)
    labelD_text=customtkinter.CTkLabel(labelD2, 
                                 width=50, 
                                 height=100, 
                                 fg_color="#D6AF67", 
                                 text="To return a book you first need to enter the book's Book ID.\n \nThe Book ID can be found on the back of the book. \nThen press the button Enter.",
                                 font=("Robot bold", 25),
                                 justify="left"
                                 )
    labelD_text.place(x=120, y=20)

    book_id = customtkinter.CTkEntry(labelD2, 
                                     width=300,
                                     font=("Robot bold", 15)
                                     )
    book_id_text = customtkinter.CTkLabel(labelD2, 
                                          text="Book ID:",
                                          font=("Robot bold", 15)
                                          )
    book_id.place(x=220, y=300)
    book_id_text.place(x=120, y=300)

    enter_button = customtkinter.CTkButton(labelD2, 
                                           text="Enter",
                                           font=("Robot bold", 15), 
                                           command=returning_button_command,
                                           fg_color="#547B60",
                                           bg_color="#D6AF67",
                                           corner_radius=7
                                           )
    enter_button.place(x=220,y=350)

def extending():
    def extending_button_command():
        home()
    labelE=customtkinter.CTkLabel(main_canvas, 
                                 width=1600, 
                                 height=1000, 
                                 fg_color="white", 
                                 text=" "
                                 )
    labelE.place(x=0, y=150)
    labelE2=customtkinter.CTkLabel(labelE, 
                                 width=1300, 
                                 height=1000, 
                                 fg_color="#67A278", 
                                 text=" "
                                 )
    labelE2.place(x=115, y=50)
    labelE_text=customtkinter.CTkLabel(labelE2, 
                                 width=50, 
                                 height=100, 
                                 fg_color="#67A278", 
                                 text="To return a book you first need to enter the book's Book ID.\n \nThe Book ID can be found on the back of the book. \nThen press the button Enter.",
                                 font=("Robot bold", 25),
                                 justify="left"
                                 )
    labelE_text.place(x=120, y=20)
    book_id = customtkinter.CTkEntry(labelE2, 
                                     width=300,
                                     font=("Robot bold", 15)
                                     )
    book_id_text = customtkinter.CTkLabel(labelE2, 
                                          text="Book ID:",
                                          font=("Robot bold", 15)
                                          )
    book_id.place(x=220, y=300)
    book_id_text.place(x=120, y=300)

    enter_button = customtkinter.CTkButton(labelE2, 
                                           text="Enter",
                                           font=("Robot bold",15), 
                                           command=extending_button_command,
                                           bg_color="#67A278",
                                           fg_color="#385B43",
                                           corner_radius=7
                                           )
    enter_button.place(x=220,y=350)

def customers():
    def customer_button_command():
        home()
    labelF=customtkinter.CTkLabel(main_canvas, 
                                 width=1600, 
                                 height=1000, 
                                 fg_color="white", 
                                 text=" "
                                 )
    labelF.place(x=0, y=150)
    labelF2=customtkinter.CTkLabel(labelF, 
                                 width=1300, 
                                 height=1000, 
                                 fg_color="#B29696", 
                                 text=" "
                                 )
    labelF2.place(x=115, y=50)
    labelF_text=customtkinter.CTkLabel(labelF2, 
                                 width=50, 
                                 height=100, 
                                 fg_color="#B29696", 
                                 text="To return a book you first need to enter the book's Book ID.\n \nThe Book ID can be found on the back of the book. \nThen press the button Enter.",
                                 font=("Robot bold", 25),
                                 justify="left"
                                 )
    labelF_text.place(x=120, y=20)
    customer_id = customtkinter.CTkEntry(labelF2, 
                                         width=300, 
                                         font=("Robot bold",15)
                                         )
    customer_id_text = customtkinter.CTkLabel(labelF2, 
                                              text="Customer ID:", 
                                              font=("Robot bold",15)
                                              )
    customer_id.place(x=220, y=300)
    customer_id_text.place(x=120, y=300)

    enter_button = customtkinter.CTkButton(labelF2, 
                                           text="Enter",
                                           font=("Robot bold",15), 
                                           command=customer_button_command,
                                           bg_color="#B29696",
                                           fg_color="#795E5B",
                                           corner_radius=7
                                           )
    enter_button.place(x=220,y=350)

def my_pages():
    def edit_page():

        def new_customer_info():
            home()
            first_name = entry_G.get()
            last_name = entry_G1.get()
            user_name = entry_G2.get()
            phone_number = entry_G3.get()
            email_address = entry_G4.get()
            adress = entry_G5.get()
            house_number = entry_G6.get()
            password = entry_G7.get()
            print("First name", first_name)
            print("Last name", last_name)
            print("User name", user_name)
            print("Phone number", phone_number)
            print("Email", email_address)
            print("Adress", adress)
            print("House nr", house_number)
            print("Password", password)
        editor_page = customtkinter.CTkLabel(labelG2, 
                                             width=400, 
                                             height=500, 
                                             fg_color="#B29696",
                                             text=""
                                             )
        editor_page.place(x=490, y=94)
        entry_G=customtkinter.CTkEntry(editor_page,
                                      font=("Robot bold",20),
                                      fg_color="white",
                                      width=200,
                                      placeholder_text="First Name"
                                      )
        entry_G.place(x=10, y=10)
        entry_G1=customtkinter.CTkEntry(editor_page,
                                      font=("Robot bold",20),
                                      fg_color="white",
                                      width=200,
                                      placeholder_text="Last Name"
                                      )
        entry_G1.place(x=10, y=55)
        entry_G2=customtkinter.CTkEntry(editor_page,
                                      font=("Robot bold",20),
                                      fg_color="white",
                                      width=200,
                                      placeholder_text="User Name"
                                      )
        entry_G2.place(x=10, y=100)
        entry_G3=customtkinter.CTkEntry(editor_page,
                                      font=("Robot bold",20),
                                      fg_color="white",
                                      width=200,
                                      placeholder_text="Phone Number"

                                      )
        entry_G3.place(x=10, y=145)
        entry_G4=customtkinter.CTkEntry(editor_page,
                                      font=("Robot bold",20),
                                      fg_color="white",
                                      width=200,
                                      placeholder_text="Email Adress"
                                      )
        entry_G4.place(x=10, y=190)
        entry_G5=customtkinter.CTkEntry(editor_page,
                                      font=("Robot bold",20),
                                      fg_color="white",
                                      width=200,
                                      placeholder_text="Adress"
                                      )
        entry_G5.place(x=10, y=235)
        entry_G6=customtkinter.CTkEntry(editor_page,
                                      font=("Robot bold",20),
                                      fg_color="white",
                                      width=200,
                                      placeholder_text="House Number"
                                      )
        entry_G6.place(x=10, y=280)
        entry_G7=customtkinter.CTkEntry(editor_page,
                                      font=("Robot bold",20),
                                      fg_color="white",
                                      width=200,
                                      placeholder_text="Password"
                                      )
        entry_G7.place(x=10, y=325)
        buttton_G=customtkinter.CTkButton(editor_page,
                                      text="Save",
                                      font=("Robot bold",15),
                                      fg_color="green",
                                      command=new_customer_info
                                      )
        buttton_G.place(x=10, y=375)
    labelG=customtkinter.CTkLabel(main_canvas, 
                                 width=1600, 
                                 height=1000, 
                                 fg_color="white", 
                                 text=" "
                                 )
    labelG.place(x=0, y=150)
    labelG2=customtkinter.CTkLabel(labelG, 
                                 width=1300, 
                                 height=1000, 
                                 fg_color="#B29696", 
                                 text=" "
                                 )
    labelG2.place(x=115, y=50)
    profile_picture = customtkinter.CTkImage(Image.open("./Login-System/profile_pic.png"),
                                             size=(300, 400))
    labelGpic=customtkinter.CTkLabel(labelG2, 
                                 width=300, 
                                 height=400, 
                                 fg_color="#B29696", 
                                 text=" ",
                                 image=profile_picture
                                 )
    labelGpic.place(x=150, y=100)
    labelG3=customtkinter.CTkLabel(labelG2, 
                                   text= "First Name:\n \nLast Name: \n \nUser Name:\n \nAdress: \n\nHouse Number: \n\nCity: \n\nPhone Number: \n\nEmail Adress:",
                                   fg_color="#B29696",
                                   font=("Robot bold",20),
                                   justify="left"
                                   )
    labelG3.place(x=500, y=105)
    buttton_G=customtkinter.CTkButton(labelG2,
                                      text="Edit",
                                      font=("Robot bold",15),
                                      fg_color="green",
                                      command=edit_page
                                      )
    buttton_G.place(x=500, y=470)
    


def create_login_system():
    root.withdraw()

    def login(username, password):
        # Add your login logic here
        # You can check the username and password against a database or any other validation logic
        if username == "admin" and password == "admin123":
            print("Login successful")
            root.deiconify()
            root.after(0, lambda: root.wm_state('zoomed'))
            login_window.withdraw()
            combobox.configure(values=["Home","Borrow a book", "Return a book","Extend a loan", "Customer info"])
            home()


        if username == "Tom" and password == "MonkeyProof":
            print("Login successful")
            root.deiconify()
            root.after(0, lambda: root.wm_state('zoomed'))
            login_window.withdraw()
            combobox.configure(values=["Home", "My pages", "Borrow a book", "Return a book","Extend a loan"])
            home()

        else:
            print("Invalid username or password")
    def signup():
        def after_signup():
            login_window.deiconify()
            signup_window.withdraw()
        #gui
        width= 700
        height= 400
        signup_window = customtkinter.CTkToplevel(root)
        login_window.iconify()

        x = (signup_window.winfo_screenmmwidth() // 1) - (width // 6)
        y = (signup_window.winfo_screenmmheight() // 1) - (height // 4)
        signup_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        signup_window.resizable(False, False)

        # Load background image
        bg_image = customtkinter.CTkImage(Image.open("./Login-System/background_green.png"),
                                        size=(width, height))
            # Set background image
        bg_image_label = customtkinter.CTkLabel(signup_window, image=bg_image, text="")
        bg_image_label.grid(row=0, column=0, padx=(0, 100), pady=(0, 230))
        first_name_entry = customtkinter.CTkEntry(signup_window,
                                            placeholder_text="First name",
                                            border_width=0,
                                            corner_radius=7,
                                            width=200,
                                            height=35,
                                            bg_color="#547B60"
                                            )
        first_name_entry.grid(row=0, column=0, padx=(0, 550), pady=(0, 460))

        last_name_entry = customtkinter.CTkEntry(signup_window,
                                            placeholder_text="Last name",
                                            border_width=0,
                                            corner_radius=7,
                                            width=200,
                                            height=35,
                                            bg_color="#547B60"
                                            )
        last_name_entry.grid(row=0, column=0, padx=(0, 550), pady=(0, 380))

        address_entry = customtkinter.CTkEntry(signup_window,
                                            placeholder_text="Address",
                                            border_width=0,
                                            corner_radius=7,
                                            width=200,
                                            height=35,
                                            bg_color="#547B60"
                                            )
        address_entry.grid(row=0, column=0, padx=(0, 550), pady=(0, 300))

        streetnr_entry = customtkinter.CTkEntry(signup_window,
                                            placeholder_text="Street Number",
                                            border_width=0,
                                            corner_radius=7,
                                            width=200,
                                            height=35,
                                            bg_color="#547B60"
                                            )
        streetnr_entry.grid(row=0, column=0, padx=(0, 550), pady=(0, 220))

        phone_number_entry = customtkinter.CTkEntry(signup_window,
                                            placeholder_text="Phone number",
                                            border_width=0,
                                            corner_radius=7,
                                            width=200,
                                            height=35,
                                            bg_color="#547B60"
                                            )
        phone_number_entry.grid(row=0, column=0, padx=(0, 550), pady=(0, 140))

        email_entry = customtkinter.CTkEntry(signup_window,
                                            placeholder_text="Email",
                                            border_width=0,
                                            corner_radius=7,
                                            width=200,
                                            height=35,
                                            bg_color="#547B60"
                                            )
        email_entry.grid(row=0, column=0, padx=(0, 550), pady=(0, 60))

        enter = customtkinter.CTkButton(signup_window,
                                        text="Enter",
                                        width=200,
                                        height=30,
                                        bg_color="#385B43",
                                        corner_radius=7,
                                        font=("Robot", 20),
                                        compound="right",
                                        command=after_signup
                                        )
        enter.grid(row=0, column=0, padx=(250, 0), pady=(0, 60))
        # Load rootlication image
        rootlication_logo = customtkinter.CTkImage(Image.open(current_path + "./The_Library.png"),
                                              size=(200, 70))
        # Set rootlication logo
        logo = customtkinter.CTkLabel(signup_window,
                                  text="",
                                  image=rootlication_logo,
                                  fg_color="white",
                                  bg_color="white"
                                  )
        logo.grid(row=0, column=0, padx=(100, 0), pady=(0, 520))

        # Retrieve the user's input from the entry fields
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        address = address_entry.get()
        streetnr = streetnr_entry.get()
        phone_number = phone_number_entry.get()
        email = email_entry.get()

        # Add your signup logic here
        # You can save the user's information to a database or perform any other necessary actions
        print("Sign Up Successful")
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Address:", address)
        print("Street nr:", streetnr)
        print("Phone Number:", phone_number)
        print("Email:", email)
    def forgot_password_help(): 
        help_password = customtkinter.CTkLabel(login_window,
                                               font=("Robot bold", 15),
                                               text="Please contact library personal\n for further assistens.",
                                               fg_color="#1E5930",
                                               bg_color="#1E5930",
                                               justify="center"
                                                  )
        help_password.grid(row=0, column=0, padx=(175, 0), pady=(200, 0))


    #customtkinter.set_rootearance_mode("system")
    customtkinter.set_default_color_theme("green")
    width = 700
    height = 400

    login_window = customtkinter.CTkToplevel(root)
    login_window.title("Login System")

    # Open window in fixed position and Fixed size
    x = (login_window.winfo_screenmmwidth() // 1) - (width // 6)
    y = (login_window.winfo_screenmmheight() // 1) - (height // 4)
    login_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    login_window.resizable(False, False)

    # Change icon in title bar
    #login_window.iconbitmap('./Login-System/nyckel.ico')

    # Load images
    current_path = os.path.dirname(os.path.realpath(__file__))

    # Load background image
    bg_image = customtkinter.CTkImage(Image.open("./Login-System/background_green.png"),
                                      size=(width, height))

    # Load rootlication image
    rootlication_logo = customtkinter.CTkImage(Image.open(current_path + "./The_Library.png"),
                                              size=(200, 70))

    # Load user image
    user_image = customtkinter.CTkImage(Image.open(current_path + "./userLock.png"),
                                        size=(100, 100))

    # Load login button image
    login_btn_image = customtkinter.CTkImage(Image.open(current_path + "./login.png"),
                                             size=(28, 28))

    # Set background image
    bg_image_label = customtkinter.CTkLabel(login_window, image=bg_image, text="")
    bg_image_label.grid(row=0, column=0, padx=(0, 170), pady=(0, 70))

    # Set rootlication logo
    logo = customtkinter.CTkLabel(login_window,
                                  text="",
                                  image=rootlication_logo,
                                  fg_color="white",
                                  bg_color="white"
                                  )
    logo.grid(row=0, column=0, padx=(0, 0), pady=(0, 350))

    # Set user image
    user_image_label = customtkinter.CTkLabel(login_window,
                                              text="",
                                              image=user_image,
                                              anchor="n",
                                              compound="top",
                                              fg_color="#547B60",
                                              bg_color="#547B60",
                                              corner_radius=10
                                              )

    user_image_label.grid(row=0, column=0, padx=(0, 600), pady=(0, 300))

    # Entry Widget for username field
    username_entry = customtkinter.CTkEntry(login_window,
                                            placeholder_text="Username",
                                            border_width=0,
                                            corner_radius=7,
                                            width=200,
                                            height=35,
                                            bg_color="#547B60"
                                            )
    username_entry.grid(row=0, column=0, padx=(0, 600), pady=(0, 100))

    # Entry Widget for password field
    password_entry = customtkinter.CTkEntry(login_window,
                                            placeholder_text="Password",
                                            border_width=0,
                                            corner_radius=7,
                                            width=200,
                                            height=35,
                                            bg_color="#547B60",
                                            show="*"
                                            )
    password_entry.grid(row=0, column=0, padx=(0, 600), pady=(100, 100))

    def login_btn_click():
        username = username_entry.get()
        password = password_entry.get()
        login(username, password)

    # Login Button
    login_btn = customtkinter.CTkButton(login_window,
                                        text="Login",
                                        width=200,
                                        height=30,
                                        bg_color="#547B60",
                                        corner_radius=7,
                                        font=("Robot", 20),
                                        image=login_btn_image,
                                        compound="right",
                                        command=login_btn_click
                                        )
    login_btn.grid(row=0, column=0, padx=(0, 600), pady=(200, 100))

    # Check box for Remember me
    remember_me = customtkinter.CTkCheckBox(login_window,
                                            text="Remember Me",
                                            width=100,
                                            height=30,
                                            bg_color="#547B60",
                                            fg_color="#547B60"
                                            )
    remember_me.grid(row=0, column=0, padx=(0, 600), pady=(320, 100))

    not_a_member_text = customtkinter.CTkLabel(login_window,
                                               text="Not a member?",
                                               font=("Roboto bold", 15),
                                               bg_color="#1E5930",
                                               fg_color="#1E5930"
                                               )
    not_a_member_text.grid(row=0, column=0, padx=(170, 0), pady=(20, 80))

    # Sign up Button
    signup_btn = customtkinter.CTkButton(login_window,
                                         text="Sign Up",
                                         width=200,
                                         height=30,
                                         bg_color="#1E5930",
                                         corner_radius=7,
                                         font=("Roboto", 20),
                                         command=signup
                                         )
    signup_btn.grid(row=0, column=0, padx=(170, 0), pady=(30, 0))

    # Forgot password Button
    forgot_password = customtkinter.CTkButton(login_window,
                                               text="Forgot Password?",
                                               width=100,
                                               height=30,
                                               bg_color="#1E5930",
                                               fg_color="#1E5930",
                                               hover_color="#1E5930",
                                               corner_radius=7,
                                               font=("Roboto", 20),
                                               command=forgot_password_help
                                               )
    forgot_password.grid(row=0, column=0, padx=(175, 0), pady=(140, 0))

    login_window.mainloop()

#create_login_system()
home()
root.mainloop()