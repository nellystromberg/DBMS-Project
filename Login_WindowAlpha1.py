import customtkinter
from PIL import Image
import os
from sys import platform

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")
width = 700 
height = 400 

root = customtkinter.CTk()
root.title("Login System")

# Open window in fixed position and Fixed size 
x = (root.winfo_screenmmwidth() // 1) - (width // 6)
y = (root.winfo_screenmmheight() // 1) - (height // 4)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.resizable(False, False)

# Change icon in title bar 
root.iconbitmap('./Login-System/nyckel.ico')

# Load images
current_path = os.path.dirname(os.path.realpath(__file__))

# Load background image 
bg_image = customtkinter.CTkImage(Image.open( "./Login-System/background_green.png"), 
                                  size = (width, height))

# Load application image
application_logo = customtkinter.CTkImage(Image.open(current_path + "./circle2.png"),
                                          size = (35, 35))

# Load user image 
user_image = customtkinter.CTkImage(Image.open(current_path + "./userLock.png"),
                                          size = (100, 100))

# Load login button image
login_btn_image = customtkinter.CTkImage(Image.open(current_path + "./login.png"),
                                          size = (28, 28))



# Set background image 
bg_image_label = customtkinter.CTkLabel(root, image=bg_image, text="")
bg_image_label.grid(row=0, column=0, padx= (0, 170), pady= (0, 70))

# Set application logo
logo = customtkinter.CTkLabel(root,
                              text="",
                              image=application_logo,
                              fg_color="#f6f6f6",
                              bg_color="transparent"
                              )
logo.grid(row=0, column=0, padx=(0, 250), pady=(0, 420))

logo_text = customtkinter.CTkLabel(root, 
                                   text="The library of Alexandria",
                                   font=("Robot bold", 20),
                                   fg_color="White",
                                   bg_color="White"
                                   )
logo_text.grid(row=0, column=0, padx=(50, 50), pady=(0, 422))

# Set user image 
user_image_label = customtkinter.CTkLabel(root,
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
username = customtkinter.CTkEntry(root, 
                                  placeholder_text="Username",
                                  border_width=0,
                                  corner_radius=7,
                                  width=200, 
                                  height=35, 
                                  bg_color="#547B60"
                                  )
username.grid(row=0, column=0, padx=(0, 600), pady=(0, 100))

password = customtkinter.CTkEntry(root, 
                                  placeholder_text="Password",
                                  border_width=0,
                                  corner_radius=7,
                                  width=200, 
                                  height=35, 
                                  bg_color="#547B60", 
                                  show="*"
                                  )
password.grid(row=0, column=0, padx=(0, 600), pady=(100, 100))

login_btn = customtkinter.CTkButton(root, 
                                    text="Login",
                                    width=200,
                                    height=30,
                                    bg_color="#547B60",
                                    corner_radius=7,
                                    font=("Robot", 20),
                                    image=login_btn_image, 
                                    compound="right"
                                    )
login_btn.grid(row=0, column=0, padx=(0, 600), pady=(200, 100))

# Check box for Remember me 
remember_me = customtkinter.CTkCheckBox(root,
                                        text="Remember Me",
                                        width=100,
                                        height=30,
                                        bg_color="#547B60",
                                        fg_color="#547B60"
                                        )
remember_me.grid(row=0, column=0, padx=(0, 600), pady=(320,100))

not_a_member_text = customtkinter.CTkLabel(root,
                                           text="Not a member?",
                                           font=("Roboto bold", 15),
                                           bg_color="#1E5930",
                                           fg_color="#1E5930"
                                           )
not_a_member_text.grid(row=0, column=0, padx=(150, 0), pady=(20,80))

# Sign up Button
signup_btn = customtkinter.CTkButton(root, 
                                    text="Sign Up",
                                    width=200,
                                    height=30,
                                    bg_color="#1E5930",
                                    corner_radius=7,
                                    font=("Roboto", 20),
                                    )
signup_btn.grid(row=0, column=0, padx=(170, 0), pady=(30, 0))

# Forgot password Button
forgot_password = customtkinter.CTkButton(root, 
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



root.mainloop()