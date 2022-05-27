from tkinter import*
import mysql.connector
from tkinter import messagebox

def searchcontact():
    def search():
        inid=ide.get()
        inmno=mble.get()
        inemail=emaile.get()

        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="alam123",
                                      database="diarydatadb")
        if (con):
            cur = con.cursor(prepared=True);
            pre_qry = "search contact set mno=%s,email, where id=%s"

            try:
                cur.execute(pre_qry, ( inmno, inemail,inid))
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
    inswin.configure(background="green");



    inswin.title("search data");

    inswin.geometry("600x400+300+200");
    idlbl=Label(inswin,text="Enter id:",font="elephant 12")
    mnolbl = Label(inswin, text="Enter mobile no:",font="elephant 12")
    emaillbl = Label(inswin, text="Enter email:",font="elephant 12")

    ide=Entry(inswin,font="elephant 12");
    mble = Entry(inswin, font="elephant 12");
    emaile = Entry(inswin, font="elephant 12");

    idlbl.grid(row=0,column=1)
    ide.grid(row=0,column=2)

    mnolbl.grid(row=1, column=1)
    mble.grid(row=1, column=2)

    emaillbl.grid(row=2, column=1)
    emaile.grid(row=2, column=2)


    btn=Button(inswin,text="searchdata",command=search)
    btn.grid(row=20,column=30)

