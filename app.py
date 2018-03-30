from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskr.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    people = Person.query.all()
    return render_template("index.html", people = people)

@app.route('/add')
def add():
    return render_template("form.html")

@app.route('/processform', methods=['GET','POST'])
def processform():
    firstname = request.form['first']
    lastname = request.form['last']
    person = Person(firstname,lastname)
    db.session.add(person)
    db.session.commit()
    return redirect(url_for('index'))

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

if __name__ == '__main__':
    app.run()
