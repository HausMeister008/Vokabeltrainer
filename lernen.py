from tkinter import *
from Vokabelverarbeitung import *

class Lernen:
    def __init__(self):
        self.main = Tk()
        self.headline = Label(self.main, text = 'Vokabeln lernen', font = ('Arial',25, 'bold'), fg = '#fff', bg='#222').pack()

    def end(self):
        self.main.destroy()

    def start(self, fach = 'englisch'):
        self.main.geometry('900x600')
        self.main.configure(background = '#222')
        box_and_pool = get_vocs(fach)
        box = box_and_pool[0]
        pool = box_and_pool[1]
        self.main.mainloop()

if __name__ == '__main__':
    lernen = Lernen()
    lernen.start()