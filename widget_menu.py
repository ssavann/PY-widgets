'''
Tkinter : Créer des interfaces graphiques
Les widgets: Faire un place() -> pour placer les widgets


'''

import tkinter
from tkinter import messagebox

fenetre = tkinter.Tk() 
#forcer la dimension à 800x600
fenetre.geometry("800x600")    

#fonction de menu
def quitter():
    quit()

def ouvrir():
    fenouvrir = tkinter.Toplevel(fenetre)
    fenouvrir.geometry("200x200")
    fenouvrir.title("Fenetre Ouvrir")
    lbl = tkinter.Label(fenouvrir, text = "Label....")
    lbl.pack()


#widgets menu
mon_menu = tkinter.Menu(fenetre)

fichier_menu = tkinter.Menu(mon_menu, tearoff = 0)
fichier_menu.add_command(label = "Ouvrir", command=ouvrir)
fichier_menu.add_command(label = "Enregistrer")
fichier_menu.add_command(label = "Quitter", command=quitter)

edition_menu = tkinter.Menu(mon_menu)
edition_menu.add_command(label = "Copier")
edition_menu.add_separator()
edition_menu.add_command(label = "Coller")

mon_menu.add_cascade(label="Fichier", menu = fichier_menu)
mon_menu.add_cascade(label="Edition", menu = edition_menu)

fenetre.configure(menu = mon_menu)



fenetre.mainloop()

