# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import tix
import time
import MultiListbox as table

x = 900
y = 600

data = [
        # Jméno, Příjmení, RČ,       ulice,         čp,   město,     PSČ,  poznámka
       ["BLS-0001", "The Four Winds","Kristin Hannah",False, 'Tom Wool', "3/25/2021",True]
       ]




class App(object):

    def refresh(self):
        self._mlb.delete(0,END)
        for i in range(len(data)): 
            self._mlb.insert(END, (data[i][0], data[i][1], data[i][2],data[i][3],data[i][4],data[i][5],data[i][6]))

    def _from_rgb(self,rgb):
        return "#%02x%02x%02x" % rgb   

    def __init__(self, master):
        self.master = master    
        self.opened = False
        #FRAMES
        self.fLeft = Frame(master)
        self.fTop = Frame(master,borderwidth = 5)
        self.fTop.config(bd=4, relief=GROOVE)
        self.fLeft.pack(side=LEFT,fill=Y)
        self.fTop.pack(fill=X)
        self.right = Frame(master)
        self.right.pack(side=LEFT,fill=BOTH,expand=True)
        self.fBotBut = Frame(self.right)

        book_image = PhotoImage(file=r"bookmark_208px.png").subsample(2)
        self.radio_button_1 = Button(self.fLeft, image=book_image, bg=self._from_rgb((191, 206, 26)))
        self.radio_button_1.image = book_image
        user_image = PhotoImage(file="contacts_208px.png").subsample(2)
        self.radio_button_2= Button(self.fLeft, image=user_image,bg='white')
        self.radio_button_2.image = user_image
        transfer_image = PhotoImage(file=r"transfer-208px.png").subsample(2)
        self.radio_button_3= Button(self.fLeft, image=transfer_image,bg='white')
        self.radio_button_3.image = transfer_image
        self.radio_button_1.pack(expand=True,fill='both')
        self.radio_button_2.pack(expand=True,fill='both')
        self.radio_button_3.pack(expand=True,fill='both')

        self.label = Label(self.fTop,text="LIBRARY SYSTEM", font = "Verdana 20",fg = self._from_rgb((42, 157, 143)))
        self.label.pack()
    
        home_image = PhotoImage(file=r"home_96px.png").subsample(3)
        self.photolabel = Label(self.fTop,image=home_image)
        
        self.photolabel.place(relx=0.97, rely=0.95, anchor="se")
        self.photolabel.image = home_image


        self._mlb = table.MultiListbox(self.right, (('ID-number', 20), ('Books', 20), ('Author', 12), ('Borrowed', 12),('Borrower', 12), ('Borrowed until', 12), ('Status', 12)))
        self.refresh()
        self._mlb.subscribe(self._edit)
        self.loadimage = PhotoImage(file="button.png")
        
        self.roundedbutton = Button(self.right, image=self.loadimage,command=self.new_user)
        self.roundedbutton["border"] = "0"
        self.roundedbutton.pack(side="top")
        self.refreshbutton = Button(self.right,text="refresh",height = 3,width=10,font="Verdana 12",command=self.refresh,bg=self._from_rgb((42, 157, 143)),fg='white').pack(side="right",expand=True,fill=X,padx=10)
        self._mlb.pack(expand=True,anchor=N,fill=BOTH,pady=20,padx=15)

    def _edit(self, row):
        self._row=row
        self.new_window()
    
    def new_user(self):
        self._row=NONE
        self.new_window()

    def new_window(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.newWindow.geometry(f"{x}x400")
        bb = NewWindow(self.newWindow,self.master,self._row)
        self.newWindow.mainloop()

class NewWindow():
    def _from_rgb(self,rgb):
        return "#%02x%02x%02x" % rgb   

    def check(self):
        if self.Id.get("1.0",'end-1c') == "":
            print("id was not entered!")
            return False
        if self.Book.get("1.0",'end-1c') == "":
            print("Book was not entered!")
            return False
        if self.Author.get("1.0",'end-1c') == "":
            print("Author was not entered!")
            return False

    def confirm_user(self):
        if self.check() == False:
            return
        self.user = [self.Id.get("1.0",'end-1c'),self.Book.get("1.0",'end-1c'),self.Author.get("1.0",'end-1c'),self.Borrowed.get("1.0",'end-1c'),self.Borrower.get("1.0",'end-1c'),self.DateBor.get("1.0",'end-1c'),self.Status.get("1.0",'end-1c')]
        self.manage_user()
        self.old_window.deiconify() 
        self.master.withdraw()

    def manage_user(self):
        i = 0
        for row in data:
            if row[0] == self.user[0]:
                data.pop(i)
            i = i+1
        data.append(self.user)

    def close_window(self): 
        i = 0
        for row in data:
            if row[0] == self.Id.get("1.0",'end-1c'):
                data.pop(i)
            i = i+1
        self.old_window.deiconify()
        self.master.withdraw()
        
    def __init__(self, master,old_window,row):
        self.old_window = old_window
        self.master = master
        self._row = row
        self.fLeft = Frame(master)
        self.fTop = Frame(master,borderwidth = 5)
        self.fTop.config(bd=4, relief=GROOVE)
        self.fLeft.pack(side=LEFT,fill=Y)
        self.fTop.pack(fill=X)
        self.fBasicInfo = Frame(master)
        self.fNextInfo = Frame(master, bg = 'red')
        self.right = Frame(master)
        self.right.pack(side=LEFT,fill=BOTH,expand=True)
        self.righter = Frame(master)
        self.righter.pack(side=LEFT,fill=BOTH,expand=True)
        self.fBotBut = Frame(self.right)
        self.dir = IntVar()
        self.dir.set(1) 
        book_image = PhotoImage(file=r"bookmark_208px.png").subsample(2)
        self.radio_button_1 = Button(self.fLeft, image=book_image, bg=self._from_rgb((191, 206, 26)))
        self.radio_button_1.image = book_image
        user_image = PhotoImage(file="contacts_208px.png").subsample(2)
        self.radio_button_2= Button(self.fLeft, image=user_image,bg='white')
        self.radio_button_2.image = user_image
        transfer_image = PhotoImage(file=r"transfer-208px.png").subsample(2)
        self.radio_button_3= Button(self.fLeft, image=transfer_image,bg='white')
        self.radio_button_3.image = transfer_image
        self.radio_button_1.pack(expand=True,fill='both')
        self.radio_button_2.pack(expand=True,fill='both')
        self.radio_button_3.pack(expand=True,fill='both')

        self.label = Label(self.fTop,text="LIBRARY SYSTEM", font = "Verdana 20",fg = self._from_rgb((42, 157, 143)))
        self.label.pack()

        home_image = PhotoImage(file=r"home_96px.png").subsample(3)
        self.photolabel = Label(self.fTop,image=home_image)
        
        self.photolabel.place(relx=0.97, rely=0.95, anchor="se")
        self.photolabel.image = home_image
        
        self.Id = Label(self.right, text = "ID:", padx=10, pady=15).grid(column = 0, row = 0)
        self.Id = Text(self.right, width=15, height=1)
        self.Id.grid(column=1, row=0)
        self.Book = Label(self.right, text="Book:", padx=10, pady=15).grid(column=0, row=1)
        self.Book = Text(self.right, width=15, height=1)
        self.Book.grid(column=1, row=1)
        self.Author = Label(self.right, text="Author:", padx=10, pady=15).grid(column=0, row=2)
        self.Author = Text(self.right, width=15, height=1)
        self.Author.grid(column=1, row=2)
        self.Borrowed = Label(self.right, text="Borrowed:", padx=10, pady=15).grid(column=0, row=3)
        self.Borrowed = Text(self.right, width=15, height=1)
        self.Borrowed.grid(column=1, row=3)
        self.Borrower = Label(self.right, text="Borrower:", padx=10, pady=15).grid(column=0, row=4)
        self.Borrower = Text(self.right, width=15, height=1)
        self.Borrower.grid(column=1, row=4)
        self.DateBor = Label(self.right, text="Borrowed until:", padx=10, pady=15).grid(column=0, row=5)
        self.DateBor = Text(self.right, width=15, height=1)
        self.DateBor.grid(column=1, row=5)
        self.Status = Label(self.right, text="Status:", padx=10, pady=15).grid(column=0, row=6)
        self.Status = Text(self.right, width=15, height=1)
        self.Status.grid(column=1, row=6)
        
        self.Id.delete(1.0, END)
        self.Book.delete(1.0, END)
        self.Author.delete(1.0, END)
        self.Borrowed.delete(1.0, END)
        self.Borrower.delete(1.0, END)
        self.DateBor.delete(1.0, END)
        self.Status.delete(1.0, END)
#           
        if self._row != NONE: 
            self.Id.insert(END, data[self._row][0])
            self.Id.config(state=DISABLED)
            self.Book.insert(END, data[self._row][1])
            self.Author.insert(END, data[self._row][2])
            self.Borrowed.insert(END, data[self._row][3])
            self.Borrower.insert(END, data[self._row][4])
            self.DateBor.insert(END, data[self._row][5])
            self.Status.insert(END, data[self._row][6])

        self.confirm_button = Button(self.righter, text='CONFIRM', bg='green',command =self.confirm_user,width=12,height=3).pack(pady=40)
        self.delete_button = Button(self.righter, text='DELETE', bg='red',command=self.close_window,width=12,height=3).pack(pady=40)
    
  
             
def main():
    root = tix.Tk()
    root.geometry(f"{x}x{y}")
    root.wm_title("Formulář")
    app = App(root)
    root.mainloop()
    
main()

