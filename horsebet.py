import random, sys, time
import tkinter as tk
from tkinter import Toplevel, messagebox
from datetime import datetime
from time import strftime

logins = {
    'admin' : 'admin',
    'user1' : 'password1',
}

horses = {
    'Thunder' : 2,
    'Storm' : 5,
    'Shadow' : 3,
    'Ghost' : 4
}

def horserace():
    global amount
    
    win_horse = random.choice(list(horses.keys()))

    if horse == 'Thunder':
        win = (amount*2)
        lose = (amount-amount)

    elif horse == 'Storm':
        win = (amount*5)
        lose = (amount-amount)

    elif horse == 'Shadow':
        win = (amount*3)
        lose = (amount-amount)

    elif horse == 'Ghost':
        win = (amount*4)
        lose = (amount-amount)

    if horse == win_horse:
        amount = win
        messagebox.showinfo('Result', f'Congratulations {win_horse} won the race')
        messagebox.showinfo('Winning',f'Your winnings of {amount} will be withdrawn')
    else:
        amount = lose
        messagebox.showinfo('Result',f'Unfortunately {win_horse} won the race')

    with open('scorelog.txt','a') as file:
        time = datetime.now()
        time = str(time)
        winnings = str(amount)
        file.write('Horse: ' + horse + '\n' + 'Winnings £' + winnings + '\n' + time + '\n' + '----------' +'\n')

    home.destroy()
    homepage()
        
def checkhorse():
    global horse

    horse = horsewin_entry.get()

    if horse in horses:
        horsewin.destroy()
        messagebox.showinfo('Confirmation','The race will start shortly')
        horserace()
    else:
        horsewin.destroy()
        messagebox.showinfo('Error','Horse does not exist')
        choosehorse()

def choosehorse():
    global horsewin, horsewin_entry
    horsewin = Toplevel()
    horsewin.title('horsebet')
    horsewin.geometry('280x80+0+0')
    horsewin.resizable(False,False)

    depositwin.destroy()

    horsewin_title = tk.Label(
        horsewin,
        text='Please type in your chosen horse',
        font=('Arial',15,'bold')
    )
    horsewin_title.pack()

    horsewin_entry = tk.Entry(horsewin)
    horsewin_entry.pack()

    horsewin_button = tk.Button(
        horsewin,
        text='Submit',
        font=('Arial'),
        command=checkhorse
    )
    horsewin_button.pack()

def checkdeposit():
    global amount
    try:
        amount = float(deposit_entry.get())
    except ValueError:
        messagebox.showinfo('Error','A value must be entered')
        return

    if amount == 0:
        messagebox.showinfo('Error','A value must be entered')
        depositwin.destroy()
        depositfunc()
    else:
        messagebox.showinfo('Confirmation','Successfully added to your balance')
        choosehorse()

def depositfunc():
    global deposit_entry, depositwin

    depositwin = Toplevel()
    depositwin.title('horsebet')
    depositwin.geometry('210x110+0+0')
    depositwin.resizable(False,False)

    deposit_title = tk.Label(
        depositwin,
        text='Deposit',
        font=('Arial',15,'bold')
    )
    deposit_title.grid(
        row=1,
        column=1,
        columnspan=2
    )

    deposit_label = tk.Label(
        depositwin,
        text='£',
        font=('Arial')
    )
    deposit_label.grid(
        row=2,
        column=1
    )

    deposit_entry = tk.Entry(depositwin)
    deposit_entry.grid(
        row=2,
        column=2
    )

    deposit_button = tk.Button(
        depositwin,
        text='Add To Balance',
        font=('Arial'),
        width=20,
        command = checkdeposit
    )
    deposit_button.grid(
        row=3,
        column=1,
        columnspan=2
    )

    deposit_cancel = tk.Button(
        depositwin,
        text='Back',
        font=('Arial'),
        width=20,
        command=depositwin.destroy
    )
    deposit_cancel.grid(
        row=4,
        column=1,
        columnspan=2
    )

def checkusr():
    usr = l3.get()
    pwd = l5.get()

    if usr in logins and logins[usr] == pwd:
        loginpage.destroy()
        homepage()
    
    else:
        messagebox.showinfo('Error','Incorrect login details')
        login()

def checkage():
    age = int(age_entry.get())
    if age >= 18:
        login()
    
    else:
        messagebox.showinfo('Error','You must be 18 or older to play')

def logout():
    messagebox.showinfo('Confirmation','Successfully logged out')
    login()
    home.destroy()

def registered():
    usr = usr_entry.get()
    pwd = pwd_entry.get()

    logins.update({usr : pwd})
    messagebox.showinfo('Confirmation','Account Successfully Created')
    homepage()

