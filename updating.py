import tkinter
import tkinter.ttk as ttk
from functions import SQL

class Eingabe:
    def __init__(self):
        self.sql = SQL()
        self.main = tkinter.Tk()
        self.main.geometry('800x600')
        self.main.configure(background = '#0A303E')
        self.main.title("Bearbeiten")

    def update(self):
        fach = self.fachauswahl.get()
        front = self.front.get()
        back = self.back.get()
        addition = self.addition.get()

            # SQL.insert(front, back, addition, fach) 

    def end(self):
        self.main.destroy()

    def start(self):

        #Überschrift
        self.ueberschrift = tkinter.Label(self.main, text = "Bearbeiten:", font = ("Arial", 20, "underline", "bold"), fg='#2cab31', bg='#0A303E')
        self.ueberschrift.place(relx = 0.5, rely = 0.04, anchor = "n")

        #Fachauswahl
        self.fachanzeige = tkinter.Label(self.main, text="Aktuelle Fachauswahl: ", font = ("Arial", 14, "underline"), fg='#9FC', bg='#0A303E' )
        self.fachanzeige.place(relx = 0.5, rely = 0.2, anchor = "n")
        list_of_subjects = self.sql.listofsubjects()
        self.fachauswahl = ttk.Spinbox(self.main,
            values=[subject for subject in list_of_subjects],
            width=15 ) #Dringend Variablen für die Sprache einfügen
        self.fachauswahl.set(list_of_subjects[0])
        self.fachauswahl.place(relx = 0.5, rely = 0.25, anchor = "n")

        # Liste aller möglichen Vokabeln  
        self.list_box = Listbox(self.main)
        vocs = self.sql.get

        #Vokabeleingabe
        self.front_headline = tkinter.Label(self.main, text = "Vorderseite:", font = ("Arial", 14, "underline"),  fg='#9FC', bg='#0A303E')
        self.front_headline.place(relx = 0.3, rely = 0.4, anchor = "n")
        self.front = tkinter.Entry(self.main, bg = '#dae6f1', font = ("Calibri", 13, "bold"))
        self.front.place(relx = 0.3, rely = 0.45, anchor = "n")

        #Übersetzungseingabe
        self.back_headline = tkinter.Label(self.main, text = "Rückseite:", font = ("Arial", 14, "underline"), fg='#9FC', bg='#0A303E')
        self.back_headline.place(relx = 0.7, rely = 0.4, anchor = "n")
        self.back = tkinter.Entry(self.main, bg = '#dae6f1', font = ("Calibri", 13, "bold")) 
        self.back.place(relx = 0.7, rely = 0.45, anchor = "n")

        #Zusatz
        self.addition_headline = tkinter.Label(self.main, text = "Zusätzliche Info:", font = ("Arial", 14, "underline"), fg='#9FC', bg='#0A303E')
        self.addition_headline.place(relx = 0.5, rely = 0.6, anchor = "n" )
        self.addition = tkinter.Entry(self.main, bg = '#dae6f1', font = ("Calibri", 13, "bold"), width = 40)
        self.addition.place(relx = 0.5, rely = 0.65, anchor = "n")

        #Bestätigen
        self.save = tkinter.Button(self.main, text = "Speichern", bg = '#ff0095', font = ("Arial", 11, "bold"), command = self.update)
        self.save.place(relx = 0.1, rely = 0.9, anchor = "n" )
    
        #Zurück
        self.end = tkinter.Button(self.main, text="Beenden", bg = '#ff0095', font = ("Arial", 11, "bold"), command = self.end)
        self.end.place(relx = 0.9, rely = 0.9, anchor = "n")
        self.main.mainloop()



def start_new():
    eingabe = Eingabe() 
    eingabe.start()

if __name__ == '__main__':
    start_new()
