'''
Tkinter : Créer des interfaces graphiques
Les widgets: Faire un pack() 


'''

import tkinter
from tkinter import messagebox

fenetre = tkinter.Tk() 
#forcer la dimension à 800x600
fenetre.geometry("800x600")    


#widgets
label = tkinter.Label(fenetre, text = "label")
#ajout d'une couleur de fond et un padding de 200px
#btn = tkinter.Button(fenetre, text = "bouton", bg = "red", padx = 200)
btn = tkinter.Button(fenetre, text = "bouton", bg = "red", width = 50)

label.pack()
#btn.pack(fill = "x")       #remplissage sur l'axe des "x"
#btn.pack(fill = "both")    
#btn.pack(expand = True)     #positionnement centré
btn.pack()


fenetre.mainloop()

