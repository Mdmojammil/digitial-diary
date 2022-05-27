from tkinter import*
import mysql.connector
from tkinter import messagebox

def friendofdaycontact():
    def insert():
        inname=namee.get()
        indob = doae.get()
        inmno=mble.get()
        inemail=emaile.get()

        inmsg=msge.get("1.0", "end-1c")
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="alam123",
                                      database="diarydatadb")
        if (con):
            cur = con.cursor(prepared=True);
            pre_qry = "insert into contact(name,mno,email,dob,message) values(%s,%s,%s,%s,%s)"
            cur.execute(pre_qry, (inname,inmno,inemail,indob,inmsg))
            con.commit();

            messagebox.showinfo("Insert info", "Row inserted successfully")

    inswin=Tk()

    inswin.iconbitmap("assets\\images\\5555.ico")
    inswin.configure(background="yellow");



    inswin.title("add data");

    inswin.geometry("600x400+300+200");
    namelbl = Label(inswin, text="Enter name:",font="elephant 12")
    doalbl = Label(inswin, text="Enter friend of day:", font="elephant 12")
    mnolbl = Label(inswin, text="Enter mobile no:",font="elephant 12")
    emaillbl = Label(inswin, text="Enter email:",font="elephant 12")
    msglbl = Label(inswin, text="Enter Message:", font="elephant 12");

    namee = Entry(inswin,font="elephant 12");
    doae = Entry(inswin, font="elephant 12");
    mble = Entry(inswin, font="elephant 12");
    emaile = Entry(inswin, font="elephant 12");
    msge=Text(inswin,font="elephant 12",width="20",height="5");

    namelbl.grid(row=0, column=1)
    namee.grid(row=0, column=2)

    doalbl.grid(row=1, column=1)
    doae.grid(row=1, column=2)

    mnolbl.grid(row=2, column=1)
    mble.grid(row=2, column=2)

    emaillbl.grid(row=3, column=1)
    emaile.grid(row=3, column=2)


    msglbl.grid(row=4, column=1)
    msge.grid(row=4, column=2)

    btn=Button(inswin,text="insertData",command=insert)
    btn.grid(row=20,column=30)

