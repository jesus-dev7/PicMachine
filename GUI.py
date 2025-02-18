import tkinter as tk

from tkinter import ttk, messagebox

from tkinter import Tk, Label

import requests

import json

global ChatContenu

ChatContenu = ""

def updt(label):
    
    try:
        
        reponse = requests.get("http://localhost:6269/recup_IPs")
        
        if reponse.status_code == 200:
            
            IPs = reponse.json().get("IPs", [])
        
        label.config(text = f"IPs connectées: {IPs}")
        
    except Exception as e:
        
        label.config(text = f"Erreur mise a jour. {e}")
        
    label.after(5000, updt, label)

def tkinterhome(IPs):
    
    """Fenêtre principale.
    
    E: type: None, None
    
    S: type: None, None
    """
            
    Home = Tk() #Crée la fenêtre.
    
    frm = tk.Frame(Home, bg = "Black", bd = 5, relief = "ridge") #Crée un cadre.
    
    frm.grid(padx = 10, pady = 10) #On organise le cadre avec une grille.
    
    Home.geometry("400x300")
    
    Home.rowconfigure(0, weight=1) #On configure la ligne 0 pour qu'elle s'adapte à la taille de la fenêtre.
    
    Home.columnconfigure(0, weight=1) #On configure la colonne 0 pour qu'elle s'adapte à la taille de la fenêtre.
    
    global LabelIPs
    
    global Bouton_
    
    LabelIPs = tk.Label(frm, text = f"IPs connectées: {IPs}", bg = "Orange", relief = "sunken") #Une étiquette.
    
    LabelIPs.grid(column=0, row=0, sticky = "nsew") #Etiquette.
    
    Bouton_ = tk.Button(frm, text="Quit", command=Home.destroy, bg = "red") #Bouton pour détruire la
    
    Bouton_.grid(column=1, row=3, sticky = "nsew") #Bouton pour détruire la fenêtre.

    updt(LabelIPs)

    #BoucleBase
    Home.mainloop()
    
def updtChat(label_):
    
    global ChatContenu
    
    try:
        
        reponse_ = requests.get("http://localhost:6269/recupChat")
        
        if reponse_.status_code == 200:
            
            ChatContenu = reponse_.json().get("Chat", "")
        
        label_.config(text = f"Chat: {ChatContenu}")
        
    except Exception as e:
        
        label_.config(text = f"Erreur mise a jour. {e}")
        
    label_.after(5000, updtChat, label_)
    
def SendChat(entree):
    
    url = "http://localhost:6269/recupChat"
    
    headers = {"Content-Type": "application/json"}
    
    data = {"message": entree}
    
    reponse_ = requests.post(url, headers = headers, data = json.dumps(data))
    
    if reponse_.status_code == 200:
        
        print("Message envoyé avec succès")
        
    else:
        
        print("Erreur lors de l'envoi du message")
    
def RecupMessage():
    
    entree = EntryChat.get()
    
    if entree:
        
        SendChat(entree)
        
        EntryChat.delete(0, tk.END)

def tkinterhomeChat():
    
    """
    
    Fenêtre chat.
    
    E: type: None, None
    
    S: type: None, None
    
    """
    
    global ChatContenu
            
    Chat = Tk() #Crée la fenêtre.
    
    frm = tk.Frame(Chat, bg = "Black", bd = 5, relief = "ridge") #Crée un cadre.
    
    frm.grid(padx = 10, pady = 10) #On organise le cadre avec une grille.
    
    Chat.geometry("400x300")
    
    Chat.rowconfigure(0, weight=1) #On configure la ligne 0 pour qu'elle s'adapte à la taille de la fenêtre.
    
    Chat.columnconfigure(0, weight=1) #On configure la colonne 0 pour qu'elle s'adapte à la taille de la fenêtre.
    
    global LabelChat
    
    global Bouton_
    
    global EntryChat
    
    LabelChat = tk.Label(frm, text = f"Chat: {ChatContenu}", bg = "Orange", relief = "sunken") #Une étiquette.
    
    LabelChat.grid(column=0, row=0, sticky = "nsew") #Etiquette.
    
    EntryChat = tk.Entry(frm, text="Chat", bg = "Lightgreen", relief = "ridge", bd = 6, font = ("bold"))
    
    EntryChat.grid(column=0, row=1, sticky = "nsew") #Etiquette.
    
    Bouton_ = tk.Button(frm, text = "Send", command = RecupMessage, bg = "blue") #Bouton pour envoyer le message.
    
    Bouton_.grid(column=1, row=2, sticky = "nsew") #Bouton pour détruire la fenêtre.
    
    BoutonChat = tk.Button(frm, text="Quit", command = Chat.destroy, bg = "red") #Bouton pour détruire la
    
    BoutonChat.grid(column=1, row=3, sticky = "nsew") #Bouton pour détruire la fenêtre.

    updtChat(LabelChat)

    #BoucleBase
    Chat.mainloop()