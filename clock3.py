import sys
from tkinter import *

import pytz
from datetime import datetime
from tkinter import messagebox
import time, os

from playsound import playsound
from PIL import ImageTk,Image 
from configparser import ConfigParser
import winsound


running = False

hours, minutes, seconds = 0, 0, 0

def tick(val):
    global clock
    window =Toplevel()
    window.geometry("300x130")
    clock=Label(window,font=('Helvetica',30,"bold"),fg="light green", bg="black",bd=16,relief=SUNKEN)
    clock.place(x=18, y=30)
    if val=="btn_24":
        time24()
    elif val=="btn_12":
        time12()
    else:
        createWidgets()      


def time24():
    global clock 
    ts= time.strftime("%H:%M:%S")
    clock["text"]=ts
    clock.after(1000, time24)

def time12():
    global clock
    ts= time.strftime("%I:%M:%S:%p")
    clock["text"]=ts
    clock.after(1000, time12)   


def createWidgets():

    window=Toplevel()
    window.title('Alarm_Clock')
    window.geometry("500x400")
    label1= Label(window,text="Enter the time in hh:mm-",font= ('Helvetica', 20, "bold"), fg= "dark red")
    label1.grid(row=0,column=0,padx=5,pady=5)

    global entry1
    entry1 = Entry(window,width=15)
    entry1.grid(row=0,column=1)

    label2= Label(window, text="Enter the message of alarm-",font= ('Helvetica', 20, "bold"), fg= "dark red")
    label2.grid(row=1,column=0,padx=5,pady=5)

    global entry2
    entry2 = Entry(window,width=15)
    entry2.grid(row=1,column=1)

    but= Button(window,text="Submit" ,width=10, command=submit)
    but.grid(row=2,column=1)
     
    global label3
    label3=Label(window,text="")
    label3.grid(row=3,column=0) 


def message1():
    global entry1,label3
    Alarmtimelabel=entry1.get()
    label3.config(text="The Alarm is counting...")
    messagebox.showinfo("Alarm Clock",f"The alarm time is :{Alarmtimelabel}")

def submit():
    global entry1,entry2,label3
    Alarmtime =entry1.get()
    alarmmessage=entry2.get()
    message1()
    currenttime = time.strftime("%H:%M")
    print(f"The alarm time is:{Alarmtime}")
    while Alarmtime!=currenttime:
        currenttime = time.strftime("%H:%M")
        time.sleep(1)
    if Alarmtime == currenttime:
        print("playing alarm sound...")
        winsound.PlaySound('alarm.wav',winsound.SND_FILENAME)
        label3.config(text="Alarm sound playing...")
        messagebox.showinfo("Alarm message",f"The message is:{alarmmessage}")  


def WorldTime():

    window1=Toplevel()
    window1.title('World_Clock')
    window1.geometry("600x200")

    # create a list of timezones
    timezones = pytz.all_timezones

    # create the dropdown menu
    global timezone_menu
    global dropdown
    dropdown =StringVar(value=timezones)
    timezone_menu =OptionMenu(window1, dropdown, *timezones)
    timezone_menu.pack()


    # create the button to get the time
    global get_time_button
    get_time_button=Button(window1, text="Get Time",command=get_time,font=('Helvetica',30,"bold"))
    get_time_button.pack()

    # create the label to display the time
    global time_label   
    time_label=Label(window1,text="",font=('Helvetica',30,"bold"))
    time_label.pack()

  
def get_time():
    global time_label
    global dropdown
    # get the selected timezone from the dropdown menu
    timezone_name = dropdown.get()
    
    # get the current time for the selected timezone
    timezone = pytz.timezone(timezone_name)
    current_time = datetime.now(timezone)
    
    # update the label with the current time
    time_label.config(text=current_time.strftime('%Y-%m-%d %H:%M:%S %Z'))



def StopWatch():

    window2=Toplevel()
    window2.title('Stopwatch')
    window2.geometry('485x220')

    # label to display time
    global stopwatch_label
    stopwatch_label = Label(window2,text='00:00:00', font=('Arial', 80))
    stopwatch_label.pack()

    # start, pause, reset, quit buttons
    start_button =Button(window2,text='start', height=5, width=7, font=('Arial', 20), command=start)
    start_button.pack(side=LEFT)
    pause_button =Button(window2,text='pause', height=5, width=7, font=('Arial', 20), command=pause)
    pause_button.pack(side=LEFT)
    reset_button =Button(window2,text='reset', height=5, width=7, font=('Arial', 20), command=reset)
    reset_button.pack(side=LEFT)
    quit_button =Button(window2,text='quit', height=5, width=7, font=('Arial', 20), command=window2.quit)
    quit_button.pack(side=LEFT)


# start function
def start():
    global running
    if not running:
        update()
        running = True

# pause function
def pause():
    global stopwatch_label
    global running
    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False

# reset function
def reset():
    global stopwatch_label
    global running
    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False
    # set variables back to zero
    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0
    # set label back to zero
    stopwatch_label.config(text='00:00:00')

# update stopwatch function
def update():
    global stopwatch_label
    # update seconds with (addition) compound assignment operator
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    # format time to include leading zeros
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    # update timer label after 1000 ms (1 second)
    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    # after each second (1000 milliseconds), call update function
    # use update_time variable to cancel or pause the time using after_cancel
    global update_time
    update_time = stopwatch_label.after(1000, update)






root =Tk()
root.title('Digital Clock')
root.geometry("800x700")
img1=PhotoImage(file="12HC3.png")
img2=PhotoImage(file="24HC2.png")
img3=PhotoImage(file="Ac.png")
img4=PhotoImage(file="SW.gif")
img5=PhotoImage(file="world_clock.png")
text=Label(root,text="***DIGITAL CLOCK***", font= ('Helvetica', 20, "bold"), fg= "dark blue")
text.place(x=240, y=20)

btn1= Button(root,image=img1, borderwidth=0, command=lambda: tick("btn_12")).place(anchor=SW,x=0,y=200)
btn2= Button(root,image=img2, borderwidth=0, command=lambda: tick("btn_24")).place(anchor=SW,x=0,y=300)
btn3= Button(root,image=img3, borderwidth=0, command=createWidgets).place(anchor=SW,x=0, y=400)
btn4= Button(root,image=img5, borderwidth=0, command=WorldTime).place(anchor=SW,x=0, y=500)
btn5= Button(root,image=img4, borderwidth=0, command=StopWatch).place(anchor=SW,x=0, y=600)

photo=ImageTk.PhotoImage(Image.open("clock_image.png"))
img_label=Label(root,image=photo)
img_label.place(x=390, y=220)

root.mainloop()