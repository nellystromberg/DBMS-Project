import os
from PIL import Image
from sys import platform
import customtkinter

root = customtkinter.CTk()
root.title("Image Viewer")
root.geometry("500x500")

       



def create_login_system():
    def login(username, password):
        # Add your login logic here
        # You can check the username and password against a database or any other validation logic
        if username == "admin" and password == "admin123":
            print("Login successful")
        else:
            print("Invalid username or password")

    customtkinter.set_appearance_mode("system")
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
    login_window.iconbitmap('./Login-System/nyckel.ico')

    # Load images
    current_path = os.path.dirname(os.path.realpath(__file__))

    # Load background image
    bg_image = customtkinter.CTkImage(Image.open("./Login-System/background_green.png"),
                                      size=(width, height))

    # Load application image
    application_logo = customtkinter.CTkImage(Image.open(current_path + "./circle2.png"),
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

    # Set application logo
    logo = customtkinter.CTkLabel(login_window,
                                  text="",
                                  image=application_logo,
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

    login_btn = customtkinter.CTkButton(login_window,
                                        text="Login",
                                        width=200,
                                        height=30,
                                        bg_color="#547B60",
                                        corner_radius=7,
                                        font=("Robot", 20),
                                        image=login_btn_image,
                                        compound="right",
                                        command=login

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
                                              )
    forgot_password.grid(row=0, column=0, padx=(175, 0), pady=(140, 0))

    login_window.mainloop()

k=customtkinter.CTkButton(root, command=create_login_system)
k.grid(row=0,column=0,padx=(100,100),pady=(100,100))

root.mainloop()