'''
Tkinter : Créer des interfaces graphiques
Les widgets: Entry -> zone de saisie 
'''

import tkinter

fenetre = tkinter.Tk() 
#forcer la dimension à 800x600
fenetre.geometry("800x600")    


#widget Entry
password = tkinter.Entry(fenetre, show="*", width = 30)
password.pack()



fenetre.mainloop()

