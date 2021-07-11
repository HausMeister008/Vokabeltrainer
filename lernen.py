from tkinter import *
from Vokabelverarbeitung import *
import random
import math
import time


class Lernen:

    #Einführung der ganzen Labels usw: 
    def __init__(self):
        
        self.list_of_voc_ids = []
        self.front_back_list = ['front', 'back']
        self.current_voc_id = 0
        self.all_vocs_dict = {}
        self.main = Tk()
        self.anzeige_vokabel = Label(self.main,  text = 'Vokabel:', font = ("Arial", 14, "underline"),  fg='#9FC', bg='#0A303E') #Denk dir meinetwegen noch nen anständigen Namen aus
        self.anzeige_vokabel.place(relx = 0.5, rely = 0.15, anchor= "n")
        self.anzeige_front = Label(self.main, font = ("Arial", 14),  fg='#9FC', bg='#0A303E')
        self.anzeige_front.place(relx = 0.5, rely = 0.2, anchor= "n")
        self.enter_solution = Label(self.main,  text = 'Übersetzung:', font = ("Arial", 14),  fg='#9FC', bg='#0A303E')
        self.enter_solution.place(relx = 0.5, rely = 0.3, anchor= "n")
        self.solution = Entry(self.main, bg = '#dae6f1', font = ("Calibri", 13, "bold"))
        self.solution.place(relx = 0.5, rely = 0.35, anchor= "n")
        self.wrong_or_right = Label(self.main, font = ("Arial", 14),  fg='#9FC', bg='#0A303E')
        self.wrong_or_right.place(relx = 0.5, rely = 0.45, anchor= "n")
        self.anzeige_zusatz = Label(self.main, font = ("Arial", 14),  fg='#9FC', bg='#0A303E' )
        self.anzeige_zusatz.place(relx = 0.5, rely = 0.55, anchor = "n")
        self.addition = Label(self.main, font = ("Arial", 14),  fg='#9FC', bg='#0A303E', wraplength=700)
        self.addition.place(relx = 0.5, rely = 0.6, anchor= "n")
        
        #Zurück
        self.back = Button(self.main, text="Beenden", bg = '#ff0095', font = ("Arial", 11, "bold"), command = self.end)
        self.back.place(relx = 0.9, rely = 0.9, anchor = "n")
        #Button um die nächste Vokabel zu laden, nur mal für die Zukunft
        self.next = Button(self.main, text = "Auswerten", bg = '#ff0095', font = ("Arial", 11, "bold"),  command = self.auswerten)
        self.next.place(relx = 0.1, rely = 0.9, anchor = "n")

    #Not aus:
    def end(self):
        self.main.destroy()

    def weiter(self, e = ''):
        self.solution.delete(0, END)
        self.addition["text"] = ""
        self.start_process(self.all_vocs_dict)
        self.wrong_or_right['text'] = ''
        self.anzeige_zusatz['text'] = ''
        self.next['text'] = 'Auswerten'
        self.next['command'] = self.auswerten

    #Auswertung, öb die Übersetzung richtig oder falsch ist:
    def auswerten(self, e = ''):
        voc_id = self.current_voc_id
        voc = self.all_vocs_dict[voc_id]
        solution = self.solution.get().strip() # Eingabe der Lösung
        if solution == voc[self.front_back_list[1]]: # Wenn die Lösung stimmt
            self.wrong_or_right['text'] = 'Richtig!' 
        else: # Sonst ist es falsch und die richtige Lösung wird vorgegeben
            self.wrong_or_right["text"] = 'Falsch: ' + voc[self.front_back_list[1]]
        if voc['add'] != '': # Wenn es noch eine Addition gibt, add also nicht leer ist
                self.anzeige_zusatz["text"] = "Zusatz:"
                self.addition["text"] = voc['add'] # Auch als Label
        if voc_id in [k['id'] for k in voc_pool]: # wenn die momentane vokabel sich im pool befindet, die ID also in den ID der pool-vokabeln ist
            for i, v in enumerate(pool): # aus dem pool die entsprechende vokabel löschen
                if v['id'] == voc_id:
                    pool.pop(i)
        self.next['text'] = 'Nächste Vokabel'
        self.next['command'] = self.weiter
        self.solution.bind('<Return>', self.weiter)
                    
    #Definitiv nochmal Erklärungsbedarf....
    def start_process(self, all_vocs_dict):
        # print(self.list_of_voc_ids)
        # for voc_id in self.list_of_voc_ids:
        #     current_variable = all_vocs_dict[voc_id]
        #     print(current_variable[self.front_back_list[0]])
        if len(self.list_of_voc_ids)> 0:
            self.current_voc_id = self.list_of_voc_ids[0]
            self.anzeige_front['text'] = all_vocs_dict[self.list_of_voc_ids[0]][self.front_back_list[0]]
            print(self.anzeige_front['text'])
            self.solution.bind('<Return>', self.auswerten)
            del self.list_of_voc_ids[0]
        else: #Warum ist hier ein Else?
            self.end()

    #Configuriert das Hauptfenster, "sammelt" die Vokabeln
    def start(self, fach = 'englisch', front_or_back_first = 'f', pool_percent = 0.5):
        self.main.geometry('800x600')
        self.main.configure(background = '#0A303E')
        self.main.title("Vokabeln lernen")
        self.front_back_list = ['front', 'back']
        if front_or_back_first.lower() in ['back', 'b']:
            self.front_back_list = ['back', 'front']
    
        box_and_pool = get_vocs(fach) # get_vocs gibt eine liste zurück
        box:dict = box_and_pool[0]
        pool:list = box_and_pool[1]
        pool_dict:dict = {i['lvl']:{i['id']:i} for i in pool}
        all_vocs = [content for drawer, content in {**box, **pool_dict}.items()]
        # all_vocs = {j,k for i.items() in all_vocs}
        self.all_vocs_dict:dict = {}
        for i in all_vocs:
            for j, k in i.items():
                self.all_vocs_dict[j] = k
        # print(all_vocs_dict)

        to_learn_drawers_nr = 0 # in wie vielen der Fächer der Box sind Vokabeln
        for lvl, vocs in box.items(): # Herausfinden, wie viele Fächer was entahlten
            if len(vocs) > 0:
                to_learn_drawers_nr += 1
        if to_learn_drawers_nr !=0:
            # Der Prozentsatz an bereits gemeisterten Vokabeln
            pool_percent = pool_percent / to_learn_drawers_nr # Den Prozentsatz noch auf die ganzen Fächer verteilen -> So hat jedes Fach seinen Anteil an den pool-vocs
        
        if (float(pool_percent) % 1)>=0.5 or pool_percent < 0.5:
            l:int = int(math.ceil(len(pool)*pool_percent)) # Gerundet auf 0 Nachkommastellen die Pool-Länge * dem Prozentsatz (geteil wie oben) -> Länge, die aus dem geshuffelten pool entnommen wird
        else:
            l:int = int(round(len(pool)*pool_percent, 0)) # Gerundet auf 0 Nachkommastellen die Pool-Länge * dem Prozentsatz (geteil wie oben) -> Länge, die aus dem geshuffelten pool entnommen wird
        

        for lvl, vocs in box.items(): # die box (noch ohne pool vocs drinnen durchloopen)
            if len(vocs) > 0: # Wenn in dem Fach mind 1 Vokabel drinnen ist
                
                random.shuffle(pool) # Pool (Liste) einmal durchmischeln
                if l > 0: # wenn diese länge höher 0 ist, dann nehme man diese anzahl aus dem pool
                    pool_list = pool[0:l] 
                else: # wenn nicht (gerundet )
                    if len(pool) == 1: # wenn eine vokabel im pool ist
                        pool_list = list(pool) # dann wird einfach der pool als liste genommen
                    else:
                        pool_list = [] # sonst ist der pool leer

                for v in pool_list: # pool in vokablelliste einfügen in gleichem schema -> bisher liste jetzt muss es ins dictionary
                    vocs[v['id']] = v
                    
                # jetzt soll das dict vocs durchgemischt werden
                keys  = list(vocs.keys()) # liste der keys in vocs
                random.shuffle(keys) # diese liste einmal durchmischen
                vocs = {k:vocs[k] for k in keys} # und wieder zurück zum dictionary

                for voc_id, voc in vocs.items(): # für jede id und die dieser zugeordneten vokabel
                    self.list_of_voc_ids.append(voc_id) # der liste die id anhängen, damit man später auf alle in der runde vorkommenden 
                del pool[0:l]
        
        self.anzeige_front['text'] = self.all_vocs_dict[self.list_of_voc_ids[0]][self.front_back_list[0]] # hier noch geprintet... später dann als label
        self.solution.delete(0, END)

        # Als nächstes müssen wir die Liste aus IDS verwerten -> erste laden und alle anderen danach
        self.start_process(self.all_vocs_dict)
        self.main.mainloop()


#Irgendwas mit Programm beim richtigen Namen starten?
if __name__ == '__main__':
    lernen = Lernen()
    lernen.start(front_or_back_first='b')