import tkinter
import tkinter.ttk as ttk
from functions import SQL


class Eingabe:
    def __init__(self):
        self.main = tkinter.Tk()
        self.main.geometry('800x600')
        self.main.configure(background = '#0A303E')
        self.main.title("neue Vokabel hinzufügen")

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
            # SQL.insert(front, back, addition, fach) 

    def end(self):
        self.main.destroy()

    def start(self):

        #Überschrift
        self.ueberschrift = tkinter.Label(self.main, text = "Neue Vokabelkarte anlegen:", font = ("Arial", 20, "underline", "bold"), fg='#2cab31', bg='#0A303E')
        self.ueberschrift.place(relx = 0.5, rely = 0.04, anchor = "n")

        #Fachauswahl
        self.fachanzeige = tkinter.Label(self.main, text="Aktuelle Fachauswahl: ", font = ("Arial", 14, "underline"), fg='#9FC', bg='#0A303E' )
        self.fachanzeige.place(relx = 0.5, rely = 0.2, anchor = "n")
        self.fachauswahl = ttk.Spinbox(self.main,
            values=("englisch", "französisch", "latein", "spanisch"),
            width=15 ) #Dringend Variablen für die Sprache einfügen
        self.fachauswahl.set("englisch")
        self.fachauswahl.place(relx = 0.5, rely = 0.25, anchor = "n")

        #Vokabeleingabe
        self.l0 = tkinter.Label(self.main, text = "Bitte die Vokabel eingeben:", font = ("Arial", 14, "underline"),  fg='#9FC', bg='#0A303E')
        self.l0.place(relx = 0.3, rely = 0.4, anchor = "n")
        self.e0 = tkinter.Entry(self.main, bg = '#dae6f1', font = ("Calibri", 13, "bold"))
        self.e0.place(relx = 0.3, rely = 0.45, anchor = "n")

        #Übersetzungseingabe
        self.l1 = tkinter.Label(self.main, text = "Bitte die Übersetzung eingeben:", font = ("Arial", 14, "underline"), fg='#9FC', bg='#0A303E')
        self.l1.place(relx = 0.7, rely = 0.4, anchor = "n")
        self.e1 = tkinter.Entry(self.main, bg = '#dae6f1', font = ("Calibri", 13, "bold")) 
        self.e1.place(relx = 0.7, rely = 0.45, anchor = "n")

        #Zusatz
        self.l2 = tkinter.Label(self.main, text = "Hier kannst du einen möglichen Zusatz eingeben:", font = ("Arial", 14, "underline"), fg='#9FC', bg='#0A303E')
        self.l2.place(relx = 0.5, rely = 0.6, anchor = "n" )
        self.e2 = tkinter.Entry(self.main, bg = '#dae6f1', font = ("Calibri", 13, "bold"), width = 40)
        self.e2.place(relx = 0.5, rely = 0.65, anchor = "n")

        #Bestätigen
        self.b0 = tkinter.Button(self.main, text = "Speichern", bg = '#ff0095', font = ("Arial", 11, "bold"), command = self.write)
        self.b0.place(relx = 0.1, rely = 0.9, anchor = "n" )
    
        #Zurück
        self.b1 = tkinter.Button(self.main, text="Zurück", bg = '#ff0095', font = ("Arial", 11, "bold"), command = self.end)
        self.b1.place(relx = 0.9, rely = 0.9, anchor = "n")



def start_new():
    eingabe = Eingabe() 
    eingabe.start()

if __name__ == '__main__':
    start_new()
