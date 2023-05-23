import os
from PIL import Image
from sys import platform
import customtkinter
root = customtkinter.CTk()
root.title("Library of Alexandria")
#root.iconify()
root.iconbitmap('./Login-System/book.ico')

window_height = 700
window_width = 1400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, 
                                   window_height, 
                                   x_cordinate, 
                                   y_cordinate)
                                   )
root.minsize(900,500)

#Font
def specfont(font_size):
    my_font = customtkinter.CTkFont(family="Ariel", 
                                    size=font_size
                                    )
    return my_font

#Frame
main_frame=customtkinter.CTkFrame(root,
                                  width=1600,
                                  height=1000, 
                                  fg_color="blue"
                                  )
main_frame.place(x=0,y=0)

#Canvas
main_canvas=customtkinter.CTkCanvas(root,
                                    width=2000,
                                    height=1000
                                    )
main_canvas.place(x=0,y=0)

#Load user image
header = customtkinter.CTkImage(Image.open("./Login-System/The_Library.png"),
                                        size=(300, 80))

#Label
banner_label = customtkinter.CTkLabel(main_canvas, 
                                   width=1600, 
                                   height=150, 
                                   fg_color="white", 
                                   text=""
                                   )
banner_label.place(x=0, y=0)

#Label
top_label = customtkinter.CTkLabel(main_canvas, 
                                   width=1600, 
                                   height=100, 
                                   fg_color="#1E5930", 
                                   text=""
                                   )
top_label.place(x=0, y=0)

top_label_log = customtkinter.CTkLabel(top_label, 
                                   width=300, 
                                   height=80, 
                                   fg_color="#1E5930", 
                                   text=""
                                   )
top_label_log.place(x=0, y=0)

labelB=customtkinter.CTkLabel(main_canvas, 
                             width=1600, 
                             height=650, 
                             fg_color="white", 
                             text=" "
                             )
labelB.place(x=0, y=150)

label_open_time=customtkinter.CTkLabel(main_canvas, 
                             width=300, 
                             height=400, 
                             fg_color="white", 
                             text=" ",
                             corner_radius=7
                             )
label_open_time.place(x=1120, y=250)

open_time_frame = customtkinter.CTkFrame(label_open_time, 
                                         width=300, height=400, 
                                         fg_color="white",
                                         corner_radius=7,
                                         border_width=2
                                         )
open_time_frame.place(x=0, y=0)

open_time_canvas= customtkinter.CTkCanvas(open_time_frame, 
                                          width=400, 
                                          height=500, 
                                          bg="white"
                                          )
open_time_canvas.place(x=0,y=0)

opent_time_scroll = customtkinter.CTkScrollbar(open_time_frame, 
                                               orientation="vertical", 
                                               command=open_time_canvas.yview, 
                                               height=500,
                                               corner_radius=7,
                                               fg_color="white"
                                               )
opent_time_scroll.place(x=280,y=0)

open_time_canvas.configure(yscrollcommand=opent_time_scroll.set)
open_time_canvas.bind('<Configure>', lambda e: open_time_canvas.configure(scrollregion=open_time_canvas.bbox("all")))

second_open_time_frame = customtkinter.CTkFrame(open_time_canvas,
                                                fg_color="white",
                                                corner_radius=7
                                                )

open_time_canvas.create_window((0,0), 
                               window=second_open_time_frame, 
                               anchor="nw",
                               width=350
                               )

