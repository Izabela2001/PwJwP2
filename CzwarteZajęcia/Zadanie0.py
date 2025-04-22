# Zadanie 0 – Środowisko wirtualne i requirements.txt
import Flask
from flask_sqlalchemy import SQLAlchemy

# requirements.txt
Flask>=3.0
SQLAlchemy==2.0.40


# test_app_with_flask.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask!"

if __name__ == '__main__':
    app.run(debug=True)