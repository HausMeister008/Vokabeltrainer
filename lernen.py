from tkinter import *

class Lernen:
    def __init__(self):
        self.main = Tk()
        self.headline = Label(self.main, text = 'Vokabeln lernen', font = ('Arial',25, 'bold'), fg = '#fff', bg='#222').pack()

    def end(self):
        self.main.destroy()

    def start(self):
        self.main.geometry('900x600')
        self.main.configure(background = '#222')
        self.main.mainloop()