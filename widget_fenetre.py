import tkinter

fenetre = tkinter.Tk() 

#donner un titre à la fenêtre
fenetre.title("Mon premier programme python Tkinter")

#forcer la dimension à 800x600
#fenetre.geometry("800x600")     

#dimension minimum, peut pas diminuer d'avantage
#fenetre.minsize(640, 400)

#dimension maximum, grandeur maximum
#fenetre.maxsize(1024, 800)

#une dimension fixe, ne peut redimensionner
#fenetre.resizable(width =  False, height = False)

#pour center une fenetre, il faut prendre la largeur de notre écran / 2
fenwidth = 960
fenheight = 540
posx = int(fenetre.winfo_screenwidth() /2) - int(fenwidth /2)
posy = int(fenetre.winfo_screenheight() /2) - int(fenheight /2)

geo = "{}x{}+{}+{}".format(fenwidth, fenheight, posx, posy)

fenetre.geometry(geo)

fenetre.mainloop()

#print("Fin de programme")