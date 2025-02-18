from random import randint

from flask import Flask, request, render_template, send_from_directory, jsonify

import subprocess

from threading import Thread

import threading

from GUI import tkinterhome

from GUI import tkinterhomeChat

list_ids = set()

txt_chat = ""

app = Flask("Ain't cappin this pic machine ain't doin' shit.")

@app.route('/')

def index():

    global client_ip
    
    client_ip = request.remote_addr
    
    list_ids.add(client_ip)

    return (render_template("Authentification.html"))

@app.route('/Resultat')

def index_():   
 
    return (render_template("Resultat.html"))

@app.route('/img_get')

def img_get():
    
    dico = {
    
        "1": "image1.jpeg",
        
        "2": "image2.jpeg",
        
        "3": "image3.jpeg",
        
        "4": "image4.jpeg",
        
        "5": "image5.jpeg",
    
    }

    indice = randint(1, 5)

    img_src = dico[str(indice)]
    
    return(send_from_directory("static", img_src))

@app.route("/recup_IPs")

def Recup_Ips():
    
    return jsonify({"IPs": list(list_ids)})

@app.route("/run_tk")

def startGUI():

    threading.Thread(target = tkinterhome, args = (list(list_ids),)).start()
    
    return jsonify({"message": "GUI lancee avec IPs affichees."})

@app.route("/auth_get", methods = ["POST"])

def auth():
    
    Valid = 0
    
    DonneesU = {
        
        "Soka7": "192.168.0.47",
        
        "Patrick": "192.168.0.47"
        
    }
    
    MdpU = {
        
        "Soka7": "BobF4*10^70N",
        
        "Patrick": "BobCunFou"
        
    }
    
    Pseudo = request.form.get("Pseudo")
    
    try:
    
        if request.remote_addr == DonneesU[Pseudo]:
            
            Valid += 1
            
    except:
        
        return("Va jouer aux heros ailleurs.")
    
    Mdp = request.form.get("Mdp")
    
    if Mdp == MdpU[Pseudo]:
        
        Valid += 1
    
    if Valid == 2:
        
        return(render_template("GenPWeb.html"))
    
    else:
        
        return("Va jouer aux heros ailleurs.")
    
@app.route("/recupChat", methods = ["GET", "POST"])
    
def recup_chat():
    
    if request.method == "POST":
    
        try:
        
            global txt_chat
            
            recup = request.get_json().get("message", "")
            
            txt_chat += "\n" + recup
            
            return jsonify({"status": "Message reçu"}), 200  # Confirmer l'ajout
        
        except Exception as e:
            
            return jsonify({"error": str(e)}), 400  # Retourner une erreur en cas de problème

    elif request.method == "GET":
    
            return(jsonify({"Chat": txt_chat}))

@app.route("/LancementChat")

def LancementChat():
    
    threading.Thread(target = tkinterhomeChat).start()
    
    return jsonify({"message": "Chat lance."})

app.run(host="0.0.0.0", debug=False, port=6269)