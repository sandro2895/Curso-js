let numero = prompt ('Digite um número')

numero = Number(numero);

const numeroTitulo = document.getElementById('numero-titulo');
const nomeTexto = document.getElementById('texto');

numeroTitulo.innerHTML = numero;

nomeTexto.innerHTML = `<p> Seu numero +2 é ${numero +2}</p>` ;