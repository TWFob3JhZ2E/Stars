document.addEventListener("DOMContentLoaded", function () {
    const destaquesContainer = document.querySelector(".destaques-cards");

    // Função para carregar filmes novos
    function carregarFilmesNovos() {
        fetch('http://127.0.0.1:5001/filmes/novos')  // Alterando para a nova rota de filmes novos
            .then(response => response.json())
            .then(filmes => {
                filmes.forEach(filme => {
                    const card = document.createElement("div");
                    card.classList.add("movie-card");
                    card.innerHTML = `
                        <img src="${filme.capa}" alt="${filme.titulo}">
                        <h3>${filme.titulo}</h3>
                        <a href="https://superflixapi.cc/filme/${filme.id}" target="_blank" class="assistir-btn">Assistir</a>
                    `;
                    destaquesContainer.appendChild(card);
                });
            })
            .catch(error => console.error('Erro ao carregar filmes novos:', error));
    }

    // Função para carregar séries (se necessário, pode ser removido)
    function carregarSeries() {
        fetch('http://127.0.0.1:5001/series')
            .then(response => response.json())
            .then(series => {
                series.forEach(serie => {
                    const card = document.createElement("div");
                    card.classList.add("movie-card");
                    card.innerHTML = `
                        <img src="${serie.capa}" alt="${serie.titulo}">
                        <h3>${serie.titulo}</h3>
                        <a href="https://superflixapi.cc/serie/${serie.id}" target="_blank" class="assistir-btn">Assistir</a>
                    `;
                    destaquesContainer.appendChild(card);
                });
            })
            .catch(error => console.error('Erro ao carregar séries:', error));
    }

    // Carregar somente filmes novos e séries quando a página for carregada
    carregarFilmesNovos();
    carregarSeries();  // Esta função pode ser removida se você não for mais usar séries
});
