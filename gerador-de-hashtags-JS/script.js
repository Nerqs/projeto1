function copiar() {
    let copia = document.getElementById('texto')
    let text = copia.outerText
    navigator.clipboard.writeText(text)
}

var txt = 'Nenhum arquivo carregado'

function analizar(files) {
    const reader = new FileReader()
    reader.onloadend = (event) => {
        console.log(event)
        let data = event.target.result
        txt = data
    }
    reader.readAsText(files[0])
}

function comecar() {
    let quant = document.getElementById("txtquant")
    let quant2 = Number(quant.value) 
    let texto =  document.querySelector("div#texto")
    texto.innerHTML = ''
    let conteudo = txt.split(';')
    if (quant.value.length == 0 || quant2 == 0) {
        alert('Preencha a quantidade de hashtags que você deseja!!')
    } else {
        misturar(conteudo)
        for (let c = 0; c < quant2; c++) {
            texto.innerHTML += ` ${conteudo[c]}`
            if (conteudo[c] == '') {
                break
            }
        }
    }
    function misturar() {
        let m = conteudo.length - 1, t, i
        while (m) {
            i = Math.floor(Math.random() * m--)
            t = conteudo[m]
            conteudo[m] = conteudo [i]
            conteudo[i] = t
        }
        return conteudo
    }
}
