'''
Tkinter : Créer des interfaces graphiques
Les widgets: Variables de contrôle -> 
StringVar()     -> Chaine de caractère STR
IntVar()        -> Nombre entier INT
DoubleVar()     -> Nombre flottant FLOAT
BoolVar()       -> Booléen BOOL
'''

import tkinter
from tkinter import messagebox

fenetre = tkinter.Tk() 
#forcer la dimension à 800x600
fenetre.geometry("800x600")    


var_label = tkinter.StringVar()
label = tkinter.Label(fenetre, textvariable = var_label)
label.pack()

label2 = tkinter.Label(fenetre, textvariable = var_label)
label2.pack()


#avec getter et setter
var_label.set("Le python est fantastique!")
print(var_label.get())


fenetre.mainloop()

