let pessoal = {
  nome:'Luiz',
  sobrenome: 'Miranda',
  idade: 25,

  fala () {
    console.log (`Minha idade é ${this.idade}`); 
  },
  incrementaIdade() {
    this.idade++;
 }
};

pessoal.fala();
pessoal.incrementaIdade();
pessoal.incrementaIdade();
pessoal.incrementaIdade();
pessoal.fala();