def register():
    global register_acc, usr_entry, pwd_entry
    register_acc = Toplevel()
    register_acc.title('horsebet')
    register_acc.geometry('280x118+0+0')
    register_acc.resizable(False,False)
    
    usr_label = tk.Label(
        register_acc,
        text='Username',
        font=('Arial',15)
    )
    usr_label.grid(
        row=1,
        column=1
    )

    usr_entry = tk.Entry(register_acc)
    usr_entry.grid(
        row=1,
        column=2
    )

    pwd_label = tk.Label(
        register_acc,
        text='Password',
        font=('Arial',15)
    )
    pwd_label.grid(
        row=2,
        column=1    
    )

    pwd_entry = tk.Entry(register_acc)
    pwd_entry.grid(
        row=2,
        column=2
    )

    register_button = tk.Button(
        register_acc,
        text='Register',
        width=20,
        font=('Arial'),
        command=registered
    )
    register_button.grid(
        row=3,
        column=1,
        columnspan=2
    )

    exit_button = tk.Button(
        register_acc,
        text='Exit',
        width=20,
        font=('Arial'),
        command=sys.exit
    )
    exit_button.grid(
        row=4,
        column=1,
        columnspan=2
    )

def login():
    global l3,l5,loginpage
    loginpage = Toplevel()
    loginpage.title('horsebet')
    loginpage.geometry('280x180+0+0')
    loginpage.resizable(False,False)

    l1 = tk.Label(
        loginpage,
        text='Login:',
        width=20,
        font=('Arial',20,'bold')
    )
    l1.grid(
        row=1,
        column=1,
        columnspan=2
    )

    l2 = tk.Label(
        loginpage,
        text='Username',
        font=('Arial',15)
    )
    l2.grid(
        row=2,
        column=1
    )

    l3 = tk.Entry(loginpage)
    l3.grid(
        row=2,
        column=2
    )

    l4 = tk.Label(
        loginpage,
        text='Password',
        font=('Arial',15)
    )
    l4.grid(
        row=3,
        column=1
    )

    l5 = tk.Entry(loginpage)
    l5.grid(
        row=3,
        column=2
    )

    l6 = tk.Button(
        loginpage,
        text='Login',
        width=20,
        command=checkusr
    )
    l6.grid(
        row=4,
        column=1,
        columnspan=2,
        pady=0
    )

    l7 = tk.Button(
        loginpage,
        text='Register',
        width=20,
        command=register
    )
    l7.grid(
        row=5,
        column=1,
        columnspan=2,
        pady=0
    )

    l8 = tk.Button(
        loginpage,
        text='Exit',
        width=20,
        command=sys.exit
    )
    l8.grid(
        row=6,
        column=1,
        columnspan=2,
        pady=0
    )

def homepage():
    def time():
        current_time = strftime("%H:%M:%S")
        time_label.config(text=current_time)
        time_label.after(1000, time)

    messagebox.showinfo('Error','Your balance will be withdrawn after each race')    
    
    global amount, home
    amount = float(0)

    home = Toplevel()
    home.update_idletasks()
    home.geometry('340x200+0+0')
    home.title('horsebet')
    home.resizable(False,False)
    
    home_title = tk.Label(
        home,
        text='horsebet',
        font=('Arial',20, 'bold'),
        width=20,
        height=2,
        anchor='center'
    )
    home_title.grid(
        row=1,
        column=1,
        columnspan=4
    )

    horse_title = tk.Label(
        home,
        text='Todays Horses:',
        font=('Arial',15,'bold')
    )
    horse_title.grid(
        row=3,
        column=1
    )

    horse_1 = tk.Label(
        home,
        text='Thunder | 2/10',
        font=('Arial',15)
    )
    horse_1.grid(
        row=4,
        column=1
    )

    horse_2 = tk.Label(
        home,
        text='Storm | 5/10',
        font=('Arial',15)
    )
    horse_2.grid(
        row=5,
        column=1
    )

    horse_3 = tk.Label(
        home,
        text='Shadow | 3/10',
        font=('Arial',15)
    )
    horse_3.grid(
        row=6,
        column=1
    )

    horse_4 = tk.Label(
        home,
        text='Ghost | 4/10',
        font=('Arial',15)
    )
    horse_4.grid(
        row=7,
        column=1
    )

    time_label = tk.Label(
        home,
        font=('Arial',20)
    )
    time_label.grid(
        row=3,
        column=3,
        columnspan=2,
        pady=0
    )

    bet_button = tk.Button(
        home,
        text='Place Bet',
        width=20,
        command=depositfunc
    )
    bet_button.grid(
        row=4,
        column=3,
        columnspan=2,
        pady=0
    )
    
    logout_button = tk.Button(
        home,
        text='Logout',
        width=20,
        command=logout
    )
    logout_button.grid(
        row=5,
        column=3,
        columnspan=2,
        pady=0
    )

    time()

    loginpage.destroy()
    register_acc.destroy()

root = tk.Tk()
root.title('horsebet')
root.geometry('230x90+0+0')
root.resizable(False,False)

age_title = tk.Label(
    root,
    text='Please verify your age',
    font=('Arial',20)
)
age_title.grid(
    row=1,
    column=1,
    columnspan=2
)

age_label = tk.Label(
    root,
    text='Age:',
    font=('Arial',15)
)
age_label.grid(
    row=2,
    column=1
)

age_entry = tk.Entry(root)
age_entry.grid(
    row=2,
    column=2
)

submit_button = tk.Button(
    root,
    text='Submit',
    command=checkage
)
submit_button.grid(
    row=3,
    column=1,
    columnspan=2
)

root.mainloop()