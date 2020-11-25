'''
Tkinter : Créer des interfaces graphiques
Les widgets: Observateurs 

Mode:
w   Write   ->  variable modifiée
r   Read    ->  variable lue

'''

import tkinter
from tkinter import messagebox

fenetre = tkinter.Tk() 
#forcer la dimension à 800x600
fenetre.geometry("800x600")    


#Observateur
def observateur_saisie(*args):
    var_label.set("Vous avez écrit: " + var_saisie.get())




#widget entry
var_saisie = tkinter.StringVar()
sasie = tkinter.Entry(fenetre, textvariable = var_saisie)
var_saisie.trace("w", observateur_saisie)   #assigner un observateur
sasie.pack()

#widget Label
var_label = tkinter.StringVar()
label = tkinter.Label(fenetre, textvariable = var_label)
var_label.set("Label")
label.pack()


fenetre.mainloop()

