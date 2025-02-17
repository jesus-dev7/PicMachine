document.querySelector('button').addEventListener('click', function() {

    var NewImage = document.getElementById("NewImage");

    NewImage.src = "/img_get";
});

document.querySelector('#affichage_IPs').addEventListener('click', function() {

    fetch("/run_tk")

        .then(response => response.json())

        .then(data => console.log(data.message))

        .catch(error => console.error('Erreur:', error));

});
