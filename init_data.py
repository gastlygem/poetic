# To be used in flask shell to add data

from data import poems, poets
for poet in poets:
    pt = Poet(name=poet['name'], dynasty=poet['dynasty'])
    db.session.add(pt)

db.session.commit()

for poem in poems:
    pm = Poem(title=poem['title'], poem=poem['poem'], poet_id=poem["poet_id"]+1)
    db.session.add(pm)

db.session.commit()
