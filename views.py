from utils import load_template,add_anotacao, load_data, apaga_anotacao

def index():
    note_template = load_template('components/note.html')
    notes_li = [note_template.format(id = dados[0], title=dados[1], content=dados[2]) for dados in load_data('banco.db')]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    return add_anotacao('banco.db', titulo, detalhes)

def delete(id_anotacao):
    return apaga_anotacao('banco.db', id_anotacao)
