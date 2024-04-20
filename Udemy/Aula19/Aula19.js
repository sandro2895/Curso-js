let a = [1, 2, 3]
let b = [...a];
let c = b;
console.log(a, b, c);

a.push(4);
console.log(a,b, c);

b.pop();
console.log(a, b, c);