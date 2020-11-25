'''
Tkinter : Créer des interfaces graphiques
Les widgets: Message 
'''

import tkinter

fenetre = tkinter.Tk() 

#forcer la dimension à 800x600
fenetre.geometry("800x600")    

#creation widget Message 
mon_message = tkinter.Message(fenetre, text = "Bonjour a vous tous !!!")

mon_message.pack()

print(mon_message.cget("text"))
mon_message.configure(text = "Hello world...")
#pour remplacer le message principale


fenetre.mainloop()

