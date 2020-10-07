from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

from data import poets

poets_2 = []
for index, poet in enumerate(poets):
    poets_2.append((index, poet['name']))

class PoemForm(FlaskForm):
    title = StringField("标题", validators=[DataRequired()])
    poem = TextAreaField("正文", validators=[DataRequired()])
    poet = SelectField("作者", choices=poets_2)
    submit = SubmitField("提交")
