#LIBRARIES
import tkinter as tk

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
w = tk.Label(window, text="Shri Shankaracharya Technical Campus\n\n", font = ('Comic Sans MS', 25), bg = '#002248', fg = '#FFFFFF')
w.pack(anchor = "center")

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



window.mainloop()