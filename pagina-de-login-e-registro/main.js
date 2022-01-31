function registrar() {
    let nome = document.getElementById('nomer')
    let email = document.getElementById('emailr')
    let senha = document.getElementById('senhar')
    let senha2 = document.getElementById('senharr')

    while (senha.value != senha2.value) {
        alert('As senhas não são iguais')
        senha.value = ''
        senha2.value = ''
        return
    }
    alert('Passou')
}