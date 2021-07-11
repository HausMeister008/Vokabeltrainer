from tkinter import *
from eingabe import *
#from lernen import *
from selection import *

def start_selection():
    select_window = Select()
    # select_window.start() 

def start_add():
    add_window = Eingabe()
    add_window.start()

class Main():
    def __init__(self):
        self.main = Tk()
        self.headline = Label(self.main, text = 'Vokabeltrainer', font = ("Arial", 20, "underline", "bold"), fg='#2cab31', bg='#0A303E' )
        self.headline.place(relx = 0.5, rely = 0.04, anchor = "n")
        self.learn_button = Button(self.main, text = 'Jetzt lernen', font = ("Arial", 14), fg='#9FC', bg='#040747', bd=1, command = start_selection)
        self.learn_button.place(relx = 0.5, rely = 0.15, anchor = "n")
        self.eingabe_button =Button(self.main, text ="Vokabeln hinzufügen", font = ("Arial", 14), fg='#9FC', bg='#040747', bd=1, command = start_add)
        self.eingabe_button.place(relx = 0.5, rely = 0.25, anchor = "n")
        self.beenden = tkinter.Button(self.main, text="Beenden", bg = '#ff0095', font = ("Arial", 11, "bold"), command = self.end)
        self.beenden.place(relx = 0.9, rely = 0.9, anchor = "n")

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