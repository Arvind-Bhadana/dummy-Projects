from ctypes import pointer
from lib2to3.pgen2.token import PLUS
from tkinter import *
import os

def reset():
    os.system('shutdown /r /t 1')

def rwt():
    os.system('shutdown /r /t 20')

def lout():
    os.system('shutdown -l')

def std():
    os.system('shutdown /s /t 1')

st = Tk()
st.title("ShutDown App")
st.geometry('400x400')
st.config(bg='#87b9b5')

restart_button = Button(st,text='Restart',font=('Time New Roman',10,'bold'),relief=RAISED,
cursor='plus',command=reset)
restart_button.place(x=100,y=50,height=50,width=200)

restart_with_time_button = Button(st,text='Restart with Time',font=('Time New Roman',10,'bold'),relief=RAISED,cursor='plus',command=rwt)
restart_with_time_button.place(x=100,y=120,height=50,width=200)

logout_button = Button(st,text='Log Out',font=('Time New Roman',10,'bold'),relief=RAISED,cursor='plus',command=lout)
logout_button.place(x=100,y=190,height=50,width=200)

shutdown_button = Button(st,text='ShutDown',font=('Time New Roman',10,'bold'),  relief=RAISED,cursor='plus',command=std)
shutdown_button.place(x=100,y=260,height=50,width=200)

st.mainloop()

