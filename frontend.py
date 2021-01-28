from tkinter import *
from backend_2 import Connection
database=Connection()


class Interface(object):

    def __init__(self,window):
        self.window=window
        self.window.wm_title("Dictionary")
    
        l1=Label(window,text="Enter your word here: ")
        l1.grid(row=0,column=0)

        self.word_text=StringVar()
        self.e1=Entry(window,textvariable=self.word_text)
        self.e1.grid(row=0,column=1)

        b1=Button(window,text="Search",width=10,command=self.search_command)
        b1.grid(row=0,column=2)

        b2=Button(window,text="Close",width=10,command=window.destroy)
        b2.grid(row=5,column=2)

        b3= Button(window,text="Yes",width=5,command=self.choice_y)
        b3.grid(row=1,column=2)

        b4=Button(window,text="No",width=5,command=self.choice_n)
        b4.grid(row=1,column=3)
        
        sc_1=Scrollbar(window,orient=HORIZONTAL)
        sc_1.grid(row=10,column=0,columnspan=2)
        
        sc_2=Scrollbar(window,orient=HORIZONTAL)
        sc_2.grid(row=3,column=0,columnspan=2)

        self.list1=Listbox(window,height=6,width=35)
        self.list1.grid(row=4,column=0,rowspan=6,columnspan=2)

        self.list2=Listbox(window,height=2,width=35)
        self.list2.grid(row=1,column=0,rowspan=2,columnspan=2)
        
        self.list1.configure(xscrollcommand=sc_1.set)
        sc_1.configure(command=self.list1.xview)

        self.list2.configure(xscrollcommand=sc_2.set)
        sc_2.configure(command=self.list2.xview)

    def translate_results(self):
        self.list1.delete(0,END)
        for row in database.translate(self.word_text.get()):
            self.list1.insert(END,row[0])
    
    def translate_error(self):
        self.list2.delete(0,END)
        self.list1.delete(0,END)
        self.list2.insert(END,database.translate_error(self.word_text.get()))

    def search_command(self):
        if database.checking(self.word_text.get())== True:
            self.translate_results()
        else:
            self.translate_error()
        
    def choice_y(self):
        try:
            self.list2.delete(0,END)
            self.list1.delete(0,END)
            for row in database.choices_y(self.word_text.get()):
                self.list1.insert(END,row[0])
        except IndexError:
            pass

    def choice_n(self):
        try:
            self.list2.delete(0,END)
            self.list1.delete(0,END)
            self.list1.insert(END,"The word does not exist.Please try again.")
        except IndexError:
            pass
window=Tk()
Interface(window)       
window.mainloop()