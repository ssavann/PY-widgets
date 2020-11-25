'''
Tkinter : Créer des interfaces graphiques
Les widgets: Faire un place() -> pour placer les widgets


'''

import tkinter
from tkinter.font import Font

police = ("Saab", 20, "bold")

#fonctions
def agrandir():
    police = ("Rasa", 50, "bold")
    label.config(font = police)


#interface graphique
fenetre = tkinter.Tk() 
#forcer la dimension à 800x600
fenetre.geometry("800x600")    

#widget
label = tkinter.Label(fenetre, text = "Tkinter c'est fantastique...")

label.pack()


btn = tkinter.Button(fenetre, text = "agrandir", command = agrandir)
btn.pack()

#lister les polices natives
police = tkinter.font.families()
for item in police:
    print(item)     #va afficher tous les polices natives de linux


fenetre.mainloop()

