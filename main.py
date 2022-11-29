from tkinter import *
import json

f = ('Times', 14)

# first screen

ws = Tk()
ws.geometry('300x250')
ws.title('Login Scren')
ws.config(bg='light blue')

Label(text='Select an option bellow', font=f, bg='light blue', width=20, height=2).pack()

Label(text='', bg='light blue').pack()


# Register screen, when the user click in the button 'register' this screen appears


def register_screen():
    global ws
    win = Toplevel(ws)
    win.geometry('300x250')
    win.title('Register')
    win.config(bg='light blue')

    #variables
    global username
    global password

    username = StringVar()
    password = StringVar()

    global username_entry
    global password_entry
    # username
    Label(win, text="Email*", font=f, bg='light blue', width=20, height=2).pack()

    username_entry = Entry(win, font=f, textvariable=username)
    username_entry.pack()

    # password
    Label(win, text='Password*', font=f, bg='light blue', width=20, height=2).pack()

    password_entry = Entry(win, font=f, show='*', textvariable=password)
    password_entry.pack()
    Label(win, text='', bg='light blue').pack()


    def registration_success():
        global username_entry
        global password_entry
        username_info = username.get()
        password_info = password.get()

        accounts = {'Username': f'{username_info}', 'Password': f'{password_info}'}
        file2 = open('user.txt', 'a')
        file2.write(json.dumps(accounts) + '\n')
        file2.close()

        Label(win, text='Registration Success', fg='green', font=f).pack()

        username_entry.delete(0,END)
        password_entry.delete(0,END)




    # Login Button
    Button(win, text='Register', font=f, width=15, height=1, command=registration_success).pack()
    return win.mainloop()


# Login screen, appears after we click in the button 'Login'
def login_screen():
    global ws
    win2 = Toplevel(ws)
    win2.geometry('300x250')
    win2.title('Register')
    win2.config(bg='light blue')

    username = StringVar()
    password = StringVar()

    Label(win2, text='E-mail*', font=f, bg='light blue', width=20, height=2).pack()

    username_entry = Entry(win2, font=f,textvariable=username)
    username_entry.pack()

    Label(win2, text='Password*', bg='light blue',font=f, width=20, height=2).pack()

    password_entry = Entry(win2,font=f, textvariable=password)
    password_entry.pack()
    Label(win2, bg='light blue', text='').pack()

    def login_sucess():
        Label(win2, text='Login success!', fg='green', font=f).pack()
        username_entry.delete(0,END)
        password_entry.delete(0,END)

    Button(win2, text='Login', width=15, height=1, font=f, command=login_sucess).pack()
    return win2.mainloop()

# Login button

Button(text='Login', font=f, width=20, height=1, command=login_screen).pack()
Label(text='', bg='light blue').pack()  # label to add a blanck space between the two buttons

# Register button

Button(text='Register', font=f, width=20, height=1, command=register_screen).pack()
ws.mainloop()









