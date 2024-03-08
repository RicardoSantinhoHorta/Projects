from tkinter import *          #Tkinter Library
from tkinter import messagebox
from PIL import Image, ImageTk #Python Imaging Library

#Colors:
purple = "#48216D"

#Login Page
class main():
    #Main code of Login Page
    def __init__(self):
        #Menu Standard configuration
        self.window = Tk()
        self.window.geometry("500x600")
        self.window.title("Login Page")
        self.window.resizable(True, True)
        self.window.configure(background="white")

        #Menu BackGround 
        menuBgImg = ImageTk.PhotoImage(Image.open("images\menuBG.png"))
        label = Label(self.window, image=menuBgImg, background="white")
        label.pack()

        #Login Label
        loginLabel = Label(self.window, text="CONCEPT", font=("Arial Black", 40),foreground= "white" , background=purple)
        loginLabel.place(relx=0.5, rely=0.22, anchor=CENTER)

        #Username Label
        usernameLabel = Label(self.window, text="Username:", font=("Arial Black", 15), foreground= purple , background= "white")
        usernameLabel.place(relx=0.27, rely=0.70, anchor=CENTER)
        
        #Password Label
        passwordLabel = Label(self.window, text="Password:", font=("Arial Black", 15), foreground= purple , background= "white")
        passwordLabel.place(relx=0.27, rely=0.80, anchor=CENTER)
        
        #Username Text
        self.usernameInput = Entry(self.window,font=("Arial Black", 15), background=purple, foreground="white")
        self.usernameInput.place(relx=0.7, rely=0.70, anchor=CENTER)
        
        #Password Text
        self.passwordInput = Entry(self.window,font=("Arial Black", 15), show= "*", background=purple, foreground="white")
        self.passwordInput.place(relx=0.7, rely=0.80, anchor=CENTER)
        
        #Login Button
        loginButton = Button(self.window, text="Log In", font=("Arial Black", 15), background="white", command=self.logInVerification)
        loginButton.place(relx=0.5, rely=0.90, anchor=CENTER)

        self.window.mainloop()
    
    #Verify if a user exists by verifying if the username and password exists and if they are equal to "user"/"123"
    def logInVerification(self):
        if self.passwordInput.get() == "" or self.usernameInput.get() == "":
            messagebox.showerror('Enter','Username or password missing.')
        elif self.passwordInput.get() != "123" or self.usernameInput.get() != "user":
            messagebox.showerror('Enter','Incorrect Password.')
        else:
            self.exit_app()
            main_user_menu()
    
    #Destroy app window function
    def exit_app(self):
        self.window.destroy()

#Main user Menu concept
class main_user_menu():
    def __init__(self):
        #Menu Standard configuration
        self.window = Tk()
        self.window.geometry("500x600")
        self.window.title("Login Page")
        self.window.resizable(True, True)
        self.window.configure(background="white")

        self.window.mainloop()


#Start
main()
    