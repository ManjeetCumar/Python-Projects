'''
To execute:

put -i before your filename. For example: python -i yourfile.py

this will start the IDLE in the command line
'''

from tkinter import *
import os 

def restart():
    os.system("shutdown /r /t 1")
def restart_wtime():
    os.system("shutdown /r /t 200")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")



window = Tk()
window.title("ShutDown App")  # gives title to window
window.geometry("500x500")    # window size
window.config(bg="Blue")      # sets color to blue

restart_button = Button(window, text = "Restart", 
                        font = ("Time New Roman", 20, "bold"),
                        relief=RAISED, cursor = "plus", 
                        command=restart)
restart_button.place(x = 150, y = 60, height = 50, width=200)

restart_button_w_time = Button(window, text = "Restart Time", 
                        font = ("Time New Roman", 20, "bold"),
                        relief=RAISED, cursor = "plus",
                        command=restart_wtime)
restart_button_w_time.place(x = 150, y = 170, height = 50, width=200)

logout_button = Button(window, text = "Logout", 
                        font = ("Time New Roman", 20, "bold"),
                        relief=RAISED, cursor = "plus",
                        command=logout)
logout_button.place(x = 150, y = 270, height = 50, width=200)


shutdown_button = Button(window, text = "Shutdown", 
                        font = ("Time New Roman", 20, "bold"),
                        relief=RAISED, cursor = "plus",
                        command=shutdown)
shutdown_button.place(x = 150, y = 370, height = 50, width=200)


window.mainloop()