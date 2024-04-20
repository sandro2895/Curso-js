function verificar()  {
  
  let data = new Date()
  let ano = data.getFullYear()
  let fano = document.getElementById("txt")
  let res = document.getElementById("res")
  let resul = document.getElementById ('resu')
  if (fano.value.length == 0 || Number(fano.value) > ano) {
  window.alert ('[ERRO] Verifique os dados e tente novamente.')
  } else {
    let fsex = document.getElementsByName("radsex")
    let idade = ano - fano.value
    let genero = ""
    let img = document.createElement('img')
    img.setAttribute('id', 'foto')
    if (fsex[0].checked){
    genero = "Homen"

        if(idade >=0 && idade <=11){
          img.setAttribute('src', 'bebe-menino.jpg') 
        }else if (idade <=21){
          img.setAttribute('src', 'jovem-homen.jpg')
        }else if (idade <=50){
          img.setAttribute('src', 'adulto-homen.png')
        }else{
          img.setAttribute('src', 'idoso-homen.png')
        }

    } else if (fsex[1].checked){
      genero = "Mulher"
      if(idade >=0 && idade <=11){
        img.setAttribute('src', 'bebe-menina.jpg')
      }else if (idade <=21){
        img.setAttribute('src', 'jovem-mulher.jpg')
      }else if (idade <=50){
        img.setAttribute('src', 'adulto-mulher.jpg')
      }else{
        img.setAttribute('src', 'idoso-mulher.png') 
      } 
    }
    resul.innerHTML = `Detectamos ${genero} com ${idade} anos`
    res.appendChild(img)
  }
}