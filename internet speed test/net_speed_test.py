from cProfile import label
from tkinter import *
from tkinter import font
import speedtest

def speed_chack():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),2)) + 'Mbps'
    up = str(round(sp.upload()/(10**6),2)) + 'Mbps'
    lebel_down.config(text=down)
    lebel_up.config(text=up)

pop = Tk()
pop.title('Internet speed test')
pop.geometry('400x400')
pop.config(bg='black')

lebel_1 = Label(pop,text='Internet speed test', font=('Time New Roman',20,'bold'),bg='black',fg='white')
lebel_1.place(x=80,y=40)

lebel_2 = Label(pop,text='Dawnload speed', font=('Time New Roman',15,'bold'),bg='black',fg='white')
lebel_2.place(x=120,y=100)

lebel_down = Label(pop,text='00', font=('Time New Roman',10,'bold'),bg='black',fg='white')
lebel_down.place(x=190,y=140)

lebel_4 = Label(pop,text='Upload speed ', font=('Time New Roman',15,'bold'),bg='black',fg='white')
lebel_4.place(x=130,y=180)

lebel_up = Label(pop,text='00', font=('Time New Roman',10,'bold'),bg='black',fg='white')
lebel_up.place(x=190,y=220)


label_6 = Button(pop,text='check speed',font=('Time New Roman',20,'bold'),relief=RAISED,command=speed_chack)
label_6.place(x=110,y=280,height=30,width=180)


pop.mainloop()