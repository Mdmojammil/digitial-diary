# Import Module
from tkinter import *
import time
from admin.main import*
from threading import *
from playsound import playsound

# Create Object 
root = Tk()

# Set geometry


root.geometry("1366x768")
root.iconbitmap("assets\\images\\5555.ico")
root.configure(background="orange");
root.title("Digital Contact Diary")
lb1=Label(root,text="DIGITAL CONTACT DIARY",bg="red",fg="white",font=("elephant",40))

lb2=Label(root,text="D",bg="black",fg="white",font=("elephant",35))
lb3=Label(root,text="C",bg="black",fg="white",font=("elephant",35))
lb4=Label(root,text="D",bg="black",fg="white",font=("elephant",35))
lb5=Label(root,text="System",bg="black",fg="white",font=("elephant",35))

# use threading

def threading():
	# Call work function
	t1=Thread(target=work)
	t1.start()

# work function
def work():
    playsound('assets\sounds\Alarm04.wav')
    time.sleep(1)
    lb1.place(x=170,y=40)

    time.sleep(.5)
    lb2.place(x=420,y=280)
    time.sleep(.5)

    lb3.place(x=520,y=280)

    time.sleep(.5)

    lb4.place(x=620,y=280)
    time.sleep(.5)

    lb5.place(x=720,y=280)

    time.sleep(3)
    start()

# Create Button
threading()
# Execute Tkinter


root.mainloop()

