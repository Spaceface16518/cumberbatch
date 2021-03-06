import datetime
import random

from flask import flash, Flask, redirect, render_template, \
    request, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import words

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Entry(db.Model):
    __tablename__ = 'entry'

    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(30), nullable=False)
    last = db.Column(db.String(30), nullable=False)
    liked = db.Column(db.Boolean, nullable=False)
    created = db.Column(db.DateTime, nullable=False,
                        default=datetime.datetime.now())

    def __repr__(self):
        return f'{self.first.title()} {self.last.title()}'


db.create_all()


@app.route('/')
def landing():
    first = random.choice(words.firsts)
    last = random.choice(words.lasts)
    return render_template('index.html', first=first.title(), last=last.title())


@app.route('/vote', methods=['POST'])
def vote():
    score = int(request.form['score'])
    was_liked = score > 0
    first = request.form['first']
    last = request.form['last']
    if score != 0:
        entry = Entry(first=first, last=last,
                      liked=was_liked)
        db.session.add(entry)
        db.session.commit()
        flash(f'You {"liked" if was_liked else "disliked"} "{first} {last}"')
    return redirect(url_for('landing'), code=303)


@app.route('/liked')
def liked():
    entries = Entry.query.order_by(Entry.created).limit(10).all()
    return render_template('liked.html', entries=entries)


if __name__ == '__main__':
    app.run()
