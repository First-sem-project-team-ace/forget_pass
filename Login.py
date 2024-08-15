# from tkinter import *
# import customtkinter
# from PIL import Image
# import sqlite3
# from tkinter import messagebox


# def login_page():
#    login_window= customtkinter.CTk()
#    login_window.title("Login")

#    customtkinter.set_appearance_mode('light')
#    screen_width = login_window.winfo_screenwidth()
#    screen_height = login_window.winfo_screenheight()
#    login_window.geometry(f"{screen_width}x{screen_height}+0+0")
#    global username
#    def login():
#        global username
#        conn = sqlite3.connect("hostel.db")
#        c = conn.cursor()
       
#        username = username_entry.get()
#        password = password_entry.get()
       
#        if not username or not password:
#            messagebox.showerror("Error", "Please fill in both username and password")
#            return
       
#        c.execute("SELECT username, password FROM hostel WHERE username=? AND password=?", (username, password))
#        result = c.fetchone()
       
#        if result:
#            stored_username, stored_password = result
#            if stored_username == username and stored_password == password:
#                login_window.destroy()

#                shared_state=username
               
#            else:
#                messagebox.showerror("Error", "Invalid username or password")
#        else:
#            messagebox.showerror("Error", "Invalid username or password")
       
#        conn.close()
   
      
#    frame = customtkinter.CTkFrame(master=login_window, width=screen_width, height=screen_height, bg_color="white", fg_color="#614BD4")
#    frame.place(relx=0, rely=0)
#    Linear_image = customtkinter.CTkImage(light_image=Image.open('images\\Dashboard_label.png'), size=(1366, 770))
#    Linear_image_label = customtkinter.CTkLabel(master=frame, image=Linear_image, text="")
#    Linear_image_label.place(x=0, y=0)
#    my_image = customtkinter.CTkImage(light_image=Image.open('images\\Hostel.jpg'), size=(1366, 400))
#    my_label = customtkinter.CTkLabel(master=frame, image=my_image, text="")
#    my_label.place(relx=0, rely=0.45)
#    Login_frame = customtkinter.CTkFrame(master=login_window, fg_color="white", width=300, height=300)
#    Login_frame.place(relx=0.7, rely=0.1)
#    Login_welcome = Label(master=Login_frame, text="Welcome to Griha Hostel", fg="black", bg="white")
#    Login_welcome.place(relx=0.3, rely=0)
#    Login_label = Label(master=Login_frame, text="Log In", font=("bold", 25), bg="white", fg="#614BD4")
#    Login_label.place(relx=0.1, rely=0.1)
#    username_label = Label(master=Login_frame, text="Username:", bg="white", fg="black", font=("20"))
#    username_label.place(relx=0.03, rely=0.3)
#    password_label = Label(master=Login_frame, text="Password:", bg="white", fg="Black", font=("20"))
#    password_label.place(relx=0.03, rely=0.4)
#    username_entry = customtkinter.CTkEntry(master=Login_frame, width=200, fg_color="gray", text_color="white", corner_radius=10, bg_color="white")
#    username_entry.place(relx=0.3, rely=0.3)
#    password_entry = customtkinter.CTkEntry(master=Login_frame, width=200, fg_color="gray", text_color="white", corner_radius=10, bg_color="white", show="*")
#    password_entry.place(relx=0.3, rely=0.4)
#    def show_pass():
#        if show_password_var.get() == 1:
#            password_entry.configure(show="")
#        else:
#            password_entry.configure(show="*")
#    show_password_var = IntVar()
#    chk = Checkbutton(master=Login_frame, text="Show password", variable=show_password_var, onvalue=1, offvalue=0, command=show_pass)
#    chk.place(relx=0.5, rely=0.5)
#    Btn_login = customtkinter.CTkButton(master=Login_frame, text="Login", width=90, fg_color="#614BD4", 
#                                        command=login,text_color="white")
#    Btn_login.place(relx=0.65, rely=0.6)
#    def about():
   
      
#       About_frame= customtkinter.CTkFrame(master=login_window, height=300, width=500, fg_color="#42ABC7")
#       About_frame.place(relx=0.3, rely=0.2)
   
#       About_label=customtkinter.CTkLabel(master=About_frame, text="About us", font=("bold",25), text_color="white")
#       About_label.place(relx=0.05, rely=0.15)
   
#       Content_label= customtkinter.CTkLabel(master=About_frame, text="Griha hostel offers a welcoming and \ncomfortable living environment for\n students abd professionals.With\n modern amenities and facilities,and a\n supportive community,Griha hostel\n ensures a home-like experience away\n from home.", justify= LEFT,
#                                   text_color="white", font=("bold",20))
#       Content_label.place(relx=0.1, rely=0.25)
#       def back():
#        About_frame.destroy()
       
