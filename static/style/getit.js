// Pegamos o formulário da página
const form = document.querySelector("form");


// Executa esta função quando o formulário for enviado
form.addEventListener("submit", function(event) {

    // Pegamos o que foi digitado nos campos
    const titulo = document.querySelector("#titulo").value.trim();
    const detalhes = document.querySelector("#detalhes").value.trim();


    // Verificamos se algum campo está vazio
    if (titulo === "" || detalhes === "") {

        // Impede o formulário de ser enviado
        event.preventDefault();

        // Mostra uma mensagem para o usuário
        alert("Preencha o título e os detalhes.");
    }

});