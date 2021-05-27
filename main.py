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
        self.headline = Label(self.main, text = 'Vokabeltrainer', font = ("Arial", 20, "underline", "bold"), fg='#2cab31', bg='#0A303E' )
        self.headline.place(relx = 0.5, rely = 0.04, anchor = "n")
        self.learn_button = Button(self.main, text = 'jetzt lernen', font = ("Arial", 14, "underline"), fg='#9FC', bg='#040747', bd=1, command = start_learn)
        self.learn_button.place(relx = 0.5, rely = 0.15, anchor = "n")
        self.eingabe_button =Button(self.main, text ="neue Vokabeln hinzufügen", font = ("Arial", 14, "underline"), fg='#9FC', bg='#040747', bd=1, command = start_add)
        self.eingabe_button.place(relx = 0.5, rely = 0.25, anchor = "n")

    def end(self):
        self.main.destroy()

    def start(self):
        self.main.geometry('800x600')
        self.main.configure(background = '#0A303E')
        self.main.title("Hauptmenü")
        self.main.mainloop()


if __name__ == '__main__':
    window = Main()
    window.start()


