import os
from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from redis import Redis

# Importa as rotas
from routes.filmes import filmes_bp
from routes.series import series_bp

# Funções auxiliares
from utils.helpers import sincronizar_dados

# Configuração do Redis
redis = Redis.from_url('redis://localhost:6379/0')

# Cria o app Flask
app = Flask(
    __name__,
    static_folder='HOMEPAGE',        # Onde estão JS, CSS e imagens
    template_folder='HOMEPAGE'       # Onde está o index.html
)

# Ativa o CORS
CORS(app)

# Limita requisições por IP
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="redis://localhost:6379/0"
)

# Registra os blueprints
app.register_blueprint(filmes_bp)
app.register_blueprint(series_bp)

# Sincroniza os dados ao iniciar
sincronizar_dados('Novosfilmes.json', 'CodeFilmesNomes.json')
sincronizar_dados('series.json', 'CodeSeriesNomes.json')


# === ROTAS ===

# Rota principal (Homepage)
@app.route('/')
def home():
    return render_template('index.html')


# Rota para arquivos da pasta GERAL
@app.route('/geral/<path:filename>')
def geral_static(filename):
    return send_from_directory('GERAL', filename)

# Rota para arquivos da pasta PAGES
@app.route('/pages/<path:filename>')
def pages_static(filename):
    return send_from_directory('PAGES', filename)

# Rota para imagens da pasta IMG
@app.route('/img/<path:filename>')
def img_static(filename):
    return send_from_directory('IMG', filename)


# === MAIN ===

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
