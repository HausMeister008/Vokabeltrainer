import tkinter
from functions import SQL


class Eingabe:
    def __init__(self):
        self.main = tkinter.Tk()
        #Textfelder/Knöpfe/Label
            
        #Definitionen für die Knöpfe

    def write(self):
        front = self.e0.get()
        back = self.e1.get()
        addition = self.e2.get()
        if (front.strip() == "") or (back.strip() == ""):
            self.l0["text"] = "Bitte gib eine Vokabel ein:"
            self.l1["text"] = "Bitte gib die Übersetzung ein:"
        else:
            print(front, back, addition)
            # SQL.insert(front, back, addition)

    def ende(self):
        self.main.destroy()

    def start(self):
        self.l0 = tkinter.Label(self.main, text = "Bitte die Vokabel eingeben:")
        self.l0.pack()
        self.e0 = tkinter.Entry(self.main)
        self.e0.pack()

        self.l1 = tkinter.Label(self.main, text = "Bitte die Übersetzung eingeben:")
        self.l1.pack()
        self.e1 = tkinter.Entry(self.main)
        self.e1.pack()

        self.l2 = tkinter.Label(self.main, text = "Hier kannst du einen möglichen Zusatz eingeben:")
        self.l2.pack()
        self.e2 = tkinter.Entry(self.main)
        self.e2.pack()

        self.b0 = tkinter.Button(self.main, text = "Bestätigen", command = self.write)
        self.b0.pack()

        self.b1 = tkinter.Button(self.main, text="Ende", command = self.ende)
        self.b1.pack()

        self.b2 = tkinter.Button(self.main, text = 'NEW WINDOW', command = start_new)
        self.b2.pack()
        self.main.mainloop()
        

def start_new():
    eingabe = Eingabe() 
    eingabe.start()
start_new()