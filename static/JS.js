// Générer une nouvelle image
document.querySelector('.btnIm').addEventListener('click', function() {
    var NewImage = document.getElementById("NewImage");
    NewImage.src = "/img_get";
});

document.querySelector('#BtnChat').addEventListener('click', function() {
    window.location.href = "/Chat";  // Redirige vers la page Chat
});


// Récupérer et afficher les IPs
async function IPs() {
    const reponse = await fetch("/recup_IPs");
    const data = await reponse.json();
    const ListIPs = document.getElementById("IPS");

    if (data.IPs && data.IPs.length > 0) {
        ListIPs.innerHTML = data.IPs.join("<br>");
    } else {
        ListIPs.innerHTML = "Pas d'IP.";
    }
}

IPs();
setInterval(IPs, 5000);

// Mettre à jour le chat
async function updtChat() {
    const ContenuChat_ = document.getElementById("Chat");
    const reponse_ = await fetch("/recupChat");
    const data = await reponse_.json();

    ContenuChat_.innerHTML = data.Chat.join("<br>");
}

updtChat();

setInterval(updtChat, 5000);

// Fonction pour envoyer un message
async function SendChat(entree) {
    const url = "/recupChat";
    const data = {"message": entree};

    const reponse_ = await fetch(url, {
        headers: {"Content-Type": "application/json"},
        method: "POST",
        body: JSON.stringify(data),
    });
}

// Fonction pour récupérer le message et l'envoyer
async function RecupMessage() {
    const Pseudo_ = await fetch("/recupPseudo");
    const data = await Pseudo_.json();

    let txt_p = document.getElementById("messageInput").value;

    let Pseudo = data.Pseudo || "Pseudo vide."; // Pseudo ou "Pseudo vide" si non défini

    let entree = `${Pseudo}: ${txt_p}`;

    SendChat(entree);

    document.getElementById("messageInput").value = "";

}

// Événement sur le bouton "Envoyer"
document.querySelector('#Send').addEventListener('click', RecupMessage);