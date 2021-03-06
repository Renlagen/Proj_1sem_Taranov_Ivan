from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.title('Security Realm')
root.geometry('750x600')
root.configure(bg='white')

var = IntVar()
var1 = IntVar()

Label(text='Active Directory', bg='white', width=15, fg='black', font='Arial 11').place(x=15, y=5)
Label(text='Domains', bg='white', width=15, fg='black', font='Arial 11').place(x=-25, y=40)
Label(text='Domain Name', bg='white', width=15, fg='black', font='Arial 11').place(x=195, y=82)
Entry(width=32, bd=1, bg='white', font='arial 15').place(x=340, y=82)
Entry(width=32, bd=1, bg='white', font='arial 15').place(x=340, y=120)
Label(text='Domain Controller', bg='white', width=13, fg='black', font='Arial 11').place(x=215, y=120)
Button(width=15, bd=0, height=1, text="Delete Domain", bg='grey90', font='Arial 11').place(x=570, y=153)
Button(width=15, bd=0, height=1, text="Add Domain", bg='grey90', font='Arial 11').place(x=207, y=185)
Label(text='Site', bg='white', width=15, fg='black', font='Arial 11').place(x=-45, y=225)
Entry(width=46, bd=1, bg='white', font='arial 15').place(x=205, y=225)
Entry(width=46, bd=1, bg='white', font='arial 15').place(x=205, y=265)
Entry(width=46, bd=1, show="•", bg='white', font='arial 15').place(x=205, y=305)
Label(text='Bind DN', bg='white', width=15, fg='black', font='Arial 11').place(x=-30, y=265)
Label(text='Bind Password', bg='white', width=15, fg='black', font='Arial 11').place(x=-8, y=305)
Label(text='Group Membership Lookup Strategy', bg='white', width=27, fg='black', font='Arial 11').place(x=4, y=345)
Label(text='Remove irrelevant groups', bg='white', width=26, fg='black', font='Arial 11').place(x=-23, y=385)
Combobox(root, width=72, values=(['Automatic'])).place(x=260, y=347)
Checkbutton(bg='white', variable=var).place(x=200, y=387)
Checkbutton(bg='white', variable=var1).place(x=9, y=419)
Label(text='Enable cache', bg='white', width=10, fg='black', font='Arial 11').place(x=35, y=420)
Label(text='Environment Properties', bg='white', width=17, fg='black', font='Arial 11').place(x=10, y=455)
Button(width=7, bd=0, height=1, text="Add", bg='grey90', font='Arial 11').place(x=205, y=455)
Label(text='Test Domain Name', bg='white', width=17, fg='black', font='Arial 11').place(x=-4, y=495)
Entry(width=46, bd=1,bg='white', font='arial 15').place(x=205, y=495)
Label(text='Test Domain Controllers', bg='white', width=17, fg='black', font='Arial 11').place(x=11, y=535)
Entry(width=46, bd=1, bg='white', font='arial 15').place(x=205, y=535)
Label(text='Success', bg='white', width=10, fg='black', font='Arial 11').place(x=185, y=570)
Button(width=15, bd=0, height=1, text="Test a test Domain", bg='grey90', font='Arial 11').place(x=575, y=570)
root.mainloop()
