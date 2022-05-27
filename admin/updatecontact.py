from tkinter import*
import mysql.connector
from tkinter import messagebox

def updatecontact():
    def update():
        inid=ide.get()
        inname=namee.get()
        inadd = adde.get()
        inmno=mble.get()
        inemail=emaile.get()
        inbgroup=bgroupe.get()
        indob=dobe.get()
        ingen=gene.get()
        incountry=countrye.get()
        incompany=companye.get()

        inmsg=msge.get("1.0", "end-1c")
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="alam123",
                                      database="diarydatadb")
        if (con):
            cur = con.cursor(prepared=True);
            pre_qry = "UPDATE contact set name=%s,address=%s,mno=%s,email=%s,bgroup=%s,dob=%s,gender=%s,country=%s,company=%s,message=%s where id=%s"

            try:
                cur.execute(pre_qry, (inname, inadd, inmno, inemail, inbgroup, indob, ingen, incountry, incompany, inmsg,inid))
                con.commit();

                if cur.rowcount==1:
                    print("update record")
                else:
                    print("failed to updated")
            except:
                print("id not found")


            messagebox.showinfo("update info", "Row updated successfully")

    inswin=Tk()
    inswin.iconbitmap("assets\\images\\5555.ico")
    inswin.configure(background="green");



    inswin.title("update data");

    inswin.geometry("600x400+300+200");
    idlbl=Label(inswin,text="Enter id:",font="elephant 12")
    namelbl = Label(inswin, text="Enter name:",font="elephant 12")
    addresslbl = Label(inswin, text="Enter address:", font="elephant 12")
    mnolbl = Label(inswin, text="Enter mobile no:",font="elephant 12")
    emaillbl = Label(inswin, text="Enter email:",font="elephant 12")
    bgrouplbl = Label(inswin, text="Enter bloodgroup:",font="elephant 12")
    doblbl = Label(inswin, text="Enter date of birth:",font="elephant 12")
    genderlbl = Label(inswin, text="Enter gender:",font="elephant 12")
    countrylbl = Label(inswin, text="Enter Country:",font="elephant 12");
    companylbl = Label(inswin, text="Enter CompanyName:", font="elephant 12");
    msglbl = Label(inswin, text="Enter Message:", font="elephant 12");

    ide=Entry(inswin,font="elephant 12");
    namee = Entry(inswin,font="elephant 12");
    adde = Entry(inswin, font="elephant 12");
    mble = Entry(inswin, font="elephant 12");
    emaile = Entry(inswin, font="elephant 12");
    bgroupe = Entry(inswin, font="elephant 12");
    dobe = Entry(inswin, font="elephant 12");
    gene = Entry(inswin, font="elephant 12");
    countrye = Entry(inswin, font="elephant 12");
    companye = Entry(inswin, font="elephant 12");
    msge=Text(inswin,font="elephant 12",width="20",height="5");

    idlbl.grid(row=0,column=1)
    ide.grid(row=0,column=2)
    namelbl.grid(row=1, column=1)
    namee.grid(row=1, column=2)

    addresslbl.grid(row=2, column=1)
    adde.grid(row=2, column=2)

    mnolbl.grid(row=3, column=1)
    mble.grid(row=3, column=2)

    emaillbl.grid(row=4, column=1)
    emaile.grid(row=4, column=2)

    bgrouplbl.grid(row=5, column=1)
    bgroupe.grid(row=5, column=2)

    doblbl.grid(row=6, column=1)
    dobe.grid(row=6, column=2)
    genderlbl.grid(row=7, column=1)
    gene.grid(row=7, column=2)

    countrylbl.grid(row=8, column=1)
    countrye.grid(row=8, column=2)

    companylbl.grid(row=9, column=1)
    companye.grid(row=9, column=2)

    msglbl.grid(row=10, column=1)
    msge.grid(row=10, column=2)

    btn=Button(inswin,text="updatedata",command=update)
    btn.grid(row=20,column=30)

