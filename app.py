# app.py
from flask import Flask
from webhook import webhook
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

# Define supported languages
app.config['LANGUAGES'] = ['en', 'pt', 'es', 'fr', 'de', 'it', 'nl', 'pl', 'ru', 'ja', 'ko', 'zh']

app.register_blueprint(webhook)

if __name__ == "__main__":
    app.run(port=5000)
