# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import tix
import MultiListbox as table

x = 800
y = 600

data = [
        # Jméno, Příjmení, RČ,       ulice,         čp,   město,     PSČ,  poznámka
       ["BLS-0001", "The Four Winds","Kristin Hannah",False, 'Tom Wool', "3/25/2021",True]]




class App(object):

    def _from_rgb(self,rgb):
        return "#%02x%02x%02x" % rgb   

    def __init__(self, master):
        self.master = master


        # form - TODO
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

        


        self._mlb = table.MultiListbox(self.right, (('ID-number', 20), ('Books', 20), ('Author', 12), ('Borrowed', 12), ('Borrowed until', 12), ('Status', 12)))

        for i in range(len(data)):
            self._mlb.insert(END, (data[i][0], data[i][1], data[i][2],data[i][3],data[i][4],data[i][5],data[i][6]))
        self._mlb.subscribe(self._edit)
        self.loadimage = PhotoImage(file="button.png")
        self.roundedbutton = Button(self.right, image=self.loadimage)
        self.roundedbutton["border"] = "0"
        self.roundedbutton.pack(side="top")
        #self.button4= Button(self.right, text="Manage BOOKS",font = "Verdana 20",bg= ,fg='white',border=2)
        #self.button4.pack(expand=True,side=TOP,fill=X,padx=100)
        self._mlb.pack(expand=True,anchor=N,fill=BOTH,pady=20,padx=15)

    def _edit(self, row):
        self._row=row
        if self.opened == False:
            self.master.withdraw()
            self.newWindow = Toplevel(self.master)
            self.newWindow.geometry(f"{x}x400")
            bb = NewWindow(self.newWindow,self.master,self._row)
            self.newWindow.mainloop()
        self.opened = True

        #print (f"{data[self._row][0]} {data[self._row][1]}")

class NewWindow():
    def _from_rgb(self,rgb):
        return "#%02x%02x%02x" % rgb   

    def __init__(self, master,old_window,row):
        print (f"{data[row][0]} {data[row][1]}")
        #old_window.deiconify()
        self.master = master
        self._row = row
        self._jmeno = StringVar()
        self._surname = StringVar()
        self._birth_number = StringVar()
        self._street = StringVar()
        self._number = StringVar()
        self._city = StringVar()
        self._zip = StringVar()

        # form - TODO

        #FRAMES
        self.fLeft = Frame(master)
        self.fTop = Frame(master,borderwidth = 5)
        self.fTop.config(bd=4, relief=GROOVE)
        self.fLeft.pack(side=LEFT,fill=Y)
        self.fTop.pack(fill=X)
        self.fBasicInfo = Frame(master)
        self.fNextInfo = Frame(master, bg = 'red')
                #PRINT LIST INFO
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

        self.Id.insert(END, data[self._row][0])
        self.Book.insert(END, data[self._row][1])
        self.Author.insert(END, data[self._row][2])
        self.Borrowed.insert(END, data[self._row][3])
        self.Borrower.insert(END, data[self._row][4])
        self.DateBor.insert(END, data[self._row][5])
        self.Status.insert(END, data[self._row][6])

        self.confirm_button = Button(self.righter, text='CONFIRM', bg='green').pack()
        self.delete_button = Button(self.righter, text='DELETE', bg='red').pack()
             
def main():
    root = tix.Tk()
    root.geometry(f"{x}x{y}")
    root.wm_title("Formulář")
    app = App(root)
    root.mainloop()
    
main()