for thing in range(8):
    customtkinter.CTkButton(second_open_time_frame, 
                            width=200,
                            height=50,
                            state="disabled",
                            font=("robot bold", 20),
                            fg_color="pink",
                            hover_color="pink"

                            ).grid(row=thing, 
                                                                column=1, 
                                                                pady=20, 
                                                                padx=30, 
                                                                sticky="nsew"
                                                                )
    if thing == 0:
        customtkinter.CTkButton(second_open_time_frame,text="OPENING HOURS \n AND \n EVENTS", width=200,font=("robot bold", 20),fg_color="pink", hover_color="pink").grid(row=thing,
                                                                                      column=1, 
                                                                                      pady=20,
                                                                                      padx=30,
                                                                                      sticky="nsew"
                                                                                      )
    if thing == 1:
        customtkinter.CTkButton(second_open_time_frame,text="Monday \n 10.00-20.00", width=200,font=("robot bold", 20),).grid(row=thing,
                                                                                      column=1, 
                                                                                      pady=20,
                                                                                      padx=30,
                                                                                      sticky="nsew"
                                                                                      )
    if thing == 2:
        customtkinter.CTkButton(second_open_time_frame,text="Tuesday \n 10.00-20.00", width=200,font=("robot bold", 20),).grid(row=thing,
                                                                                      column=1, 
                                                                                      pady=20,
                                                                                      padx=30,
                                                                                      sticky="nsew"
                                                                                      )
    if thing == 3:
        customtkinter.CTkButton(second_open_time_frame,text="Wednesday \n 10.00-21.00", width=200,font=("robot bold", 20),).grid(row=thing,
                                                                                      column=1, 
                                                                                      pady=20,
                                                                                      padx=30,
                                                                                      sticky="nsew"
                                                                                      )
    if thing == 4:
        customtkinter.CTkButton(second_open_time_frame,text="Thursday \n 10.00-20.00", width=200,font=("robot bold", 20),).grid(row=thing,
                                                                                      column=1, 
                                                                                      pady=20,
                                                                                      padx=30,
                                                                                      sticky="nsew"
                                                                                      )
    if thing == 5:
        customtkinter.CTkButton(second_open_time_frame,text="Friday \n 10.00-21.00", width=200,font=("robot bold", 20),).grid(row=thing,
                                                                                      column=1, 
                                                                                      pady=20,
                                                                                      padx=30,
                                                                                      sticky="nsew"
                                                                                      )
    if thing == 6:
        customtkinter.CTkButton(second_open_time_frame,text="Saturday \n 12.00-20.00", width=200,font=("robot bold", 20),).grid(row=thing,
                                                                                      column=1, 
                                                                                      pady=20,
                                                                                      padx=30,
                                                                                      sticky="nsew"
                                                                                      )
    if thing == 7:
        customtkinter.CTkButton(second_open_time_frame,text="Sunday \n 12.00-18.00", width=200,font=("robot bold", 20),).grid(row=thing,
                                                                                      column=1, 
                                                                                      pady=20,
                                                                                      padx=30,
                                                                                      sticky="nsew"
                                                                                      )


img1 = customtkinter.CTkImage(Image.open("./Login-System/1.png"),
                                        size=(700, 400))

img2 = customtkinter.CTkImage(Image.open("./Login-System/2.png"),
                                        size=(700, 400))

img3 = customtkinter.CTkImage(Image.open("./Login-System/3.png"),
                                        size=(700, 400))

img4 = customtkinter.CTkImage(Image.open("./Login-System/4.png"),
                                        size=(700, 400))

img5 = customtkinter.CTkImage(Image.open("./Login-System/5.png"),
                                        size=(700, 00))


info=customtkinter.CTkLabel(main_canvas, 
                             width=700, 
                             height=400, 
                             fg_color="pink", 
                             text=" ",
                             corner_radius=7
                             
                             )
info.place(x=115, y=250)
info_radio=customtkinter.CTkLabel(info, 
                             width=200, 
                             height=30, 
                             fg_color="red", 
                             text=" ",
                             corner_radius=7
                             )
info_radio.place(x=400,y=360)

var=customtkinter.IntVar()

def section():
    choice = var.get()
    if choice == 1:
        info.configure(image=img1)
    elif choice == 2:
        info.configure(image=img2)
    elif choice == 3:
        info.configure(image=img3)
    elif choice == 4:
        info.configure(image=img4)
    elif choice == 5:
        info.configure(image=img5)
    else:
        info.configure(image=img1)

radiobutton1 = customtkinter.CTkRadioButton(info_radio, text="", variable=var, value=1, command=section)
radiobutton1.place(x=30,y=1)
radiobutton2 = customtkinter.CTkRadioButton(info_radio, text="", variable=var, value=2, command=section)
radiobutton2.place(x=60,y=1)
radiobutton3 = customtkinter.CTkRadioButton(info_radio, text="", variable=var, value=3, command=section)
radiobutton3.place(x=90,y=1)
radiobutton4 = customtkinter.CTkRadioButton(info_radio, text="", variable=var, value=4, command=section)
radiobutton4.place(x=120,y=1)
radiobutton5 = customtkinter.CTkRadioButton(info_radio, text="", variable=var, value=5, command=section)
radiobutton5.place(x=150,y=1)
section()
#info2=customtkinter.CTkLabel(main_canvas, 
                            # width=1300, 
                            # height=80, 
                           #  fg_color="blue", 
                            # text=" ",
                          #   corner_radius=7
                          #   )
#info2.place(x=115, y=655)

#Entry
search_bar = customtkinter.CTkEntry(labelB, 
                                    width=1300,
                                    fg_color="white", 
                                    height=50, 
                                    font=("Robot bold",30),
                                    placeholder_text="Look up diffrent titles or authors here."
                                    )
search_bar.place(x=115, y=20)

