from tkinter import*
import mysql.connector
from tkinter import messagebox

def todaysbirthdaycontact():
    from datetime import date
    today = date.today()
    print(today)
    def checkBirthday():
        inname=namee.get()
        indob = dobe.get()
        inmno=mble.get()
        inemail=emaile.get()

        inmsg=msge.get("1.0", "end-1c")
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="alam123",
                                      database="diarydatadb")
        if (con):
            cur = con.cursor(prepared=True);
            pre_qry = "search contact set mno=%s,email=%s,dob=%s,msg=%s,name=%s"

            try:
                cur.execute(pre_qry, ( inmno, inemail,indob,inmsg,inmno,inname))
                con.commit();

                if cur.rowcount==1:
                    print("search record")
                else:
                    print("failed to search")
            except:
                print("id not found")


            messagebox.showinfo("search info", "Recoard found")


    inswin=Tk()

    inswin.iconbitmap("assets\\images\\5555.ico")
    inswin.configure(background="purple");



    inswin.title("search data");

    inswin.geometry("600x400+300+200");
    namelbl = Label(inswin, text="Enter name:",font="elephant 12")
    doblbl = Label(inswin, text="Enter date of birthday:", font="elephant 12")
    mnolbl = Label(inswin, text="Enter mobile no:",font="elephant 12")
    emaillbl = Label(inswin, text="Enter email:",font="elephant 12")
    msglbl = Label(inswin, text="Enter Message:", font="elephant 12");

    namee = Entry(inswin,font="elephant 12");
    dobe = Entry(inswin, font="elephant 12");
    mble = Entry(inswin, font="elephant 12");
    emaile = Entry(inswin, font="elephant 12");
    msge=Text(inswin,font="elephant 12",width="20",height="5");

    namelbl.grid(row=0, column=1)
    namee.grid(row=0, column=2)

    doblbl.grid(row=1, column=1)
    dobe.grid(row=1, column=2)

    mnolbl.grid(row=2, column=1)
    mble.grid(row=2, column=2)

    emaillbl.grid(row=3, column=1)
    emaile.grid(row=3, column=2)


    msglbl.grid(row=4, column=1)
    msge.grid(row=4, column=2)

    btn=Button(inswin,text="searchData",command=checkBirthday)
    btn.grid(row=20,column=30)

