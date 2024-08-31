from flask import Flask
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from app import db
from app.models import Game


class JogoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    informacooes = StringField('Informações', validators=[DataRequired()])
    jogos = StringField('Jogos', validators=[DataRequired()])
    categorias = TextAreaField('Categorias', validators=[DataRequired()])
    consoles = StringField('Consoles', validators=[DataRequired()])
    submit = SubmitField('Salvar')

    def validate_title(self, title):
        jogo_existente = Game.query.filter_by(title=title.data).first()
        if jogo_existente and (self.jogo_id is None or jogo_existente.id != self.jogo_id):
            raise ValidationError("Jogo já cadastrado.")

    def save(self, jogo=None):
        if jogo is None:
            jogo = Game()

        nome = self.nome.data,
        informacoes = self.informacoes.data,
        jogos = self.jogos.data,
        categorias = self.categorias.data,
        consoles = self.consoles.data

        db.session.add(jogo)
        db.session.commit()
        return jogo
