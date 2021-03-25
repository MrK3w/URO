# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import tix
import time
import MultiListbox as table

x = 900
y = 600

data = [
        # Jméno, Příjmení, RČ,       ulice,         čp,   město,     PSČ,  poznámka
       ["BLS-0001", "The Four Winds","Kristin Hannah",0, 'Tom Wool', "3/25/2021",1],
       ["BLS-0002", "The Four Winds","Kristin Hannah",1, 'Tom Wool', "3/25/2021",1],
       ["BLS-0003", "The Four Winds","Kristin Hannah",0, 'Tom Wool', "3/25/2021",1],
       ["BLS-0004", "The Four Winds","Kristin Hannah",1, 'Tom Wool', "3/25/2021",1],
       ["BLS-0005", "Pepa","Kristin Hannah",0, 'Tom Wool', "3/25/2021",1],
       ["BLS-0006", "Karel","Kristin Hannah",0, 'Tom Wool', "3/25/2021",0]
       ]

searched_book = ["","",""]


class App(object):

    def refresh(self):
        self._mlb.delete(0,END)
        for i in range(len(data)):
            mistake = False 
            for j in range(0,3):
                if searched_book[j] not in data[i][j]:
                    mistake = True
            if mistake == False:
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
        self.right.pack(fill=BOTH,expand=True)
        self.bottom = Frame(master).pack(side=BOTTOM,fill=BOTH,expand=True)
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


        self._mlb = table.MultiListbox(self.bottom, (('ID-number', 20), ('Books', 20), ('Author', 12), ('Borrowed', 12),('Borrower', 12), ('Borrowed until', 12), ('Status', 12)))
        self.refresh()
        self._mlb.subscribe(self._edit)
        self.loadimage = PhotoImage(file="button.png")
        
        self.roundedbutton = Button(self.right, image=self.loadimage,command=self.new_user)
        self.roundedbutton["border"] = "0"
        self.roundedbutton.pack(side="left",padx=(100,0))
        self.newimage = PhotoImage(file="refresh_30px.png")
        self.refreshbutton = Button(self.right,image=self.newimage,command=self.refresh,bg=self._from_rgb((42, 157, 143)),fg='white').pack(side='left',anchor=W,padx=(30,5))
        self.newimage2 = PhotoImage(file="search_32px.png")
        self.searchbutton = Button(self.right,image=self.newimage2,command=self.search,bg=self._from_rgb((42, 157, 143)),fg='white').pack(side='left',anchor=W,padx=5)
        self._mlb.pack(side="bottom",expand=True,fill=BOTH,padx=20)

    def search(self):

        self.newWindow = Toplevel(self.master)
        self.newWindow.geometry("250x280")
        self._row = NONE
        bb = SearchBooks(self.newWindow,self.master)
        self.newWindow.mainloop()
        print(searched_book)

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
        bb = EditBook(self.newWindow,self.master,self._row)
        self.newWindow.mainloop()

