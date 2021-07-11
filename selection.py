from tkinter import *

from lernen import *

def start_learn(fach = 'englisch', front_or_back_first = 'f'):
    select_window = Lernen()
    select_window.start(fach, front_or_back_first) # hat noch parameter: fach, front_or_back_first

class Select:

    def __init__(self):
        self.main = Tk()
        self.main.geometry('800x600')
        self.main.configure(background = '#0A303E')
        self.main.title("Auswahl")
        self.prozentwert = IntVar()
        self.prozentwert.set(0)
        self.headline = Label(self.main, text = 'Auswahl', font = ("Arial", 20, "underline", "bold"), fg='#2cab31', bg='#0A303E' )
        self.headline.place(relx = 0.5, rely = 0.04, anchor = "n")
        self.beenden = Button(self.main, text="Beenden", bg = '#ff0095', font = ("Arial", 11, "bold"), command = self.end)
        self.beenden.place(relx = 0.1, rely = 0.9, anchor = "n")
        self.jetzt_lernen = Button(self.main, text="jetzt lernen", bg = '#ff0095', font = ("Arial", 11, "bold"), command = start_learn)
        self.jetzt_lernen.place(relx = 0.9, rely = 0.9, anchor = "n")
        self.anzeige_prozentwert = Label(self.main, text = 'Gibt hier den Anteil Vokabel (im Verhältnis zu den zu lernenen), die aus dem Pool gezogen werden an.'
                        )
        self.prozentwert = Scale(self.main, width=20, length=200, orient="vertical", from_=0,to=100,
                           resolution=10, tickinterval = 10, label="Prozentsatz", variable = self.prozentwert, bg = '#0A303E', borderwidth = 0 )
        self.prozentwert.place(relx = 0.5, rely = 0.5, anchor = "n")


    def end(self):      
        self.main.destroy()
    

