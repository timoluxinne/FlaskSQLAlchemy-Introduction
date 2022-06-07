import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="mydb",
    user=os.environ['DB_USERNAME'],
    password= os.environ['DB_PASSWORD']
)

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE books(id serial PRIMARY KEY,'
                                'title varchar(150) NOT NULL,'
                                'author varchar(150) NOT NULL,'
                                'pages_num integer NOT NULL,'
                                'review text,'
                                'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                )

cur.execute('INSERT INTO books(title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            (
                'Tim Njoroge',
                'Isaac Muroki',
                864,
                'A new Story'
            )
)

conn.commit()
cur.close()
conn.close()
