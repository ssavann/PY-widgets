'''
Tkinter : Créer des interfaces graphiques
Les widgets: Faire un place() -> pour placer les widgets


'''

import tkinter
from tkinter import messagebox

fenetre = tkinter.Tk() 
#forcer la dimension à 800x600
fenetre.geometry("800x600")    


#widgets
label = tkinter.Label(fenetre, text="texte du label", bg="blue")
label2 = tkinter.Label(fenetre, text="texte du label", bg="orange")
label.place(x=100, y=100)
label2.place(x=200, y=200)


fenetre.mainloop()

