# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import tix
import MultiListbox as table


NAME = 0
SURNAME = 1
BIRTH_NUMBER = 2
STREET = 3
NUMBER = 4
CITY = 5
ZIP = 6
NOTE = 7
data = [
        # Jméno, Příjmení, RČ,       ulice,         čp,   město,     PSČ,  poznámka
       ["Petr", "Bílý","045214/1512","17. Listopadu", 15, "Ostrava", 70800,"poznamka"],
       ["Jana", "Zelený","901121/7238","Vozovna", 54, "Poruba", 78511,""],
       ["Karel", "Modrý","800524/5417","Porubská", 7, "Praha", 11150,""],
       ["Martin", "Stříbrný","790407/3652","Sokolovská", 247, "Brno", 54788,"nic"]]



class App(object):

    def __init__(self, master):
        self._row = IntVar()
        self._row = None
        self._jmeno = StringVar()
        self._surname = StringVar()
        self._birth_number = StringVar()
        self._street = StringVar()
        self._number = StringVar()
        self._city = StringVar()
        self._zip = StringVar()

        # form - TODO

        #FRAMES
        self.fTop = Frame(master)
        self.fTop.pack(fill = X)
        self.fBasicInfo = Frame(master)
        self.fNextInfo = Frame(master, bg = 'red')
        self.fBotBut = Frame(master)

        #PRINT LIST INFO

        self._mlb = table.MultiListbox(master, (('Jméno', 20), ('Příjmení', 20), ('Rodné číslo', 12)))

        for i in range(len(data)):
            self._mlb.insert(END, (data[i][0], data[i][1], data[i][2]))
        self._mlb.pack(expand=YES, fill=BOTH, padx=10, pady=10)
        # self._mlb.subscribe( lambda row: self._edit( row ) )
        self._mlb.subscribe(self._edit)

        self.fBasicInfo.pack(pady = 10)
        self.fNextInfo.pack(pady = 10, padx = 100)

        #IMAGES

        self.iNewFile = PhotoImage(file="newFile.png").subsample(2)
        self.iLNewFile = Button(self.fTop, image = self.iNewFile, command=self.comNew)
        self.iSaveFile = PhotoImage(file="savefile.png").subsample(2)
        self.iLSaveFile = Button(self.fTop, image=self.iSaveFile, command=self.comSave)
        self.iLNewFile.pack(side = LEFT)
        self.iLSaveFile.pack(side = LEFT)

        self.lInfo = Label(self.fTop, text="", padx=10, pady=10, fg="red")
        self.lInfo.pack(side = BOTTOM)

        #BASIC INFO

        self.lFName = Label(self.fBasicInfo, text = "Jméno:", padx=10, pady=3).grid(column = 0, row = 0)
        self.tFName = Text(self.fBasicInfo, width=15, height=1)
        self.tFName.grid(column=1, row=0)
        self.lLName = Label(self.fBasicInfo, text="Příjmení:", padx=10, pady=3).grid(column=0, row=1)
        self.tLName = Text(self.fBasicInfo, width=15, height=1)
        self.tLName.grid(column=1, row=1)
        self.lBNum = Label(self.fBasicInfo, text="Rodné číslo:", padx=10, pady=3).grid(column=0, row=2)
        self.tBNum = Text(self.fBasicInfo, width=15, height=1)
        self.tBNum.grid(column=1, row=2)

        #NEXT INFO

        self.nb = tix.NoteBook(master)
        self.nb.add("page1", label="Adresa")
        self.nb.add("page2", label="Poznámka")
        self.nbAdres = self.nb.subwidget_list["page1"]
        self.nbNotes = self.nb.subwidget_list["page2"]
        self.nb.pack(expand=1, fill=BOTH)
        #   ADRESA
        self.lStr = Label(self.nbAdres, text="Ulice:", padx=10, pady=3).grid(column=0, row=0)
        self.tStr = Text(self.nbAdres, width=15, height=1)
        self.tStr.grid(column=1, row=0)
        self.lCity = Label(self.nbAdres, text="Město:", padx=20, pady=3).grid(column=0, row=1)
        self.tCity = Text(self.nbAdres, width=15, height=1)
        self.tCity.grid(column=1, row=1)
        self.lPSC = Label(self.nbAdres, text="PSČ:", padx=20, pady=3).grid(column=0, row=2)
        self.tPSC = Text(self.nbAdres, width=8, height=1)
        self.tPSC.grid(column=1, row=2, sticky = W)
        self.lCP = Label(self.nbAdres, text="č.p.:", padx=20, pady=3).grid(column=2, row=0)
        self.tCP = Text(self.nbAdres, width=5, height=1)
        self.tCP.grid(column=3, row=0)

        #   POZNÁMKA
        self.lNote = Label(self.nbNotes, text="Poznámka:", padx=10, pady=3).pack(side = LEFT)
        self.tNote = Text(self.nbNotes, width=35, height=5)
        self.tNote.pack(side = RIGHT, fill = BOTH, expand = True)

        # menu - TODO
        master.bind("<Button-3>", self.do_popup)

        self.popup = Menu(master, tearoff=0)
        self.popup.add_command(label="Nový záznam", command=self.comNew)
        self.popup.add_command(label="Uložit záznam", command=self.comSave)
        self.popup.add_command(label="Konec", command = master.destroy)

        # tabs - TODO
        #self._nb = tix.NoteBook()

        # buttons - TODO
        self.fBotBut.pack(pady = 10)
        self.bCancel = Button(self.fBotBut, text = "Konec", width=15, command = master.destroy).pack(side = LEFT)
        self.bNew = Button(self.fBotBut, text="Nový záznam", width=15,command=self.comNew).pack(side = LEFT)
        self.bSave = Button(self.fBotBut, text="Uložit záznam", width=15,command=self.comSave).pack(side = LEFT)

    def do_popup(self, event):
        # display the popup menu
        try:
            self.popup.tk_popup(event.x_root, event.y_root)
        finally:
            self.popup.grab_release()

    def _edit(self, row):
        self._row=row
        
        # assign actual values to variables - TODO
        # deleting - TODO
        # inserting - TODO
        # new window - TODO

        self.lInfo["text"] = ""

        #Delete and insert new values
        self.tFName.delete(1.0, END)
        self.tLName.delete(1.0, END)
        self.tBNum.delete(1.0, END)
        self.tStr.delete(1.0, END)
        self.tCity.delete(1.0, END)
        self.tPSC.delete(1.0, END)
        self.tCP.delete(1.0, END)
        self.tNote.delete(1.0, END)

        self.tFName.insert(END, data[self._row][0])
        self.tLName.insert(END, data[self._row][1])
        self.tBNum.insert(END, data[self._row][2])
        self.tStr.insert(END, data[self._row][3])
        self.tCity.insert(END, data[self._row][5])
        self.tPSC.insert(END, data[self._row][6])
        self.tCP.insert(END, data[self._row][4])
        self.tNote.insert(END, data[self._row][7])

        #print (row)


    def comNew(self):

        self.lInfo["text"] = ""

        self.tFName.delete(1.0, END)
        self.tLName.delete(1.0, END)
        self.tBNum.delete(1.0, END)
        self.tStr.delete(1.0, END)
        self.tCity.delete(1.0, END)
        self.tPSC.delete(1.0, END)
        self.tCP.delete(1.0, END)
        self.tNote.delete(1.0, END)

    def comSave(self):

        contact = [self.tFName.get(1.0, END)[:-1], self.tLName.get(1.0, END)[:-1],
                   self.tBNum.get(1.0, END)[:-1], self.tStr.get(1.0, END)[:-1], self.tCP.get(1.0, END)[:-1],
                   self.tCity.get(1.0, END)[:-1], self.tPSC.get(1.0, END)[:-1], self.tNote.get(1.0, END)[:-1]]

        for c in data:
            if self.tBNum.get(1.0, END)[:-1] == c[2]:
                self.lInfo["fg"] = "red"
                self.lInfo["text"] = ("Chyba, nemůžeme evidovat 2 uživatele se stejným\nrodným číslem! R. č. {0} již je v databázi!".format(self.tBNum.get(1.0, END)[:-1]))
                return

        if self.tFName.get(1.0, END)[:-1] == "" or self.tLName.get(1.0, END)[:-1] == "" or self.tBNum.get(1.0, END)[:-1] == "" or self.tStr.get(1.0, END)[:-1] == "" \
                or self.tCP.get(1.0, END)[:-1] == "" or self.tCity.get(1.0, END)[:-1] == "" or self.tPSC.get(1.0, END)[:-1] == "":

            self.lInfo["fg"] = "red"
            self.lInfo["text"] = "Chyba, pro vložení uživatele zadejte\nvšechny důležité informace!"
            return

        self.lInfo["fg"] = "green"
        self.lInfo["text"] = "Uživatel s rodným číslem {0}\nbyl úspěšně vložen do databáze!".format(self.tBNum.get(1.0, END)[:-1])

        data.append(contact)

        for i in range(len(data)):
            self._mlb.delete(0)

        for i in range(len(data)):
            self._mlb.insert(END, (data[i][0], data[i][1], data[i][2]))


             
def main():
    root = tix.Tk()
    root.wm_title("Formulář")
    app = App(root)
    root.mainloop()
    
main()

