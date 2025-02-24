document.querySelector('.btnIm').addEventListener('click', function() {
    var NewImage = document.getElementById("NewImage");
    NewImage.src = "/img_get?" + new Date().getTime();  // Force le rechargement
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