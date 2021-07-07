var p = document.querySelectorAll('input[type="text"]')


let cidade;

for (let x of p) {
    x.placeholder = '';
    if(x.name == 'cidade'){
        cidade = x;
    }
}

// var cidade = document.querySelector('input[name="cidade"]');
// var estado = document.querySelector('input[name="estado"]');
// var nome_ponto_t = document.querySelector('input[name="nome-ponto_turistico]"');


// var body = document.querySelector('body');

// body.onclick(function (){
//     for (let x of p) {
//         x.placeholder = '';
//     };
// });