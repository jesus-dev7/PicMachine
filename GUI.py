import tkinter as tk

from tkinter import ttk, messagebox

from tkinter import Tk, Label

def tkinterhome(IPs):
    
    """Fenêtre principale.
    
    E: type: None, None
    
    S: type: None, None
    """
            
    Home = Tk() #Crée la fenêtre.
    
    frm = tk.Frame(Home, bg = "Black", bd = 5, relief = "ridge") #Crée un cadre.
    
    frm.grid(padx = 10, pady = 10) #On organise le cadre avec une grille.
    
    Home.rowconfigure(0, weight=1) #On configure la ligne 0 pour qu'elle s'adapte à la taille de la fenêtre.
    
    Home.columnconfigure(0, weight=1) #On configure la colonne 0 pour qu'elle s'adapte à la taille de la fenêtre.
    
    global LabelGest
    
    global Bouton_
    
    LabelGest = tk.Label(frm, text = f"IPs connectées: {IPs}", bg = "Orange", relief = "sunken") #Une étiquette.
    
    LabelGest.grid(column=0, row=0, sticky = "nsew") #Etiquette.
    
    Bouton_ = tk.Button(frm, text="Quit", command=Home.destroy, bg = "red") #Bouton pour détruire la
    
    Bouton_.grid(column=1, row=3, sticky = "nsew") #Bouton pour détruire la fenêtre.


    #BoucleBase
    Home.mainloop()