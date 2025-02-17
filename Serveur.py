from random import randint

from flask import Flask, request, render_template, send_from_directory, jsonify

import subprocess

from threading import Thread

import threading

from GUI import tkinterhome

list_ids = set()

app = Flask("Ain't cappin this pic machine ain't doin' shit.")

@app.route('/')

def index():

    global client_ip
    
    client_ip = request.remote_addr
    
    list_ids.add(client_ip)

    return (render_template("GenPWeb.html"))

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

@app.route("/run_tk")

def startGUI():

    threading.Thread(target = tkinterhome, args = (list(list_ids))).start()
    
    return jsonify({"message": "GUI lancee avec IPs affichees."})

app.run(host="0.0.0.0", debug=False, port=6271)