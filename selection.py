from tkinter import *

from lernen import *

def start_learn(fach = 'englisch', front_or_back_first = 'f'):
    select_window = Lernen()
    select_window.start(fach, front_or_back_first) # hat noch parameter: fach, front_or_back_first

class Select:

    def __init__(self):
        self.list_of_motivations = [
            'Es ist egal, wie langsam du vorankommst. Du überrundest noch immer jeden auf dem Sofa',
            'Gestern hast du morgen gesagt!', 
            'Es gibt kein "Ich kann das nicht". Höchstens ein "Ich kann das noch nicht"!',
            'Man ist nicht stark oder schwach. Nur trainiert oder untrainiert.', 
            'Erzähle den Leuten nicht von deinen Träumen. Zeige sie ihnen!',
            'Jeder Mensch macht Fehler. Das Kunststück liegt darin, sie dann zu machen, wenn keiner zuschaut.',
            'Wenn du die Person suchst, die dein Leben verändert: Schau in den Spiegel!', 
            'Tue es JETZT... Denn "irgendwann später" wird zu NIEMALS.',
            'Warte nicht darauf, dass die Dinge einfacher werden. Werde du besser!', 
            'Schaue nur zurück, um zu sehen, wie weit du gekommen bist',
            'Es ist nicht zu wenig Zeit, die wir haben, es ist zu viel Zeit, die wir nicht nutzen.',
            'Du musst bereit sein, die Dinge zu tun, die andere niemals tun werden, um die Dinge zu haben, die andere niemals haben werden.',
            'Das ganze Leben ist ein ewiges Wiederanfangen',
            'Es ist nicht genug zu wissen - Man muss auch anwenden. Es ist nicht genug zu wollen - man muss auch tun.',
            'Du bist besser, als du weißt. Und alle Hater fürchten sich vor dem Tag, an dem du das erkennst.',
            'Mehr als die Vergangenheit interessiert mich die Zukunft. Denn in ihr gedenke ich zu leben!',
            'Fokussiere dich darauf, effektiv zu sein, nicht beschäftigt.',
            'Das kalte Wasser wird nicht wärmer, wenn du später springst.'
            ]
        self.main = Tk()
        self.main.geometry('800x600')
        self.main.configure(background = '#0A303E')
        self.main.title("Auswahl")
        self.prozentwert = IntVar()
        self.prozentwert.set(0)
        self.spruch = Label(self.main, text = random.choice(self.list_of_motivations), font = ("Arial", 11, "bold"), wraplength=750,fg='#2cab31', bg='#0A303E')
        self.spruch.place(relx= 0.5, rely=0.9, anchor = "n")
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
    

