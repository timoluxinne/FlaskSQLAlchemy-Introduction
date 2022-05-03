from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://timoh@localhost:3306/testdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app) 


engine = db.create_engine("mysql://root:timoh@localhost:3306/testdb", {})

connection = engine.connect()
metadata = db.MetaData()

testtbl = db.Table("testtbl", metadata, autoload=True, autoload_with=engine)

query = db.select(people)

stmt = connection.execute(query)
ResultSet = stmt.fetchall()

for rs in ResultSet:
    print(rs)