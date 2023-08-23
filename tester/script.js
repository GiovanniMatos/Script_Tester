const h2color = document.getElementById('h2');
h2color.style.color = 'blue';
const form = document.getElementsByTagName('form');
var teste = "teste";

function map(f, a) {
    var result = []; // Cria um novo Array
    var i;
    for (i = 0; i != a.length; i++) result[i] = f(a[i]);
    return result;
  }

function teste(t, a) {
    var t = []; // Cria um novo Array
    var t;
    for (t = 0; t != a.length; t++) result[t] = f(a[t]);
    return t;
  }