#       Exit_button= customtkinter.CTkButton(master=About_frame, text="X", command=back, width=30)
#       Exit_button.place(relx=0.9, rely=0.05)   
#    What_btn= customtkinter.CTkButton(master=frame,text="?", bg_color="#3FB5CB",fg_color="#3FB5CB",width=50, text_color="black",
#                           corner_radius=80, font=("bold", 20), command=about)
#    What_btn.place(relx=0.7, rely=0.05)
#    login_window.mainloop()

from tkinter import *
import customtkinter
from PIL import Image
import sqlite3
from tkinter import messagebox


def login_page():
    login_window = customtkinter.CTk()
    login_window.title("Login")

    customtkinter.set_appearance_mode('light')
    screen_width = login_window.winfo_screenwidth()
    screen_height = login_window.winfo_screenheight()
    login_window.geometry(f"{screen_width}x{screen_height}+0+0")

    global username

    def login():
        global username
        conn = sqlite3.connect("hostel.db")
        c = conn.cursor()

        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in both username and password")
            return

        c.execute("SELECT username, password FROM hostel WHERE username=? AND password=?", (username, password))
        result = c.fetchone()

        if result:
            stored_username, stored_password = result
            if stored_username == username and stored_password == password:
                login_window.destroy()

                shared_state = username

            else:
                messagebox.showerror("Error", "Invalid username or password")
        else:
            messagebox.showerror("Error", "Invalid username or password")

        conn.close()

    def forgot_password():
        login_frame.destroy()  # Destroy the login frame
        
        forgot_frame = customtkinter.CTkFrame(master=login_window, fg_color="white", width=300, height=300)
        forgot_frame.place(relx=0.7, rely=0.1)

        forgot_label = Label(master=forgot_frame, text="Forgot Password", font=("bold", 25), bg="white", fg="#614BD4")
        forgot_label.place(relx=0.1, rely=0.05)

        question1_label = Label(master=forgot_frame, text="Favorite Food:", bg="white", fg="black", font=("20"))
        question1_label.place(relx=0.03, rely=0.22)

        question1_entry = customtkinter.CTkEntry(master=forgot_frame, width=170, fg_color="gray", text_color="white", corner_radius=10, bg_color="white")
        question1_entry.place(relx=0.35, rely=0.2)

        question2_label = Label(master=forgot_frame, text="First Pet Name:", bg="white", fg="black", font=("20"))
        question2_label.place(relx=0.03, rely=0.32)

        question2_entry = customtkinter.CTkEntry(master=forgot_frame, width=170, fg_color="gray", text_color="white", corner_radius=10, bg_color="white")
        question2_entry.place(relx=0.35, rely=0.3)

        new_password_label = Label(master=forgot_frame, text="New Password:", bg="white", fg="black", font=("20"))
        new_password_label.place(relx=0.03, rely=0.42)

        new_password_entry = customtkinter.CTkEntry(master=forgot_frame, width=170, fg_color="gray", text_color="white", corner_radius=10, bg_color="white", show="*")
        new_password_entry.place(relx=0.35, rely=0.4)

        confirm_password_label = Label(master=forgot_frame, text="Confirm Password:", bg="white", fg="black", font=("20"))
        confirm_password_label.place(relx=0.03, rely=0.52)

        confirm_password_entry = customtkinter.CTkEntry(master=forgot_frame, width=170, fg_color="gray", text_color="white", corner_radius=10, bg_color="white", show="*")
        confirm_password_entry.place(relx=0.35, rely=0.5)

        def reset_password():
            favorite_food = question1_entry.get()
            pet_name = question2_entry.get()
            new_password = new_password_entry.get()
            confirm_password = confirm_password_entry.get()

            if not favorite_food or not pet_name or not new_password or not confirm_password:
                messagebox.showerror("Error", "Please fill in all fields")
                return

            if new_password != confirm_password:
                messagebox.showerror("Error", "Passwords do not match")
                return

            conn = sqlite3.connect("hostel.db")
            c = conn.cursor()

            c.execute("SELECT security_question1, security_question2 FROM hostel WHERE username=?", (username,))
            result = c.fetchone()

            if result:
                stored_food, stored_pet = result
                if stored_food == favorite_food and stored_pet == pet_name:
                    c.execute("UPDATE hostel SET password=? WHERE username=?", (new_password, username))
                    conn.commit()
                    messagebox.showinfo("Success", "Password reset successful")
                    forgot_frame.destroy()
                    create_login_frame()
                else:
                    messagebox.showerror("Error", "Security answers do not match")
            else:
                messagebox.showerror("Error", "Username not found")

            conn.close()

        reset_button = customtkinter.CTkButton(master=forgot_frame, text="Confirm", width=120, fg_color="#614BD4", 
                                               command=reset_password, text_color="white")
        reset_button.place(relx=0.48, rely=0.7)

    def create_login_frame():
        global login_frame, username_entry, password_entry

        login_frame = customtkinter.CTkFrame(master=login_window, fg_color="white", width=300, height=300)
        login_frame.place(relx=0.7, rely=0.1)

        Login_welcome = Label(master=login_frame, text="Welcome to Griha Hostel", fg="black", bg="white")
        Login_welcome.place(relx=0.3, rely=0)

        Login_label = Label(master=login_frame, text="Log In", font=("bold", 25), bg="white", fg="#614BD4")
        Login_label.place(relx=0.1, rely=0.1)

        username_label = Label(master=login_frame, text="Username:", bg="white", fg="black", font=("20"))
        username_label.place(relx=0.03, rely=0.3)

        password_label = Label(master=login_frame, text="Password:", bg="white", fg="Black", font=("20"))
        password_label.place(relx=0.03, rely=0.4)

        username_entry = customtkinter.CTkEntry(master=login_frame, width=200, fg_color="gray", text_color="white", corner_radius=10, bg_color="white")
        username_entry.place(relx=0.3, rely=0.3)

        password_entry = customtkinter.CTkEntry(master=login_frame, width=200, fg_color="gray", text_color="white", corner_radius=10, bg_color="white", show="*")
        password_entry.place(relx=0.3, rely=0.4)

        def show_pass():
            if show_password_var.get() == 1:
                password_entry.configure(show="")
            else:
                password_entry.configure(show="*")

        show_password_var = IntVar()
        chk = Checkbutton(master=login_frame, text="Show password", variable=show_password_var, onvalue=1, offvalue=0, command=show_pass)
        chk.place(relx=0.5, rely=0.5)

        Btn_login = customtkinter.CTkButton(master=login_frame, text="Login", width=90, fg_color="#614BD4", 
                                            command=login, text_color="white")
        Btn_login.place(relx=0.65, rely=0.6)

        forgot_password_btn = customtkinter.CTkButton(master=login_frame, text="Forgot Password?", width=120, fg_color="#42ABC7", 
                                                      command=forgot_password, text_color="white")
        forgot_password_btn.place(relx=0.05, rely=0.6)

    frame = customtkinter.CTkFrame(master=login_window, width=screen_width, height=screen_height, bg_color="white", fg_color="#614BD4")
    frame.place(relx=0, rely=0)

    Linear_image = customtkinter.CTkImage(light_image=Image.open('images\\Dashboard_label.png'), size=(1366, 770))
    Linear_image_label = customtkinter.CTkLabel(master=frame, image=Linear_image, text="")
    Linear_image_label.place(x=0, y=0)

    my_image = customtkinter.CTkImage(light_image=Image.open('images\\Hostel.jpg'), size=(1366, 400))
    my_label = customtkinter.CTkLabel(master=frame, image=my_image, text="")
    my_label.place(relx=0, rely=0.45)

    create_login_frame()

    def about():
        About_frame = customtkinter.CTkFrame(master=login_window, height=300, width=500, fg_color="#42ABC7")
        About_frame.place(relx=0.3, rely=0.2)

        About_label = customtkinter.CTkLabel(master=About_frame, text="About us", font=("bold", 25), text_color="white")
        About_label.place(relx=0.05, rely=0.15)

        Content_label = customtkinter.CTkLabel(master=About_frame, text="Griha hostel offers a welcoming and \ncomfortable living environment for\n students and professionals. With\n modern amenities and facilities, and a\n supportive community, Griha hostel\n ensures a home-like experience away\n from home.", justify=LEFT,
                                               text_color="white", font=("bold", 20))
        Content_label.place(relx=0.1, rely=0.25)

        def back():
            About_frame.destroy()

        Exit_button = customtkinter.CTkButton(master=About_frame, text="X", command=back, width=30)
        Exit_button.place(relx=0.9, rely=0.05)

    What_btn = customtkinter.CTkButton(master=frame, text="?", bg_color="#3FB5CB", fg_color="#3FB5CB", width=50, text_color="black",
                                       corner_radius=80, font=("bold", 20), command=about)
    What_btn.place(relx=0.7, rely=0.05)

    login_window.mainloop()


login_page()
