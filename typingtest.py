from tkinter import *   
import json, time, random

root = Tk() #main widget. ist das window
root.title("Speed Typing Test") #window name
root.iconphoto(False, PhotoImage(file="imgs/lock_favicon.png")) # set window icon
typed = ""
start = 0
fehler = 0 #Falsche Wörter
score = 0  #Richtige Wörter
ges = 0    #gesamtanzahl Wörter
bg = "#333" # Hintergrundfarben
fg = "#0ff" # Textfarben

content = json.load(open("bib.json", encoding="utf-8"))
random.shuffle(content)
frame = LabelFrame(root, height=580, width=880, padx=20, pady=30, bg ="#222")
frame.pack(padx=10, pady=10)

text = Text(frame, height=1)
text.insert(INSERT, "".join(wort + " " for wort in content))
text.configure(bg=bg, fg=fg, font=("Arial",25))
text.pack(pady=20)


input_field = Entry(frame, bg=bg, fg=fg, width=840, font=("Arial", 25))
input_field.pack(pady=(0,20))

text2 = Label(frame, bg=bg, fg=fg, width=10, text="", font=("Arial", 25), anchor="w")
text2.pack(pady=(0,20))

def strt(event=None):
    global start, score, content
    score = 0
    input_field.focus()
    start = time.time()
    content = json.load(open("bib.json", encoding="utf-8"))
    random.shuffle(content)
    text.delete("1.0", "end")
    text.insert(INSERT,"".join(wort + " " for wort in content))


b = Button(frame, text="START", command=strt, bg=bg, fg=fg, font= 25)
b.pack()

def check_spelling(event):
    global content
    if event.char.isalpha():
        word = (input_field.get().strip() + event.char).strip()
        len_word = len(word)
        current_word = content[0]
        if word != current_word[0:len_word]:
            text.tag_add("start", "1.0", "1."+str(len(content[0])))
            text.tag_config("start", foreground="#f00")
        else:
            text.tag_add("start", "1.0", "1."+str(len(content[0])))
            text.tag_config("start", foreground="#0f9")

        


def auswerten(event):
    global content, start, score, fehler, ges
    i = input_field.get().strip()
    end = time.time()
    ges += 1
    if i != "":
        if i == content[0]:
            text2["text"] = "super"
            score +=1
        else:
            text2["text"] = "schlecht"
            fehler += 1
        input_field.delete(0, END)
        content = content[1:]
        text.delete("1.0", "end")
        text.insert(INSERT, "".join(wort + " " for wort in content))
        text.tag_add("start", "1.0", "1."+str(len(content[0])))
        text.tag_config("start", foreground=fg)
        if (end-start) >= 60.0:
            accuracy = score / ges 
            text.delete("1.0", "end")
            text.insert(INSERT, f"ENDE - WPM: {score} -- Falsche Wörter: {fehler} -- Accuracy: {accuracy*100}%")

input_field.bind("<space>", auswerten) #bei Enter-click wird jetzt der Inhalt des entry ausgewertet

input_field.bind("<Key>", check_spelling)
root.bind("<F5>", strt)

root.geometry("1200x600")
root.configure(bg="#111")
root.mainloop() #laufen lassen