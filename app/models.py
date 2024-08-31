from app import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    informacoes = db.Column(db.Text, nullable=False)
    jogos = db.Column(db.Text, nullable=False)
    categorias = db.Column(db.Text, nullable=False)
    consoles = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Game {self.nome}>'
