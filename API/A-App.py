from flask import Flask
from flask_cors import CORS

# Removido temporariamente:
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address
# from redis import Redis

# Importa as rotas e funções auxiliares
from routes.filmes import filmes_bp
from routes.series import series_bp
from utils.helpers import sincronizar_dados

# Inicializa o app Flask
app = Flask(__name__)

# Configuração CORS (permite acesso de diferentes origens)
CORS(app)

# ❌ Desativado temporariamente:
# Configuração do Redis + Limiter
# redis = Redis.from_url('redis://localhost:6379/0')
# limiter = Limiter(
#     get_remote_address,
#     app=app,
#     storage_uri="redis://localhost:6379/0"
# )

# ✅ Registra as rotas
app.register_blueprint(filmes_bp)
app.register_blueprint(series_bp)

# 📁 Sincroniza os dados antes de iniciar o servidor
sincronizar_dados('Novosfilmes.json', 'CodeFilmesNomes.json')
sincronizar_dados('series.json', 'CodeSeriesNomes.json')

# 🚀 Inicializa o app com o debug DESATIVADO (para segurança)
# ✅ Usa host='0.0.0.0' e porta dinâmica para funcionar no Render
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 10000))
    app.run(debug=False, host='0.0.0.0', port=port)
