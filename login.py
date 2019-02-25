#LIBRARIES
import tkinter as tk

login={"CSELECT01":["0001","Kamal Mehta"],"CSELECT02":["0002","Akanksha Choubey"],"CSELECT03":["0003","Abhishek Dewangan"],"CSELECT04":["0004","Rajesh Tiwari"],"CSELECT05":["0005","Krishna Kumar Pandey"],"CSELECT06":["0006","Manjula Swarnkar"],"CSELECT07":["0007","Yamini Chauhan"], "CSELECT08":["0008","Siddharth Choubey"], "CSELECT09":["0009","Samta Gajbhiye"],"CSELECT10": ["0010", "Yogesh Kumar Sahu"], "CSELECT11":["0011","Megha Mishra"], "CSELECT12":["0012","Vishnu Mishra"],"CSELECT13": ["0013", "Sampada Massey"], "CSELECT14":["0014","Prageet Vajpayee"]}


#WINDOW CONFIGURATIONS
window = tk.Tk()
window.title('SSTC Automatic Time-Table Generator')
window.geometry("1000x600+200+50")
window.configure(bg = '#002248')

#LOGIN PAGE SSTC LOGO
logo = tk.PhotoImage(file = "sstc.png")
default_image_label = tk.Label(window, image = logo)
default_image_label.pack(pady = 50)

#LOGIN PAGE HEADING
w = tk.Label(window, text="Shri Shankaracharya Technical Campus", font = ('Comic Sans MS', 25), bg = '#002248', fg = '#FFFFFF')
w.pack(anchor = "center")
v = tk.Label(window, text="Automatic Time-Table Generator", font = ('Comic Sans MS', 20), bg = '#002248', fg = '#FFFFFF')
v.pack(anchor = "center")

#LOGIN PAGE ENTRY
user_name = tk.Label(text = "Username: ", bg = '#002248', fg = '#FFFFFF')
user_name.pack(anchor = "center")
user_ = tk.Entry()
user_.pack(anchor = "center")
password = tk.Label(text = "Password: ", bg = '#002248', fg = '#FFFFFF')
password.pack(anchor = "center")
pass_ = tk.Entry(window, show = '*', width = 20)
pass_.pack(anchor = "center")
login_button = tk.Button(text = "Login")
login_button.pack(pady = 10)
username=user_.get()
password=pass_.get()

#validation of user

def validation():
    if username in login.key():
        if password==login["username"]:
            Button(f1, text='login', command=lambda:raise_frame(disp_timetable)).pack()
            Label(f1, text='FRAME 1').pack()
        else:
            messagebox.showinfo("not a valid password.")


validation()

#frame collection and accessing

from tkinter import *
def raise_frame(frame):
    frame.tkraise()

root = Tk()

log = Frame(root)
disp_timetable = Frame(root)
modified_timetable = Frame(root)

#frame switching
from tkinter import *
def raise_frame(frame):
    frame.tkraise()

root = Tk()

log = Frame(root)
disp_timetable = Frame(root)
modified_timetable = Frame(root)


"""for frame in (log,disp_timetable,modified_timetable):
    frame.grid(row=0, column=0, sticky='news')


Label(f2, text='FRAME 2').pack()
Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

Label(f3, text='FRAME 3').pack(side='left')
Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

"""

raise_frame(f1)
root.mainloop()


window.mainloop()

