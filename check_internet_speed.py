from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+" Mbps"
    up = str(round(sp.upload()/(10**6),3))+" Mbps"
    lab_down.config(text = down)
    lab_up.config(text = up)

if __name__ == '__main__':
    
    window = Tk()

    window.title("Internet Speed Test")
    window.geometry("500x500")
    window.config(bg = 'Blue')

    lab = Label(window, text="Internet Speed Test", 
                font=("Time New Roman",30,"bold"), bg="blue", fg="white")
    lab.place(x=60, y=40,height=50, width=380)

    lab = Label(window, text="Downloading Speed", 
                font=("Time New Roman",30,"bold"))
    lab.place(x=60, y=130, height=50, width=380)

    lab_down = Label(window, text="00", 
                font=("Time New Roman",30,"bold"))
    lab_down.place(x=60, y=190, height=50, width=380)

    lab = Label(window, text="Uploading Speed", 
                font=("Time New Roman",30,"bold"))
    lab.place(x=60, y=270, height=50, width=380)

    lab_up = Label(window, text="00", 
                font=("Time New Roman",30,"bold"))
    lab_up.place(x=60, y=330, height=50, width=380)

    button = Button(window, text="RUN TEST",
                    font=("Time New Roman",30,"bold"),
                    relief=RAISED, bg = "red", fg="black",
                    command= speedcheck)
    button.place(x=60, y= 400, height=50, width=380)

    window.mainloop()