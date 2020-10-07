from app.forms import PoemForm
from flask import flash, redirect, render_template
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

@app.route("/add_poem", methods=["GET", "POST"])
def add_poem():
    form = PoemForm()
    if form.validate_on_submit():
        poems.append({"title": form.title.data, "poem": form.poem.data, "poet_id": int(form.poet.data)})
        flash(f"诗歌《{form.title.data}》添加成功")
        return redirect('/index')
    return render_template("add_poem.html", title="添加诗", form=form)
