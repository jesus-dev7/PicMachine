from random import randint

from flask import Flask, request, render_template, send_from_directory, jsonify

import subprocess

from GUI import tkinterhome

app = Flask("Ain't cappin this pic machine ain't doin' shit.")

@app.route('/')

IPs_connectes = set()

def index():
    
    global client_ip
    
    client_ip = request.remote_addr
    
    IPs_connectes.add(client_ip)

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
    
@app.route("/affichage_IPs")
    
def get_IPs():
    
    return jsonify({"IPs": list(IPs_connectes)})

@app.route("/run_tk", method = ['POST'])

def run_tkinterhome():
    
    
    
    return jsonify({"message": "GUI lancee."})

app.run(host="0.0.0.0", debug=False, port=6271)