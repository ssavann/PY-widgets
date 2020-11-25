'''
Tkinter : Créer des interfaces graphiques
Les widgets: Button 
'''

import tkinter

fenetre = tkinter.Tk() 
#forcer la dimension à 800x600
fenetre.geometry("800x600")    


#widget bouton
def BoutonAction():
    print("Vous avez cliquez sur le bouton...")


mon_buton = tkinter.Button(fenetre, text = "click moi !", 
    width = 20, height = 5, command = BoutonAction)



mon_buton.pack()

print(mon_buton.cget("text"))

mon_buton.config(text = "Push me...")


fenetre.mainloop()

