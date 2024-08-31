
from flask import render_template, redirect, url_for, request

from app import app
from app.forms import JogoForm


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/jogos/novo', methods=['GET', 'POST'])
def novoJogo():
    form = JogoForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('home'))
    return render_template('cadastro.html', form=form)

@app.route('/saida', methods=['POST'])
def saida():
    nome = request.form.get('nome')
    informacoes = request.form.get('textarea')
    categorias = request.form.getlist('categorias')
    consoles_selecionados = request.form.getlist('consoles')

    # Certifique-se de que as listas têm o mesmo comprimento
    return render_template('saida.html', nome=name, informacoes=info,
                           jogos=jogos_selecionados, categorias=categorias_selecionadas,
                           consoles=consoles_selecionados)

