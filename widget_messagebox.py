'''
Tkinter : Créer des interfaces graphiques
Les widgets: messagebox -> Boîte message system

showinfo
showerror
showwarning
askquestion
askokcancel
askyesnocancel

'''

import tkinter
from tkinter import messagebox

fenetre = tkinter.Tk() 
#forcer la dimension à 800x600
fenetre.geometry("800x600")    


#widget messagebox system
#messagebox.showinfo("information", "ceci est un test...")
#messagebox.showerror("information", "ceci est un test...")
#messagebox.showwarning("information", "ceci est un test...")
#messagebox.askquestion("information", "ceci est un test...")
#messagebox.askokcancel("information", "ceci est un test...")
#messagebox.askyesnocancel("information", "ceci est un test...")
#messagebox.askretrycancel("information", "ceci est un test...")

def info():
    messagebox.showinfo("information", "ceci est un test...")

btn = tkinter.Button(fenetre, text = "OK", command = info)
btn.pack()

fenetre.mainloop()

