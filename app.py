from random import randint

from flask import Flask, request, render_template, send_from_directory, jsonify

import subprocess

from threading import Thread

import threading

from flask_socketio import SocketIO, send

# Dictionnaires pour utilisateurs et mots de passe
users = {
    "Soka7": "192.168.0.47",
    "Patrick": "192.168.0.47",
    "Annafee": "192.168.0.23"
}

passwords = {
    "Soka7": "BobF4*10^70N",
    "Patrick": "BobCunFou",
    "Annafee": "sudoku"
}

# Liste des IPs connectées
list_ids = set()

app = Flask("Serv")

app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, cors_allowed_origins="*")

# Page principale d'authentification
@app.route('/')
def index():
    global client_ip
    client_ip = request.remote_addr
    list_ids.add(client_ip)
    return render_template("Authentification.html")

# Page après authentification
@app.route('/PicMachine')
def pic_machine():
    return render_template("PicMachine.html")

# Page du chat
@app.route('/Chat')
def chat():
    return render_template("chat.html")

# Récupérer une image aléatoire
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
    
    return send_from_directory("static/images", img_src)

# Récupérer les IPs connectées
@app.route("/recup_IPs")
def recup_ips():
    return jsonify({"IPs": list(list_ids)})

# Récupérer le pseudo basé sur l'IP
@app.route("/recupPseudo", methods=["GET"])
def recup_pseudo():
    pseudo = {
        "192.168.0.47": "Soka7",
        "192.168.0.23": "Annafee",
        "127.0.0.1": "Soka7"
    }
    
    return jsonify({"Pseudo": pseudo.get(request.remote_addr, "Inconnu")})

# Authentification des utilisateurs
@app.route("/auth_get", methods=["POST"])
def auth():
    pseudo = request.form.get("Pseudo")
    mdp = request.form.get("Mdp")
    
    if pseudo in users and passwords.get(pseudo) == mdp:
        return render_template("PicMachine.html")  # Redirige vers la page principale après une authentification réussie
    else:
        return "Nom d'utilisateur ou mot de passe incorrect", 403

@socketio.on('message')
def handle_message(msg):
    print(f'Message reçu : {msg}')
    send(msg, broadcast=True)

socketio.run(app, host='0.0.0.0', port=6269, debug = False)