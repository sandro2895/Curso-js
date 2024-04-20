const nomeClient = 'Doca Augusto';
const sobreNomeClient = 'de Oliveira';
const idade = 27;
const peso = 120;
const alturaEmM =  1.80;
let imc = peso / (alturaEmM * alturaEmM)
let anoNascimento = 2022 - idade;

console.log (`${nomeClient} ${sobreNomeClient} nasceu em ${anoNascimento} e tem ${idade} anos.`)
console.log(`Pesa ${peso}KG e tem ${alturaEmM} de altura.`)
console.log(`Fazendo seu Índice de massa corporal(imc) ser ${imc}.`)