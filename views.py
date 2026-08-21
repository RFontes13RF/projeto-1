from utils import load_template,add_anotacao, load_data, apaga_anotacao, busca_anotacao, edita_anotacao

def index():
    note_template = load_template('components/note.html')
    notes_li = [note_template.format(id = dados[0], title=dados[1], content=dados[2]) for dados in load_data('banco.db')]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    return add_anotacao('banco.db', titulo, detalhes)

def delete(id_anotacao):
    return apaga_anotacao('banco.db', id_anotacao)

def editar(id_anotacao):
    anotacao = busca_anotacao('banco.db', id_anotacao)
    return load_template('edit.html').format(id=anotacao[0],titulo=anotacao[1],detalhes=anotacao[2])

def salvar_edicao(titulo, detalhes, id_anotacao):
    return edita_anotacao('banco.db', titulo, detalhes, id_anotacao)
