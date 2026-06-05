 import os
import time
from flask import Flask
import psycopg2

app = Flask(__name__)

def get_db_connection():
    # Intenta conectarse usando las variables de entorno que definiremos en el compose
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('DB_NAME', 'taller_db'),
        user=os.environ.get('DB_USER', 'admin'),
        password=os.environ.get('DB_PASSWORD', 'secret')
    )

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f'<h1>🚀 Taller 3.0: Flask + PostgreSQL Exitoso</h1><p>Conectado a: {db_version[0]}</p><p>Autor: Fernando Cajias</p>'
    except Exception as e:
        return f'<h1>❌ Error de conexión a la Base de Datos</h1><p>{str(e)}</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
