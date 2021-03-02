#------------------------------------------------------------------------------#
# Kalkulacka                                                                   #
#------------------------------------------------------------------------------#

from tkinter import * 
from math import *
from tkinter import font

class MyApp:

    def insKey(self, sign):
        sign_list = ['+','-','*','^','/','.','%']
        number_list = ['0','1','2','3','4','5','6','7','8','9']
        if self.x == "EOF":
            self.x = ""
        if sign == '=':
            try:
                self.x = eval(f"{self.x}")
                self.x = str(self.x)
            except:
                self.x = "EOF"
        elif sign in sign_list:
            if self.x == "":
                return
            if self.x[-1] in number_list:
                if sign == '^':
                    self.x += "**"
                else:   
                    self.x += sign
        elif sign == 'C':
            self.x = ""
        elif sign == '√':
            try:
                self.x = eval(f"{self.x}**0.5")
                self.x = str(self.x)
            except:
                self.x = "EOF"
        elif sign == '±':
            try:
                self.x = eval(f"{self.x}")
                self.x = str(self.x*-1)
            except:
                self.x = "EOF"
        elif sign == '←':
            self.x = self.x[:-1]
        else:
            self.x += sign
        
        self.la['text'] = f"{self.x}"

        
    def __init__(self, root):
        self.fo = StringVar()
        root.title("Calculator")
        self.font = font.Font(size=10, weight="normal")
        self.x = ""
        self.la = Label(root, text=0, background="#ffffff", anchor=E, relief=SUNKEN, height=2, font=self.font)
        self.la.pack(fill=X, side=TOP, padx=8, pady=15)
        self.numbts = Frame(root)
        self.numbts.pack(fill=BOTH, expand=1, padx=4, pady=4)

        self.btnp_arrow = Button(self.numbts, text="←",width=5, height=2, font=self.font, bg='#d4d2cd',command=lambda: self.insKey("←"))
        self.btnp_arrow.grid(row=1, column=0, sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_c = Button(self.numbts, text="C",width=5, height=2, font=self.font, bg='#d4d2cd',command=lambda: self.insKey("C"))
        self.btnp_c.grid(row=1, column=1,sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_pow = Button(self.numbts, text="^",width=5, height=2, font=self.font, bg='#d4d2cd',command=lambda: self.insKey("^"))
        self.btnp_pow.grid(row=1, column=2,sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_plusminus = Button(self.numbts, text="±",width=5, height=2, font=self.font, bg='#d4d2cd',command=lambda: self.insKey("±"))
        self.btnp_plusminus.grid(row=1, column=3,sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_sqrt= Button(self.numbts, text="√",width=5, height=2, font=self.font, bg='#d4d2cd',command=lambda: self.insKey("√"))
        self.btnp_sqrt.grid(row=1, column=4,sticky=W+E+N+S, padx=2, pady=2)

        self.btnp_seven = Button(self.numbts, text="7",width=5, height=2, font=self.font, command=lambda: self.insKey("7"))
        self.btnp_seven.grid(row=2, column=0, sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_eigth = Button(self.numbts, text="8",width=5, height=2, font=self.font, command=lambda: self.insKey("8"))
        self.btnp_eigth.grid(row=2, column=1,sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_nine = Button(self.numbts, text="9",width=5, height=2, font=self.font, command=lambda: self.insKey("9"))
        self.btnp_nine.grid(row=2, column=2,sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_divide = Button(self.numbts, text="/",width=5, height=2, font=self.font,bg='#d4d2cd', command=lambda: self.insKey("/"))
        self.btnp_divide.grid(row=2, column=3,sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_modulo= Button(self.numbts, text="%",width=5, height=2, font=self.font,bg='#d4d2cd', command=lambda: self.insKey("%"))
        self.btnp_modulo.grid(row=2, column=4,sticky=W+E+N+S, padx=2, pady=2)

        self.btnp_four = Button(self.numbts, text="4",width=5, height=2, font=self.font, command=lambda: self.insKey("4"))
        self.btnp_four.grid(row=3, column=0, sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_five = Button(self.numbts, text="5",width=5, height=2, font=self.font, command=lambda: self.insKey("5"))
        self.btnp_five.grid(row=3, column=1,sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_six = Button(self.numbts, text="6",width=5, height=2, font=self.font, command=lambda: self.insKey("6"))
        self.btnp_six.grid(row=3, column=2,sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_multiple = Button(self.numbts, text="*",width=5, height=2, font=self.font,bg='#d4d2cd', command=lambda: self.insKey("*"))
        self.btnp_multiple.grid(row=3, column=3,sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_fraction= Button(self.numbts, text="1/x",width=5, height=2, font=self.font,bg='#d4d2cd', command=lambda: self.insKey("/"))
        self.btnp_fraction.grid(row=3, column=4,sticky=W+E+N+S, padx=2, pady=2)

        self.btnp_one = Button(self.numbts, text="1",width=5, height=2, font=self.font, command=lambda: self.insKey("1"))
        self.btnp_one.grid(row=4, column=0, sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_two = Button(self.numbts, text="2",width=5, height=2, font=self.font, command=lambda: self.insKey("2"))
        self.btnp_two.grid(row=4, column=1,sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_three = Button(self.numbts, text="3",width=5, height=2, font=self.font, command=lambda: self.insKey("3"))
        self.btnp_three.grid(row=4, column=2,sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_minus = Button(self.numbts, text="-",width=5, height=2, font=self.font,bg='#d4d2cd', command=lambda: self.insKey("-"))
        self.btnp_minus.grid(row=4, column=3,sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_equals= Button(self.numbts, text="=",width=5, height=2, font=self.font,bg='#d4d2cd', command=lambda: self.insKey("="))
        self.btnp_equals.grid(row=4, column=4,rowspan=2,sticky=W+E+N+S, padx=2, pady=2)
        
        self.btnp_zero = Button(self.numbts, text="0",width=5, height=2, font=self.font, command=lambda: self.insKey("0"))
        self.btnp_zero.grid(row=5, column=0, columnspan=2,sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_dot = Button(self.numbts, text=",",width=5, height=2, font=self.font,bg='#d4d2cd', command=lambda: self.insKey("."))
        self.btnp_dot.grid(row=5, column=2, sticky=W+E+N+S, padx=2, pady=2)
        self.btnp_plus = Button(self.numbts, text="+",width=5, height=2, font=self.font,bg='#d4d2cd', command=lambda: self.insKey("+"))
        self.btnp_plus.grid(row=5, column=3,sticky=W+E+N+S, padx=2, pady=2)
        #self.btn.config(state=DISABLED)
        self.numbts.rowconfigure(1,weight=1)
        self.numbts.rowconfigure(2,weight=1)
        self.numbts.rowconfigure(5,weight=1)
        self.numbts.rowconfigure(4,weight=1)
        self.numbts.rowconfigure(3,weight=1)
        self.numbts.columnconfigure(0,weight=1)
        self.numbts.columnconfigure(1,weight=1)
        self.numbts.columnconfigure(2,weight=1)
        self.numbts.columnconfigure(3,weight=1)
        self.numbts.columnconfigure(4,weight=1)

root = Tk()
app = MyApp(root)
root.mainloop()
