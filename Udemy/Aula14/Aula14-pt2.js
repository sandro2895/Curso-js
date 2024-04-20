let numero = prompt ('Digite um número')

numero = Number(numero);

const numeroTitulo = document.getElementById('numero-titulo');
const nomeTexto = document.getElementById('texto');

numeroTitulo.innerHTML = numero;

nomeTexto.innerHTML = ``;

nomeTexto.innerHTML += `<p>Raiz quadrada : ${numero ** 0.5}</p>`;

nomeTexto.innerHTML += `<p>${numero} é inteiro : ${Number.isInteger(numero)}</p>`;

nomeTexto.innerHTML += `<p>${numero} é NaN : ${Number.isNaN(numero)}</p>`;

nomeTexto.innerHTML += `<p> Arredondando pra baixo é : ${Math.floor(numero)}</p>`;

nomeTexto.innerHTML += `<p> Arredondando pra cima é : ${Math.ceil(numero)}</p>`;

nomeTexto.innerHTML += `<p> Com duas casas decimais : ${numero.toFixed(2)}</p>`;