import tkinter
import tkinter.ttk as ttk
from functions import SQL


class Eingabe:
    def __init__(self):
        self.main = tkinter.Tk()
        self.main.geometry('900x600')
        self.main.configure(background = '#0A303E')

    def write(self):
        fach = self.fachanzeige.get()
        front = self.e0.get()
        back = self.e1.get()
        addition = self.e2.get()
        if (front.strip() == "") or (back.strip() == ""):
            self.l0["text"] = "Bitte gib eine Vokabel ein:"
            self.l1["text"] = "Bitte gib die Übersetzung ein:"
        else:
            print(front, back, addition, fach)
            # SQL.insert(front, back, addition)

    def ende(self):
        self.main.destroy()

    def start(self):

        #Überschrift
        self.ueberschrift = tkinter.Label(self.main, text = "neue Vokabelkarte anlegen: ")
        self.ueberschrift.place(relx = 0.5, rely = 0.04, anchor = "n")

        #Fachauswahl
        self.fachanzeige = tkinter.Label(self.main, text="Aktuelle Fachauswahl: ")
        self.fachanzeige.place(relx = 0.5, rely = 0.1, anchor = "n")
        self.fachauswahl = ttk.Spinbox(self.main,
            values=("englisch", "französisch", "latein", "spanisch"),
            width=15, command= self.write) #Dringend Variablen für die Sprache einfügen
        self.fachauswahl.set("englisch")
        self.fachauswahl.place(relx = 0.5, rely = 0.15, anchor = "n")

        #Vokabeleingabe
        self.l0 = tkinter.Label(self.main, text = "Bitte die Vokabel eingeben:")
        self.l0.place(relx = 0.3, rely = 0.4, anchor = "n")
        self.e0 = tkinter.Entry(self.main)
        self.e0.place(relx = 0.3, rely = 0.45, anchor = "n")

        #Übersetzungseingabe
        self.l1 = tkinter.Label(self.main, text = "Bitte die Übersetzung eingeben:")
        self.l1.place(relx = 0.7, rely = 0.4, anchor = "n")
        self.e1 = tkinter.Entry(self.main) 
        self.e1.place(relx = 0.7, rely = 0.45, anchor = "n")

        #Zusatz
        self.l2 = tkinter.Label(self.main, text = "Hier kannst du einen möglichen Zusatz eingeben:")
        self.l2.place(relx = 0.5, rely = 0.6, anchor = "n" )
        self.e2 = tkinter.Entry(self.main)
        self.e2.place(relx = 0.5, rely = 0.65, anchor = "n")

        #Bestätigen
        self.b0 = tkinter.Button(self.main, text = "Speichern", command = self.write)
        self.b0.place(relx = 0.1, rely = 0.95, anchor = "n"  )
    
        #Zurück
        self.b1 = tkinter.Button(self.main, text="Zurück", command = self.ende)
        self.b1.place(relx = 0.9, rely = 0.95, anchor = "n")



def start_new():
    eingabe = Eingabe() 
    eingabe.start()

if __name__ == '__main__':
    start_new()
