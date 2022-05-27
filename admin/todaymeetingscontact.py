from tkinter import*
import mysql.connector
from tkinter import messagebox

def todaymeetingscontact():
    def insert():
        inname=namee.get()
        inmeetid=meetid.get()
        incontactid=contactid.get()
        indate=date.get()
        inpurpose=purpose.get()

        inmsg=msge.get("1.0", "end-1c")
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="alam123",
                                      database="diarydatadb")
        if (con):
            cur = con.cursor(prepared=True);
            pre_qry = "insert into contact(name,meetingid,contactid,date,purpose,message) values(%s,%s,%s,%s,%s,%s)"
            cur.execute(pre_qry, (inname,inmeetid,incontactid,indate,inpurpose,inmsg))
            con.commit();

            messagebox.showinfo("Insert info", "Row inserted successfully")

    inswin=Tk()

    inswin.iconbitmap("assets\\images\\5555.ico")
    inswin.configure(background="cyan");



    inswin.title("add data");

    inswin.geometry("600x400+300+200");
    namelbl = Label(inswin, text="Enter name:",font="elephant 12")
    meetidlbl = Label(inswin, text="Enter meeting id:", font="elephant 12")
    contactidlbl = Label(inswin, text="Enter contact id:",font="elephant 12")
    datelbl = Label(inswin, text="Enter date:",font="elephant 12")
    purposelbl= Label(inswin, text="Enter purpose:",font="elephant 12")
    msglbl = Label(inswin, text="Enter Message:", font="elephant 12");

    namee = Entry(inswin,font="elephant 12");
    meetid = Entry(inswin, font="elephant 12");
    contactid = Entry(inswin, font="elephant 12");
    date = Entry(inswin, font="elephant 12");
    purpose = Entry(inswin, font="elephant 12");
    msge=Text(inswin,font="elephant 12",width="20",height="5");

    namelbl.grid(row=0, column=1)
    namee.grid(row=0, column=2)

    meetidlbl.grid(row=1, column=1)
    meetid.grid(row=1, column=2)

    contactidlbl.grid(row=2, column=1)
    contactid.grid(row=2, column=2)

    datelbl.grid(row=3, column=1)
    date.grid(row=3, column=2)

    purposelbl.grid(row=4, column=1)
    purpose.grid(row=4, column=2)


    msglbl.grid(row=5, column=1)
    msge.grid(row=5, column=2)

    btn=Button(inswin,text="insertData",command=insert)
    btn.grid(row=20,column=30)

