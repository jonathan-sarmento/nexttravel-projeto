
let estado = document.querySelector('input[name="estado"]');
let cidade = document.querySelector('input[name="cidade"]');
let url = document.querySelectorAll('input[placeholder="Ex: https://www.google.com"]');

estado.addEventListener('input', function () {
    estado.value = this.value.toUpperCase();
});

cidade.addEventListener('input', function () {
    cidade.value = titleize(this.value);
});

for (let x of [0, 1]){
    url[x].addEventListener('input', function () {
        url[x].value = this.value.trim();
    });
}

function titleize(text) {
    var words = text.toLowerCase().split(" ");
    for (var a = 0; a < words.length; a++) {
        var w = words[a];
        words[a] = w[0].toUpperCase() + w.slice(1);
    }
    return words.join(" ");
}

