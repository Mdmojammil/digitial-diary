from tkinter import*
from admin.addcontact import*
from admin.updatecontact import *
from admin.deletecontact import *
from admin.searchcontact import *
from admin.todaysbirthdaycontact import*
from admin.todaysaniversorycontact import *
from admin.friendofdaycontact import *
from admin.todaymeetingscontact import*



#from search import*
#from update import*
def mainwindow():
    mw=Tk()
    mw.title('Main windows')
    mw.configure(background="red");
    #menu bar

    menubar = Menu(mw)
    # file menu code
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Add",command=addcontact)
    filemenu.add_command(label="Update",command=updatecontact)
    filemenu.add_command(label="Delete",command=deletecontact)
    filemenu.add_command(label="Search",command=searchcontact)
    


    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=mw.quit)

    menubar.add_cascade(label="Contact", menu=filemenu)

    filemenu1 = Menu(menubar, tearoff=0)
    filemenu1.add_command(label="Todays Birthday", command=todaysbirthdaycontact)
    filemenu1.add_command(label="Todays aniversory", command=todaysaniversorycontact)
    filemenu1.add_command(label="friend of day", command=friendofdaycontact)

    menubar.add_cascade(label="Today", menu=filemenu1)
    filemenu2 = Menu(menubar, tearoff=0)



    filemenu2.add_command(label="Todays meetings",command=todaymeetingscontact)


    menubar.add_cascade(label="Meetings", menu=filemenu2)

    mw.config(menu=menubar)

    #insert,update,delete,search,showall
    mw.geometry("500x500+200+100")
    mw.mainloop()