
from playsound import playsound
from tkinter import *
import datetime
import time


def alarm(set_alarm):
    while True:
        time.sleep(1)
        date = datetime.datetime.now()
        now = date.strftime("%H:%M:%S")
        print(now)
        if now == set_alarm:
            print("Alarm Clock")
            playsound("mixkit-digital-clock-digital-alarm-buzzer-992.wav")
            break

def getvalue():
    set_alarm = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm)

root = Tk()

root.geometry("700x750")
icon=PhotoImage(file="5-crying-out-loud-alarm-clock-emoji-cartoon-clipart (1).png")
image=Label(root,image=icon).place(x=0,y=0)
info = Label(root,text = "(24)Hour  Min  Sec").place(x =250,y=230)
set_time = Label(root,text = "Set Time",relief = "solid",font=("Cambria",10,"bold")).place(x=150,y=260)


# Entry Variables

hour = StringVar()
min = StringVar()
sec = StringVar()



# Entry Widget
hour_E = Entry(root,textvariable = hour,bg = "grey",width =4).place(x=250,y=260)
min_E = Entry(root,textvariable = min,bg = "grey",width = 4).place(x=305,y=260)
sec_E = Entry(root,textvariable = sec,bg = "grey",width = 4).place(x=350,y=260)

submit = Button(root,text = "Set Alarm",width =15,bg="MAGENTA",fg="BLACK",command = getvalue).place(x =250,y=300)

root.mainloop()
