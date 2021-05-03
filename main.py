from tkinter import *
from eingabe import *
from lernen import *

def start_learn():
    learn_window = Lernen()
    learn_window.start()

def start_add():
    add_window = Eingabe()
    add_window.start()

class Main():
    def __init__(self):
        self.main = Tk()
        self.headline = Label(self.main, text = 'Vokabeltrainer', font = ('Arial',25, 'bold'), fg = '#fff', bg='#222').pack()
        self.learn_button = Button(self.main, text = 'jetzt lernen', font=('Arial', 15), fg = '#fff', bg='#222', bd=1, command = start_learn).pack(pady=10)
        Button(self.main, text ="neue Vokabeln hinzufügen",font=('Arial', 15), fg = '#fff', bg='#222', bd=1, command = start_add).pack(pady=10)

    def end(self):
        self.main.destroy()

    def start(self):
        self.main.geometry('900x600')
        self.main.configure(background = '#222')
        self.main.mainloop()


if __name__ == '__main__':
    window = Main()
    window.start()