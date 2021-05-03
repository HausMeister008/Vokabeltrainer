from functions import *

db = SQL()

endlevel = 6

# Alle Zeilen in einer Liste: Jeder Eintrag ein dictionary; keys: id, front, back, add, lvl
voc_pool = db.get()
box = {}


for i in range(endlevel):
    box[i] = {}

#print(box)

for vok in voc_pool:
    print(vok)

for index, vokabel in enumerate(voc_pool):
    # 1. Runde -> {id: 1, front: 'hello world'...}
    # Hier werden alle Vokabeln ihrem Level zugeordnet -> Wir nehmen die Karte und gucken uns das Level an
    # --> Dann löschen wir die Karte bei einem niedrigeren Level als das endlevel aus dem pool und fügen sie in die box 
    # an der entsprechenden Stelle ein
    # 1) box and stelle vom aktuellen vokabellevel -> dict ->
    vokabel_level = vokabel['lvl'] # bei lvl-von-vokabel = 1 -> vokabel_level = 1
    vokabel_id = vokabel['id']
    if vokabel_level < 6:
        box[vokabel['lvl']][vokabel['id']] = vokabel #öffnet Box, öffnet Level - setzt id auf entsprechende Vokabel
        voc_pool.pop(index)
for lvl, content in box.items():
    print('lvl '+str(lvl) + ': ')
    for id_, voc in content.items():
        print('    - '+str(id_) + ':', str(voc))

print(voc_pool)