document.getElementById("fetchButton").addEventListener("click", function() {
    fetch('https://power-path-backend-3e6dc9fdeee0.herokuapp.com/test')
    .then(response => response.json())
    .then(data => {
        document.getElementById("dataText").innerHTML = data;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

