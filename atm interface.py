from tkinter import *
from tkinter import messagebox
t=Tk()
global bank
t.title("ATM")
t.geometry("600x500")
pin='1208'
bank=200000
l1=Label(t,text="Welcome To ATM",font = ("comic sans ms",30,"bold"))
l1.place (x=100,y=0)
l2=Label (t,text="Enter your 4 digit pin:",font=("consolas 10 bold"))
l2.place(x=100,y=100)
e1=Entry(t,bd=10)
e1.place(x=300,y=93)
def login():
    x=e1.get()
    t.withdraw()
    if x==pin:
        global t2
        t2=Toplevel()
        t2.geometry("600x500")
        l1=Label(t2,text="Welcome To ATM",font = ("comic sans ms",30,"bold"))
        l1.place(x=100,y=0)
        def withdraw():
            t2.withdraw()
            t3=Toplevel()
            t3.geometry("600x500")
            l1=Label(t3,text="Welcome To ATM",font = ("comic sans ms",30,"bold"))
            l1.place(x=100,y=0)
            l2=Label(t3,text="Enter the amount you want to withdraw:",font=("consolas 10 bold"))
            l2.place(x=100,y=100)
            e2=Entry(t3,bd=10)
            e2.place(x=400,y=93)
            def money():
                global bank
                y=e2.get()
                bank = bank - int(y)
                msg=messagebox.showinfo("withdrawal",'Money successfully withdrawn.... \nCurrent balance = '+ str(bank))
                t3.withdraw()
                t2.deiconify()
            b2=Button(t3,text="Enter",font=("consolas 15 bold"),command = money)
            b2.place(x=230,y=140)
            t3.mainloop()
        b1=Button(t2,text="Cash Withdrawal",font=("consolas 20 bold"),command = withdraw)
        b1.place(x=20,y=150)
        def deposit():
            t2.withdraw()
            t4=Toplevel()
            t4.geometry("600x500")
            l1=Label(t4,text="Welcome To ATM",font = ("comic sans ms",30,"bold"))
            l1.place (x=100,y=0)
            l2=Label(t4,text="Enter the amount you want to deposit:",font=("consolas 10 bold"))
            l2.place(x=100,y=100)
            e2=Entry(t4,bd=10)
            e2.place(x=400,y=93)
            def money():
                global bank
                y=e2.get()
                bank = bank + int(y)
                msg=messagebox.showinfo("deposit",'Money successfully deposited.... \nCurrent balance = '+ str(bank))
                t4.withdraw()
                t2.deiconify()
            b2=Button(t4,text="Enter",font=("consolas 15 bold"),command = money)
            b2.place(x=230,y=140)
            t4.mainloop()
        b2=Button(t2,text="Cash Deposit",font=("consolas 20 bold"),command = deposit)
        b2.place(x=365,y=150)
        def check():
            t2.withdraw()
            t5=Toplevel()
            t5.geometry("600x500")
            l1=Label(t5,text="Welcome To ATM",font = ("comic sans ms",30,"bold"))
            l1.place(x=100,y=0)
            l2=Label(t5,text="Your Current Bank Balance = "+ str(bank),font=("consolas 20 bold"))
            l2.place(x=50,y=100)
            def ok():
                t5.withdraw()
                t2.deiconify()
            b2=Button(t5,text="Ok",font=("consolas 15 bold"),command = ok)
            b2.place(x=230,y=140)
            t5.mainloop()
        b3=Button(t2,text="Check Balance", font=("consolas 20 bold"),command = check)
        b3.place(x=20,y=300)
        b4=Button(t2,text="Exit ATM",font=("consolas 20 bold"),command =exit)
        b4.place(x=365,y=300)
        t2.mainloop()
    else :
        msg=messagebox.showerror("Error", "Wrong Password!!!!")
b1=Button(t,text="Enter",font=("consolas 15 bold"),command = login)
b1.place(x=230,y=140)


        
t.mainloop()
