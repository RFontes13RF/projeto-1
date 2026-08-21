from flask import Flask, render_template_string, request, redirect
import views
from utils import cria_tabela


app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():

    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  # Obtém o valor do campo 'titulo'
    detalhes = request.form.get('detalhes')  # Obtém o valor do campo 'detalhes'

    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete/<int:id_anotacao>/')
def delete(id_anotacao):
    views.delete(id_anotacao)
    return redirect('/')

@app.route('/update/<int:id_anotacao>/')
def update(id_anotacao):
    return render_template_string(views.editar(id_anotacao))

@app.route('/update', methods=['POST'])
def update_submit():
    id_anotacao = request.form.get('id')
    titulo = request.form.get('titulo')
    detalhes = request.form.get('detalhes')
    views.salvar_edicao(titulo, detalhes, id_anotacao)
    return redirect('/')
    

if __name__ == '__main__':
    cria_tabela('banco.db')
    app.run(debug=True)