def home():
    #Entry
    search_bar = customtkinter.CTkEntry(labelB, 
                                    width=1300,
                                    fg_color="white", 
                                    height=50, 
                                    font=("Robot bold",30),
                                    placeholder_text="Look up diffrent titles or authors here."
                                    )
    search_bar.place(x=115, y=20) 
    labelB=customtkinter.CTkLabel(main_canvas, 
                             width=1600, 
                             height=600, 
                             fg_color="white", 
                             text=" "
                             )
    labelB.place(x=0, y=150)
    #Search Image 
    search_img = customtkinter.CTkImage(Image.open("./Login-System/search.png"),
                                        size=(40, 40))
    #Button
    search_button = customtkinter.CTkButton(search_bar, 
                                        width=50, 
                                        height=50, 
                                        fg_color="grey", 
                                        text="", 
                                        font=("Robot bold",24), 
                                        text_color="#1E5930", 
                                        hover_color="grey",
                                        border_width=0,
                                        image=search_img
                                        )
    search_button.place(x=1243, y=0)
    

home_button = customtkinter.CTkButton(top_label, 
                                        width=300, 
                                        height=80, 
                                        text="", 
                                        font=("Robot bold",24), 
                                        text_color="#1E5930", 
                                        hover_color="grey",
                                        border_width=0,
                                        image=header,
                                        fg_color="#1E5930",
                                        command=home
                                        )
home_button.place(x=20, y=0)

#Search Image 
search_img = customtkinter.CTkImage(Image.open("./Login-System/search.png"),
                                        size=(40, 40))
#Button
search_button = customtkinter.CTkButton(search_bar, 
                                        width=50, 
                                        height=50, 
                                        fg_color="grey", 
                                        text="", 
                                        font=("Robot bold",24), 
                                        text_color="#1E5930", 
                                        hover_color="grey",
                                        border_width=0,
                                        image=search_img, 
                                        )
search_button.place(x=1243, y=0)

#Function
def borrowing():
    def borrowing_button_command():
        labelC.destroy()
        labelB()
    labelB.destroy
    labelC=customtkinter.CTkLabel(main_canvas, 
                                 width=1600, 
                                 height=600, 
                                 fg_color="white", 
                                 text=" "
                                 )
    labelC.place(x=0, y=150)
    customer_id = customtkinter.CTkEntry(labelC, 
                                         width=200, 
                                         font=("Robot bold",15)
                                         )
    customer_id_text = customtkinter.CTkLabel(labelC, 
                                              text="Customer ID:", 
                                              font=("Robot bold",15)
                                              )
    customer_id.place(x=400, y=200)
    customer_id_text.place(x=300, y=200)
    book_id = customtkinter.CTkEntry(labelC, 
                                     width=200,
                                     font=("Robot bold",15)
                                     )
    book_id_text = customtkinter.CTkLabel(labelC, 
                                          text="Book ID:",
                                          font=("Robot bold", 15)
                                          )
    book_id.place(x=400, y=300)
    book_id_text.place(x=300, y=300)
    enter_button = customtkinter.CTkButton(labelC, 
                                           text="Enter",
                                           font=("Robot bold",15),
                                           command=borrowing_button_command 
                                           )
    enter_button.place(x=300,y=350)

def returning():
    def returning_button_command():
        labelD.destroy()
        labelB()
    labelD=customtkinter.CTkLabel(main_canvas, 
                                 width=1600, 
                                 height=600, 
                                 fg_color="white", 
                                 text=" "
                                 )
    labelD.place(x=0, y=150)

    book_id = customtkinter.CTkEntry(labelD, 
                                     width=200,
                                     font=("Robot bold", 15)
                                     )
    book_id_text = customtkinter.CTkLabel(labelD, 
                                          text="Book ID:",
                                          font=("Robot bold", 15)
                                          )
    book_id.place(x=400, y=300)
    book_id_text.place(x=300, y=300)

    enter_button = customtkinter.CTkButton(labelD, 
                                           text="Enter",
                                           font=("Robot bold", 15), 
                                           command=returning_button_command
                                           )
    enter_button.place(x=300,y=350)


def extending():
    def extending_button_command():
        labelE.destroy()
        labelB()
    labelE=customtkinter.CTkLabel(main_canvas, 
                                 width=1600, 
                                 height=650, 
                                 fg_color="white", 
                                 text=" "
                                 )
    labelE.place(x=0, y=150)

    book_id = customtkinter.CTkEntry(labelE, 
                                     width=200,
                                     font=("Robot bold", 15)
                                     )
    book_id_text = customtkinter.CTkLabel(labelE, 
                                          text="Book ID:",
                                          font=("Robot bold", 15)
                                          )
    book_id.place(x=400, y=300)
    book_id_text.place(x=300, y=300)

    enter_button = customtkinter.CTkButton(labelE, 
                                           text="Enter",
                                           font=("Robot bold",15), 
                                           command=extending_button_command
                                           )
    enter_button.place(x=300,y=350)


