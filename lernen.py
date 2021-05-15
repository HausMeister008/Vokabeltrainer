from tkinter import *
from Vokabelverarbeitung import *
import random

class Lernen:
    def __init__(self):
        # self.main = Tk()
        # self.headline = Label(self.main, text = 'Vokabeln lernen', font = ('Arial',25, 'bold'), fg = '#fff', bg='#222').pack()
        pass

    def end(self):
        # self.main.destroy()
        pass

    def start(self, fach = 'englisch'):
        # self.main.geometry('900x600')
        # self.main.configure(background = '#222')

        box_and_pool = get_vocs(fach) 
        box:dict = box_and_pool[0]
        pool:dict = box_and_pool[1]
        pool_percent = 0.5 # Der Prozentsatz an bereits gemeisterten Vokabeln (wird irgendwann mit Schieberegler übergeben)
        to_learn_drawers_nr = 0 # in wie vielen der Fächer der Box sind Vokabeln
        for lvl, vocs in box.items(): # Herausfinden, wie viele Fächer was entahlten
            if len(vocs) > 0:
                to_learn_drawers_nr += 1
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
                        pool = {}
                for v in pool:
                    vocs[v['id']] = v
                keys  = list(vocs.keys())
                random.shuffle(keys)
                vocs = {k:vocs[k] for k in keys}
                for voc_id, voc in vocs.items():
                    print('\n', voc['front'])
                    solution = input('>..>').strip()
                    if solution == voc['back']:
                        if voc['add'] != '':
                            print(voc['add'])
                    else:
                        print('WRONG -', voc['back'])
                    if voc_id in [k['id'] for k in voc_pool]:
                        for i, v in enumerate(pool):
                            if v['id'] == voc_id:
                                pool.pop(i)

        # self.main.mainloop()

if __name__ == '__main__':
    lernen = Lernen()
    lernen.start()