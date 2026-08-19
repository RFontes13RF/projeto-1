from utils import load_template,add_anotacao, load_data

def index():
    note_template = load_template('components/note.html')
    notes_li = [note_template.format(title=dados[0],content=dados[1]) for dados in load_data('banco.db')]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    return add_anotacao('banco.db', titulo, detalhes)
