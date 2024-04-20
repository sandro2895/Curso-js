const nome1 = 'doca'; // string
const idade1 = 27; // number
let altura1 = 1.80;  // number com ponto flutuante(flot)
let futuro; // Undefined = não aponta para local nenhum na memória.é automatico
let sobreNome = null; // Nulo --> Não aponta para local nenhum na memória. usado quando você quer explicitamente que a variavel não aponte para nenhum lugar na memória
let aprovado = true; //boolean só poder ser true ou false (logico).pode ser usado para mudar o fluxo da aplicação.


console.log(typeof(sobreNome), sobreNome)


 // Isso faz ambas variavels terem o mesmo valor:
let a = 4; 
let b = a ; // o valor de b sempre continua sendo uma copia do valor de a nesse exato momento
console.log(a, b)

a = 5; // o valor de a pode ser mudado mas o de b continuara o mesmo.
console.log(a, b)
b = a // o valor de b sera mudado novamento para o valor de a caso seja redeclarado o valor.

console.log(a, b)