from tkinter import*
import mysql.connector
from tkinter import messagebox

def deletecontact():
    def delete():
        id = ide.get()
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="alam123",
                                      database="diarydatadb")
        if (con):
            cur = con.cursor(prepared=True);
            pre_qry = "Delete from contact  where id={}".format(id)

            try:
                cur.execute(pre_qry)
                con.commit();

                if cur.rowcount>0:
                    print("delete record")
                else:
                    print("failed to delete")
            except:
                print("id not found")



            messagebox.showinfo("delete info", "Row deleted successfully")

    inswin=Tk()

    inswin.iconbitmap("assets\\images\\5555.ico")
    inswin.configure(background="blue");



    inswin.title("Delete data");

    inswin.geometry("600x400+300+200");
    idlbl = Label(inswin, text="Enter id:", font="elephant 12")

    ide = Entry(inswin, font="elephant 12");


    idlbl.grid(row=0, column=1)
    ide.grid(row=0, column=2)



    btn=Button(inswin,text="deleteData",command=delete)
    btn.grid(row=20,column=30)

