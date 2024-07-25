import sqlite3 as sql


def create_tables_database():
    database = sql.connect('Inventory_Storage.db')
    query = database.cursor()

    query.execute('''CREATE TABLE IF NOT EXISTS users
                    (username TEXT UNIQUE,
                    password INTEGER)''')

    query.execute('''CREATE TABLE IF NOT EXISTS products
                    (product_id INTEGER UNIQUE,
                    product_name TEXT,
                    quantity INTEGER,
                    price REAL)''')

    database.commit()

    query.execute("insert into users values ('Sumit', 81015)")
    query.execute("insert into users values ('Robin', 360)")
    query.execute("insert into users values ('Zoro', 110)")
    query.execute('select * from users')
    print(query.fetchall())
    database.commit()
    database.close()


create_tables_database()
