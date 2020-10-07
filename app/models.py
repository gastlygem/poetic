from app import db


class Poem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    poem = db.Column(db.String(500))
    poet_id = db.Column(db.Integer, db.ForeignKey('poet.id'))

    def __repr__(self):
        return f'<Poem {self.title}>'


class Poet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    dynasty = db.Column(db.String(64))
    poems = db.relationship('Poem', backref="poet", lazy="dynamic")

    def __repr__(self):
        return f'<Poet {self.name}>'
