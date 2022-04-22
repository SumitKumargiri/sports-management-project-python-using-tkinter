#import modules
import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter import *
import os
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()

KEYS = ("Matches Played", "Goals", "Assists", "YC", "RC")

# create a player and save into "stored_data"
def create_player(name, matches=0, goals=0, assists=0, yc=0, rc=0):
    statistics = {}
    for key, val in zip(KEYS, (matches, goals, assists, yc, rc)):
        statistics[key] = tk.IntVar(value=val)
    stored_data[name] = statistics


# a generic function to edit player statistics
def edit_player(parent, name):
    def change(var, delta):
        value = var.get() + delta
        if value >= 0:
            var.set(value)

    def create_form(parent, key, var):
        f = tk.Frame(parent, bd=1, relief="sunken")
        f.pack(side="left")
        tk.Label(f, text=key, width=12, fg="white", bg="blue").grid(row=0, column=0, columnspan=3)
        tk.Button(f, text="-", command=lambda: change(var, -1)).grid(row=1, column=0, sticky="ew")
        tk.Label(f, textvariable=var, width=3).grid(row=1, column=1)
        tk.Button(f, text="+", command=lambda: change(var, +1)).grid(row=1, column=2, sticky="ew")

    tp = tk.Toplevel(parent)
    tp.title("Edit Player Statistics")
    tk.Label(tp, text=name, font="Helvetica 14 bold").pack()
    frame = tk.Frame(tp)
    frame.pack()
    statistics = stored_data[name]
    for col, (key, var) in enumerate(statistics.items(), 1):
        create_form(frame, key, var)
    # make this toplevel like a modal dialog
    tp.grab_set()
    tp.wait_window()


# show player statistics
def add_player_row(parent, row, name):
    tk.Label(parent, text=name, anchor="w").grid(row=row, column=0, sticky="ew")
    statistics = stored_data[name]
    for col, key in enumerate(KEYS, 1):
        tk.Label(parent, textvariable=statistics[key]).grid(row=row, column=col)
    tk.Button(parent, text="Edit", command=lambda: edit_player(root, name)).grid(row=row, column=col+1)


# ask for new player name and create the player
def new_player(parent):
    # get player name
    name = askstring("New Player", "Player Name")
    if name:
        create_player(name)
        add_player_row(parent, len(stored_data), name)


# main block

root = tk.Tk()

stored_data = {}
# store player data
create_player('Daniel Keelagher', 10, 4, 4, 0, 0)
create_player('Joseph Keelagher', 10, 2, 2, 1, 0)
create_player('Benjamin Miller', 10, 0, 0, 1, 0)
create_player('Joran Terlato', 8, 1, 1, 3, 1)
create_player('Arki Gantzos', 9, 3, 2, 0, 0)
create_player('Billy Houndalas', 10, 0, 0, 0, 0)
create_player('Hayato Uematsu', 9, 2, 3, 0, 0)
create_player('Mark Boccari', 10, 1, 1, 2, 0)
create_player('Oliver Gibson', 7, 1, 2, 0, 0)
create_player('Zaid Khaleqi', 9, 2, 0, 0, 0)

# Application title
tk.Label(text="Chelsea FC Player Statistics", font=(None, 15, 'bold'), fg="blue",).pack(pady=5)

# a frame for showing player statistics
table_frame = tk.Frame(root)
table_frame.pack()

# table headings
font="Helvetica 13 bold"
tk.Label(table_frame, text="Player Name", font=font, anchor="w", width=20, fg="white", bg="blue").grid(row=0, column=0, sticky="ew")
for col, key in enumerate(KEYS, 1):
    tk.Label(table_frame, text=key, font=font, width=12, fg="white", bg="blue").grid(row=0, column=col)
tk.Label(table_frame, font=font, anchor="w", fg="white", bg="blue").grid(row=0, column=col+1, sticky="ew")

# player statistics table
for row, name in enumerate(stored_data, 1):
    add_player_row(table_frame, row, name)

# add new player button
tk.Button(root, text="Add New Player", command=lambda: new_player(table_frame)).pack(pady=5)
# Main loop of tkinter
root.mainloop()