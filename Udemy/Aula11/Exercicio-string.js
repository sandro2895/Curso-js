const nome = prompt('Digite seu nome completo:');

numerosLetras = nome.length;
segLetra = nome[1];
indiceLetra = nome.indexOf('');
lastIndiceLetra = nome.lastIndexOf('');
letrasMaiusculas = nome.toUpperCase('')
letrasMinusculas = nome.toLowerCase('')

  document.body.innerHTML += `Seu nome é: <strong>${nome}<strong/><br />`;
  document.body.innerHTML += `Seu nome tem: <strong>${numerosLetras}<strong/> letras <br />`;
  document.body.innerHTML += `A segunda letra do seu nome é: <strong>${segLetra}<strong/><br />`;
  document.body.innerHTML += `O primeiro índice da letra LETRA no seu nome é: <strong>${indiceLetra}<strong/><br />`;
  document.body.innerHTML += `O último índice da letra LETRA no seu nome é: <strong>${lastIndiceLetra}<strong/><br />`;
  document.body.innerHTML += `As últimas 3 letras do seu nome são: ${nome.slice(-3)}<br />`;
  document.body.innerHTML += `As letras do seu nome são: ${nome.split('')}<br />`;
  document.body.innerHTML += `Seu nome com letras maiúsculas: <strong>${letrasMaiusculas}<strong/><br />`;
  document.body.innerHTML += `Seu nome com letras minúsculas: <strong>${letrasMinusculas}<strong/><br />`;
