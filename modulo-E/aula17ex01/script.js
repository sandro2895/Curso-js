function tabular(){
  let num = document.getElementById("txtn")
  let tab = document.getElementById("seltab")
  if(num.value == 0){
    tab.innerHTML = ''
    window.alert('Por favor, digite um número!')
  }else {
    let n = Number(num.value)
    let c = 1
    tab.innerHTML = ''
    while (c <= 10) {
      let item = document.createElement('option')
      item.text = `${n} x ${c} = ${n*c}`
      item.value = `tab${c}`
      tab.appendChild(item)
      c++
    }
  }


}