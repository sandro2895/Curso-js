function criaPessoa (nome, sobrenome, idade) {
   return {
    nome: nome,
    sobrenome: sobrenome,
    idade: idade
   }
}

let pessoa1 = criaPessoa('Luiz', 'Otavio', 25)
let pessoa2 = criaPessoa('Maria', 'Cavalcante', 19)
console.log(pessoa1)
console.log(pessoa2.nome, pessoa2.idade)