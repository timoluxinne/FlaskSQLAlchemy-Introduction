## Connection to sqlite

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://db.sqlite3"

#### Using python Interactive for sqlite
engine = db.create_engine("sqlite:///table.sqlite")

## Connection to mysql
engine = db.create_engine("mysql://username:password@localhost:port/dbname", {})

connection = engine.connect()
metadata = db.MetaData()

people = db.Table("people", metadata, autoload=True, autoload_with=engine)

query = db.select(people)

stmt = connection.execute(query)
ResultSet = stmt.fetchall()

for rs in ResultSet:
    print(rs)