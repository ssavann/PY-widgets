'''
Tkinter : Créer des interfaces graphiques
Les widgets: Faire un grid() -> des grilles pour placer les widgets
row     ->rangé
column  ->colonne

'''

import tkinter
from tkinter import messagebox

fenetre = tkinter.Tk() 
#forcer la dimension à 800x600
fenetre.geometry("800x600")    


#widgets
label = tkinter.Label(fenetre, text="Widget label")
btn = tkinter.Button(fenetre, text="Bouton")
msg = tkinter.Message(fenetre, text = "Ceci est un exemple de message avec tkinter.")

label.grid(column=0, row=0)
btn.grid(column=1, row=1)
msg.grid(column=2, row=2)


fenetre.mainloop()

