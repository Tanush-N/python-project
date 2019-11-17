from tkinter import *
from tkinter import ttk
import os
def main_account_screen():
    global main_screen
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("300x250") # set the configuration of GUI window 
    main_screen.title("XYZ Super Market") # set the title of GUI window
    
    
    #login_screen.geometry("300x250")
    Label(main_screen, text="Please enter details below to login").pack()
    Label(main_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()
    Label(main_screen, text="Username  ").pack()
    username_login_entry = Entry(main_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(main_screen, text="").pack()
    Label(main_screen, text="Password  ").pack()
    password__login_entry = Entry(main_screen, textvariable=password_verify, show= '*')
    password__login_entry.pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Login", width=10, height=1, command=home_page).pack()
    main_screen.mainloop()
def home_page():
    screen=Toplevel(main_screen)
    screen.geometry("300x250")
    Label(screen, text="Home Page").pack()
    Label(screen, text="").pack()
    Button(screen, text="ITEM",width=20, height=3,bd=10,command=item_page ).pack()
    Button(screen, text="CUSTOMER", width=20, height=3,bd=10,command=customer_page).pack()
    Button(screen, text="LOG OUT", width=10,height=1,command=main_account_screen).pack()
def item_page():
    item_screen=Toplevel(main_screen)
    item_screen.geometry("500x350")
    Label(item_screen, text="Item Page").pack()
    Button(item_screen, text="INSERT",width=20, height=3,bd=10,command=insert_item).pack()
    Button(item_screen, text="UPDATE",width=20, height=3,bd=10,command=update_item).pack()
    Button(item_screen, text="DISPLAY",width=20, height=3,bd=10,command=retreive_item).pack()
    Button(item_screen, text="DELETE",width=20, height=3,bd=10,command=delete_item).pack()
    Button(item_screen, text="DISPLAY ALL",width=20, height=3,bd=10,command=display_item).pack()
    Button(item_screen, text="Back",width=10,height=2,command=home_page).pack()
def customer_page():
    cus_screen=Toplevel(main_screen)
    cus_screen.geometry("500x350")
    Label(cus_screen, text="Customer Page").pack()
    Button(cus_screen, text="INSERT",width=20, height=3,bd=10,command=Insert_customer).pack()
    Button(cus_screen, text="UPDATE",width=20, height=3,bd=10,command=update_customer).pack()
    Button(cus_screen, text="DISPLAY",width=20, height=3,bd=10,command=retreive_customer).pack()
    Button(cus_screen, text="DELETE",width=20, height=3,bd=10,command=delete_customer).pack()
    Button(cus_screen, text="DISPLAY ALL",width=20, height=3,bd=10,command=display_customer).pack()
    Button(cus_screen, text="Back",width=10,height=2,command=home_page).pack()
main_account_screen()

