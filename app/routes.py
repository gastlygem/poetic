from flask import render_template
from app import app

from data import poems, poets

@app.route("/")
@app.route("/index")
def index():
    all_poems = []
    for poem in poems:
        poem2 = poem.copy()
        poem2['poet'] = poets[poem2['poet_id']]
        all_poems.append(poem2)
    return render_template("index.html", title="诗歌列表", poems=all_poems)
