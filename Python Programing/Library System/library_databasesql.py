import sqlite3 as sql
from datetime import datetime

database = sql.connect('library.db')
query = database.cursor()

query.execute('''
CREATE TABLE IF NOT EXISTS users(
              user_id INTEGER PRIMARY KEY,
              name TEXT,
              username TEXT UNIQUE,
              password INTEGER,
              admin INTEGER
              )
''')

query.execute('''
CREATE TABLE IF NOT EXISTS books(
              book_id INTEGER PRIMARY KEY,
              book_name TEXT,
              author TEXT,
              language TEXT
              )
''')

query.execute('''
CREATE TABLE IF NOT EXISTS student_book(
              id INTEGER PRIMARY KEY,
              student_id INTEGER,
              book_id INTEGER,
              book_name TEXT,
              date TEXT,
              FOREIGN KEY (student_id) REFERENCES users(user_id),
              FOREIGN KEY (book_id) REFERENCES books(book_id)
              )
''')

# query.execute(f"INSERT INTO users (name, username, password, admin) VALUES ('Sumit Dubey', 'sumit810', {81015}, {1})")
# query.execute(f"INSERT INTO books VALUES ({45}, 'Python', 'Sumit', 'English')")

query.execute("SELECT * FROM books")
print(query.fetchall())
query.execute("SELECT * FROM users")
print(query.fetchall())
query.execute("SELECT * FROM student_book")
print(query.fetchall())
database.commit()
database.close()