def customers():
    def customer_button_command():
        labelF.destroy()
        labelB()
    
    labelF=customtkinter.CTkLabel(main_canvas, 
                                 width=1600, 
                                 height=600, 
                                 fg_color="white", 
                                 text=" "
                                 )
    labelF.place(x=0, y=150)

    customer_id = customtkinter.CTkEntry(labelF, 
                                         width=200, 
                                         font=("Robot bold",15)
                                         )
    customer_id_text = customtkinter.CTkLabel(labelF, 
                                              text="Customer ID:", 
                                              font=("Robot bold",15)
                                              )
    customer_id.place(x=400, y=200)
    customer_id_text.place(x=300, y=200)

    enter_button = customtkinter.CTkButton(labelF, 
                                           text="Enter",
                                           font=("Robot bold",15), 
                                           command=customer_button_command
                                           )
    enter_button.place(x=300,y=350)



def combobox_callback(choice):
    def homely():
        labelB()

    if choice == "Borrow a book":
         borrowing()
    if choice == "Return a book":
        returning()
    if choice == "Extend a loan":
        extending()
    if choice == "Customer info":
        customers()
    if choice == "Home":
        homely()
        print("combobox dropdown clicked:", choice)

combobox_var = customtkinter.StringVar(value="My pages")
combobox = customtkinter.CTkComboBox(banner_label, 
                                     values=["My pages", "Borrow a book", "Return a book","Extend a loan", "Customer info", "Home"],
                                     width=1300,
                                     height=50,
                                     command=combobox_callback, 
                                     variable=combobox_var,
                                     justify="center",
                                     font=("Robot bold", 20),
                                     dropdown_font=("Robot bold", 20),
                                     button_color="grey",
                                     hover=True,
                                     corner_radius=7
                                     )
combobox_var.set("My pages")
combobox.place(x=115, y=100)


def create_login_system():
    root.withdraw()

    def login(username, password):
        # Add your login logic here
        # You can check the username and password against a database or any other validation logic
        if username == "admin" and password == "admin123":
            print("Login successful")
            root.deiconify()
            login_window.destroy()
        if username == "Tom" and password == "MonkeyProof":
            print("Login successful")
            root.deiconify()
            login_window.destroy()
            
            

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
                                        bg_color="#1E5930",
                                        corner_radius=7,
                                        font=("Robot", 20),
                                        compound="right",
                                        command=after_signup
                                        )
        enter.grid(row=0, column=0, padx=(250, 0), pady=(0, 60))
        # Load rootlication image
        rootlication_logo = customtkinter.CTkImage(Image.open(current_path + "./circle2.png"),
                                              size=(35, 35))
        # Set rootlication logo
        logo = customtkinter.CTkLabel(signup_window,
                                  text="",
                                  image=rootlication_logo,
                                  fg_color="#f6f6f6",
                                  bg_color="transparent"
                                  )
        logo.grid(row=0, column=0, padx=(0, 170), pady=(0, 570))
        
        logo_text = customtkinter.CTkLabel(signup_window,
                                       text="The library of Alexandria",
                                       font=("Robot bold", 20),
                                       fg_color="White",
                                       bg_color="White"
                                       )
        logo_text.grid(row=0, column=0, padx=(80, 0), pady=(0, 570))

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
    rootlication_logo = customtkinter.CTkImage(Image.open(current_path + "./circle2.png"),
                                              size=(35, 35))

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
                                  fg_color="#f6f6f6",
                                  bg_color="transparent"
                                  )
    logo.grid(row=0, column=0, padx=(0, 250), pady=(0, 420))

    logo_text = customtkinter.CTkLabel(login_window,
                                       text="The library of Alexandria",
                                       font=("Robot bold", 20),
                                       fg_color="White",
                                       bg_color="White"
                                       )
    logo_text.grid(row=0, column=0, padx=(50, 50), pady=(0, 422))

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
    not_a_member_text.grid(row=0, column=0, padx=(150, 0), pady=(20, 80))

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
                                               fg_color="#0E421E",
                                               hover_color="#197434",
                                               corner_radius=7,
                                               font=("Roboto", 20),
                                               command=forgot_password_help
                                               )
    forgot_password.grid(row=0, column=0, padx=(175, 0), pady=(140, 0))

    login_window.mainloop()

#create_login_system()

root.mainloop()