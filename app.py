from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app) 

class User(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    date_joined = db.Column(db.Date, default=datetime.utcnow())

    def __repr__(self):
        return f"<User: {self.name}>"

u1 = User()
u1.id=1
u1.name='tim'
u1.email='tim@gmail.com'
u1.date_joined=datetime.now()



@app.route("/")
def hello():
    return f"Hello world {u1}"

@app.route("/about")
def about():
    return "This is about page"
