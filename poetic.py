from app import app, db
from app.models import Poem, Poet

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Poem': Poem, 'Poet': Poet}
