function carregar() {
  let msg = window.document.getElementById("msg")
  let img = window.document.getElementById("imagem")
  let data = new Date()
  // let hora = data.getHours()
  hora = 18
  
  
  msg.innerHTML = `Agora são ${hora} horas.` 

  if (hora >= 0 && hora <12) {
    img.src = 'sol-manha.jpg'
   document.body.style.background ="#fbe689"
   let foto = window.document.getElementById("fot")
   foto.style.background ="#dbad1a"
   let texto = window.document.getElementById("text")
    texto.style.color ="orange"

  }else if (hora >= 12 && hora < 18) {
    img.src = 'sol-tarde.jpg'
    document.body.style.background ="#f7f376"
    let texto = window.document.getElementById("text")
    texto.style.color ="rgb(201, 201, 0)"
    

  }else {
    img.src = 'lua-noite.jpg'
    document.body.style.background ="#00466a"
    let foto = window.document.getElementById("fot")
    foto.style.background ="#083145"
    let texto = window.document.getElementById("text")
    texto.style.color ="cadetblue"

  }

}