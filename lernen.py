from tkinter import *
from Vokabelverarbeitung import *
import random

import time

class Lernen:
    def __init__(self):
        self.list_of_voc_ids = []
        self.main = Tk()
        self.headline = Label(self.main, text = 'Vokabeln lernen', font = ('Arial',25, 'bold'), fg = '#fff', bg='#222').pack()
        self.anzeige_front = Label(self.main, bg='#222', fg='#0ff')
        self.anzeige_front.pack()
        self.enter_solution = Label(self.main,  text = 'Lösung:', bg='#222', fg='#0ff')
        self.enter_solution.pack()
        self.solution = Entry(self.main, bg='#222', fg='#0ff')
        self.solution.pack()
        self.addition = Label(self.main, bg='#222', fg='#0ff')
        self.addition.pack()
        self.wrong_or_right = Label(self.main, bg='#222', fg='#0ff')
        self.wrong_or_right.pack()

    def end(self):
        self.main.destroy()

    def auswerten(self, front_back_list, voc_id):
        solution = self.solution.get().strip() # Eingabe der Lösung
        if solution == voc[front_back_list[1]]: # Wenn die Lösung stimmt
            if voc['add'] != '': # Wenn es noch eine Addition gibt, add also nicht leer ist
                self.addition["text"] = voc['add'] # Auch als Label
            self.wrong_or_right['text'] = 'CORRECT!' 
        else: # Sonst ist es falsch und die richtige Lösung wird vorgegeben
            self.wrong_or_right['text'] = 'WRONG -', voc[front_back_list[1]]
        if voc_id in [k['id'] for k in voc_pool]: # wenn die momentane vokabel sich im pool befindet, die ID also in den ID der pool-vokabeln ist
            for i, v in enumerate(pool): # aus dem pool die entsprechende vokabel löschen
                if v['id'] == voc_id:
                    pool.pop(i)
                    

    def start(self, fach = 'englisch', front_or_back_first = 'f'):
        self.main.geometry('900x600')
        self.main.configure(background = '#222')
        if front_or_back_first.lower() == 'b':
            front_back_list = ['back', 'front']
        else:
            front_back_list = ['front', 'back']
    
        box_and_pool = get_vocs(fach) # get_vocs gibt eine liste zurück
        box:dict = box_and_pool[0]
        pool:dict = box_and_pool[1]
        pool_percent = 0.5 # Der Prozentsatz an bereits gemeisterten Vokabeln (wird irgendwann mit Schieberegler übergeben)
        to_learn_drawers_nr = 0 # in wie vielen der Fächer der Box sind Vokabeln
        for lvl, vocs in box.items(): # Herausfinden, wie viele Fächer was entahlten
            if len(vocs) > 0:
                to_learn_drawers_nr += 1
        if to_learn_drawers_nr !=0:
            pool_percent = pool_percent / to_learn_drawers_nr # Den Prozentsatz noch auf die ganzen Fächer verteilen -> So hat jedes Fach seinen Anteil an den pool-vocs
        


        for lvl, vocs in box.items(): # die box (noch ohne pool vocs drinnen durchloopen)
            if len(vocs) > 0: # Wenn in dem Fach mind 1 Vokabel drinnen ist
                
                random.shuffle(pool) # Pool (Liste) einmal durchmischeln
                l:int = int(round(len(pool)*pool_percent, 0)) # Gerundet auf 0 Nachkommastellen die Pool-Länge * dem Prozentsatz (geteil wie oben) -> Länge, die aus dem geshuffelten pool entnommen wird
                
                if l > 0: # wenn diese länge höher 0 ist, dann nehme man diese anzahl aus dem pool
                    pool = pool[0:l] 
                else: # wenn nicht (gerundet )
                    if len(pool) == 1: # wenn eine vokabel im pool ist
                        pool = list(pool) # dann wird einfach der pool als liste genommen
                    else:
                        pool = {} # sonst ist der pool leer
                
                for v in pool: # pool in vokablelliste einfügen in gleichem schema -> bisher liste jetzt muss es ins dictionary
                    vocs[v['id']] = v    
                    
                for voc_id, voc in vocs.items(): # für jede id und die dieser zugeordneten vokabel
                    self.list_of_voc_ids.append((voc_id, voc['lvl']))
                # self.anzeige_front['text'] = voc[front_back_list[0]] # hier noch geprintet... später dann als label
                # self.solution.delete(0, END)

                
                # # jetzt soll das dict vocs durchgemischt werden
                # keys  = list(vocs.keys()) # liste der keys in vocs
                # random.shuffle(keys) # diese liste einmal durchmischen
                # vocs = {k:vocs[k] for k in keys} # und wieder zurück zum dictionary

        print(self.list_of_voc_ids)
        # self.main.mainloop()

if __name__ == '__main__':
    lernen = Lernen()
    lernen.start(front_or_back_first='b')