#------------------------------------------------------------------------------#
# Obycejne tlacitko                                                            #
#------------------------------------------------------------------------------#
from tkinter import *

class button1:
  def __init__(self, master):
    self.fr = Frame(master)
    self.bu1 = Button(self.fr, text="tlacitko1", command=self.fr.quit)
    self.bu2 = Button(self.fr, text="tlacitko2", command=self.fr.quit)
    self.bu3 = Button(self.fr, text="tlacitko3", command=self.fr.quit)
    self.bu4 = Button(self.fr, text="tlacitko4", command=self.fr.quit)
    self.fr.master.title("tk")
    self.fr.pack()
    self.bu1.pack(side=BOTTOM)
    self.bu2.pack(side=BOTTOM)
    self.bu3.pack(side=LEFT)
    self.bu4.pack(side=RIGHT)

class button2:
   def __init__(self, master):
    self.fr = Frame(master)
    self.bu1 = Button(self.fr, text="tlacitko1", command=self.fr.quit)
    self.bu2 = Button(self.fr, text="tlacitko2", command=self.fr.quit)
    self.bu3 = Button(self.fr, text="tlacitko3", command=self.fr.quit)
    self.bu4 = Button(self.fr, text="tlacitko4", command=self.fr.quit)
    self.fr.master.title("tk")
    self.fr.pack()
    self.bu1.pack(side=LEFT)
    self.bu2.pack(side=RIGHT)
    self.bu3.pack(side=TOP)
    self.bu4.pack(side=BOTTOM)

root = Tk()
root1 = Tk()
app = button1(root)
app2 = button2(root1)
root.mainloop()
root1.mainloop()
#------------------------------------------------------------------------------#