class EditBook():
    def _from_rgb(self,rgb):
        return "#%02x%02x%02x" % rgb   

    def check(self):
        if self.Book.get("1.0",'end-1c') == "":
            print("Book was not entered!")
            return False
        if self.Author.get("1.0",'end-1c') == "":
            print("Author was not entered!")
            return False

    def get_id(self):
        if self.Id.get("1.0",'end-1c') == "":
            return "BLS-000"+str(len(data)+1)
        else:
            return self.Id.get("1.0",'end-1c')

    def confirm_user(self):
        if self.check() == False:
            return
        id = self.get_id()
        self.user = [id,self.Book.get("1.0",'end-1c'),self.Author.get("1.0",'end-1c'),self.Borrowed.get("1.0",'end-1c'),self.Borrower.get("1.0",'end-1c'),self.DateBor.get("1.0",'end-1c'),self.Status.get("1.0",'end-1c')]
        self.manage_user()
        self.old_window.deiconify() 
        self.master.withdraw()

    def manage_user(self):
        i = 0
        for row in data:
            if row[0] == self.user[0]:
                data.pop(i)
                data.insert(i,self.user)
                return
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
    
    def click_me(self):
        print(self.i.get())

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
        self.Id = Text(self.right, width=15, height=1,bg="gray",fg="white")
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
        self.i = IntVar()
        if self._row != NONE:
            self.i.set(data[self._row][3])
        self.i.set(data[self._row][3])
        self.Check = Label(self.right, text="Checkbox:", padx=10, pady=15).grid(column=0, row=7)
        self.Check = Checkbutton(self.right, width=15, height=1,variable=self.i,onvalue=1)
        self.Check.grid(column=1, row=7)
        self.b = Button(self.right,text="Click here",command=self.click_me)
        self.b.grid(column=1,row=8)
       
        
        self.Id.delete(1.0, END)
        self.Book.delete(1.0, END)
        self.Author.delete(1.0, END)
        self.Borrowed.delete(1.0, END)
        self.Borrower.delete(1.0, END)
        self.DateBor.delete(1.0, END)
        self.Status.delete(1.0, END)


        if self._row != NONE: 
            self.Id.insert(END, data[self._row][0])
            self.Book.insert(END, data[self._row][1])
            self.Author.insert(END, data[self._row][2])
            self.Borrowed.insert(END, data[self._row][3])
            self.Borrower.insert(END, data[self._row][4])
            self.DateBor.insert(END, data[self._row][5])
            self.Status.insert(END, data[self._row][6])
        self.Id.config(state=DISABLED)
        self.confirm_button = Button(self.righter, text='CONFIRM', bg='green',command =self.confirm_user,width=12,height=3).pack(pady=40)
        self.delete_button = Button(self.righter, text='DELETE', bg='red',command=self.close_window,width=12,height=3).pack(pady=40)
    
class SearchBooks():
    def _from_rgb(self,rgb):
        return "#%02x%02x%02x" % rgb   

    def close_window(self): 
        global searched_book
        searched_book = [self.Id.get("1.0",'end-1c'),self.Book.get("1.0",'end-1c'),self.Author.get("1.0",'end-1c')]
        self.old_window.deiconify()
        self.master.destroy()
        
    def __init__(self, master,old_window):
        self.old_window = old_window
        self.master = master
        self.fTop = Frame(master,borderwidth = 5)
        self.fTop.config(bd=4, relief=GROOVE)
        self.fTop.pack(fill=X)
        self.fBasicInfo = Frame(master)
        self.fNextInfo = Frame(master, bg = 'red')
        self.right = Frame(master)
        self.right.pack(side=LEFT,fill=BOTH,expand=True)

        self.label = Label(self.fTop,text="LIBRARY SYSTEM", font = "Verdana 20",fg = self._from_rgb((42, 157, 143)))
        self.label.pack()        
        self.Id = Label(self.right, text = "ID:", padx=10, pady=15).grid(column = 0, row = 0)
        self.Id = Text(self.right, width=15, height=1)
        self.Id.grid(column=1, row=0)
        self.Book = Label(self.right, text="Book:", padx=10, pady=15).grid(column=0, row=1)
        self.Book = Text(self.right, width=15, height=1)
        self.Book.grid(column=1, row=1)
        self.Author = Label(self.right, text="Author:", padx=10, pady=15).grid(column=0, row=2)
        self.Author = Text(self.right, width=15, height=1)
        self.Author.grid(column=1, row=2)
        
        self.delete_button = Button(self.right, text='CLOSE',fg='white', font = "Verdana 10",bg=self._from_rgb((42, 157, 143)),command=self.close_window,width=15).grid(column=1, row=3,pady=20)
        self.Id.delete(1.0, END)
        self.Book.delete(1.0, END)
        self.Author.delete(1.0, END)
        
        self.Id.insert(END, searched_book[0])
        self.Book.insert(END, searched_book[1])
        self.Author.insert(END, searched_book[2])
       
             
def main():
    root = tix.Tk()
    root.geometry(f"{x}x{y}")
    root.wm_title("Formulář")
    app = App(root)
    root.mainloop()
    
main()

