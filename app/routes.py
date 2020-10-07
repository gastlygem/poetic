from app.forms import PoemForm
from flask import flash, redirect, render_template, url_for
from app import app, db

from app.models import Poet, Poem

@app.route("/")
@app.route("/index")
def index():
    all_poems = Poem.query.all()
    return render_template("index.html", title="诗歌列表", poems=all_poems)

@app.route("/add_poem", methods=["GET", "POST"])
def add_poem():
    form = PoemForm()
    if form.validate_on_submit():
        db.session.add(Poem(title=form.title.data, poem=form.poem.data, poet_id=int(form.poet.data)))
        db.session.commit()
        flash(f"诗歌《{form.title.data}》添加成功")
        return redirect(url_for('index'))
    return render_template("add_poem.html", title="添加诗", form=form)
