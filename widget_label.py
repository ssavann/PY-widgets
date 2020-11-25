'''
Tkinter : Créer des interfaces graphiques
Les widgets: Label (message texte)
'''

import tkinter

fenetre = tkinter.Tk() 

#forcer la dimension à 800x600
fenetre.geometry("800x600")    

#création label: permet d'afficher un message
mon_label = tkinter.Label(fenetre, text = "Hello world", background = "orange")
mon_label.pack()  

#pour afficher ce que contient le message
print("le label contient " + mon_label.cget("text"))

#pour changer le texte
mon_label.config(text= "Salut à toi...")


fenetre.mainloop()

