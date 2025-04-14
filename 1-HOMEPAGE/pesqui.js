async function buscarSugestoes(texto) {
    const sugestoesDiv = document.getElementById('sugestoes');
    sugestoesDiv.innerHTML = '';
    if (texto.length < 2) return;
  
    try {
      const res = await fetch(`http://localhost:5001/buscar?q=${encodeURIComponent(texto)}`);
      const dados = await res.json();
  
      dados.forEach(item => {
        const div = document.createElement('div');
        div.className = 'sugestao-item';
  
        const img = document.createElement('img');
        img.src = item.capa || 'https://via.placeholder.com/40x60?text=?';
  
        const span = document.createElement('span');
        span.textContent = item.titulo;
  
        div.appendChild(img);
        div.appendChild(span);
  
        div.onclick = () => {
          // Redireciona para play.html com ID do conteúdo
          window.location.href = `../2-PAGES/player.html?id=${item.id}`;

        };
  
        sugestoesDiv.appendChild(div);
      });
    } catch (err) {
      console.error('Erro na busca:', err);
    }
  }