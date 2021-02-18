# -*- coding: utf-8 -*-

from tkinter import *
from math import sqrt
import tkinter.font
from tkinter import messagebox

class myApp:
  
    def prevod(self, event=None):
        self.ca.delete("all")
        try:
            if int(self.dir.get() == 1):
                x = self.ent_in.get()
                celsius = int(x)
                v = int(x)*(9/5)+32
            else:
                x = self.ent_in.get()
                v = (float(x) - 32) / 1.8
                celsius = v
            if celsius > 50:
                celsius = 50
            elif celsius < -20:
                celsius = -20
            self.ent_out.delete(0, END)
            self.ent_out.insert(0, str(round(v, 2)))
            self.ca.create_image(150, 200, image=self.photo)
            my_rect = self.ca.create_rectangle(146, 230, 152, 230 + (-3*celsius), fill="red")
           
        except ValueError:
            messagebox.showerror("Error", "Vstup je špatně zadaný")

    def __init__(self, root):

        #function
        root.title('Převodník teplot')
        root.resizable(True, True)
        root.bind('<Return>', self.prevod)        

        #font
        def_font = tkinter.font.nametofont("TkDefaultFont")
        def_font.config(size=16)
        #main frames left and rigth
        self.left_frame = Frame(root)
        self.right_frame = Frame(root)
        
        self.control_frame = LabelFrame(self.left_frame, text="Smer prevodu")

        self.dir = IntVar()
        self.dir.set(1) 
        self.radio_button_1 = Radiobutton(self.control_frame, variable=self.dir, value= 1, text="C => F")
        self.radio_button_2= Radiobutton(self.control_frame, variable=self.dir, value= 2, text="F => C")

        self.ent_frame = LabelFrame(self.left_frame)
        self.lbl_in = Label(self.ent_frame, text="Vstup")
        self.ent_in = Entry(self.ent_frame, width=10, font = def_font,justify='center')
        self.ent_in.insert(0, '0')

        self.lbl_out = Label(self.ent_frame, text="Vystup")
        self.ent_out = Entry(self.ent_frame, width=10, font = def_font,justify='center')
        
        self.button_1 = Button(self.ent_frame, text = "Prevod",command=self.prevod)

        self.ca = Canvas(self.right_frame, width=300, height=400)
        self.photo = PhotoImage(file="th_empty.png")
        self.ca.create_image(150, 200, image=self.photo)


        self.left_frame.pack(side="left", fill=Y)
        self.ca.pack()
        self.right_frame.pack()

        self.control_frame.pack(side="top")
        self.radio_button_1.pack(side="left",padx=5)
        self.radio_button_2.pack(side="right",padx=5)

        self.ent_frame.pack(side="top", pady= 10, fill =BOTH, expand =1)
        self.lbl_in.pack(pady=5)  
        self.ent_in.pack(pady=5)
        self.lbl_out.pack(pady=5)
        self.ent_out.pack(pady=5)
        self.button_1.pack(pady=30)
        self.ent_in.focus_force()


root = Tk()
app = myApp(root)
root.mainloop()

