from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from local_settings import SECRET_KEY

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instanciando os objetos 'banco de dados' e 'migrate'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views
from app.models import Game
