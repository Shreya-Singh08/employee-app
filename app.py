from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
Employee Management Application - Version 4

APP_NAME={os.getenv('APP_NAME')}
APP_ENV={os.getenv('APP_ENV')}
COMPANY={os.getenv('COMPANY')}

DB_USERNAME={os.getenv('DB_USERNAME')}
DB_PASSWORD={os.getenv('DB_PASSWORD')}
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)