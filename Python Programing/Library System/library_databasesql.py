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

# books = [
#     (1, 'To Kill a Mockingbird', 'Harper Lee', 'English'),
#     (2, '1984', 'George Orwell', 'English'),
#     (3, 'The Great Gatsby', 'F. Scott Fitzgerald', 'English'),
#     (4, 'Pride and Prejudice', 'Jane Austen', 'English'),
#     (5, 'Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling', 'English'),
#     (6, 'The Catcher in the Rye', 'J.D. Salinger', 'English'),
#     (7, 'Animal Farm', 'George Orwell', 'English'),
#     (8, 'Jane Eyre', 'Charlotte Brontë', 'English'),
#     (9, 'Brave New World', 'Aldous Huxley', 'English'),
#     (10, 'The Hobbit', 'J.R.R. Tolkien', 'English'),
#     (11, 'Fahrenheit 451', 'Ray Bradbury', 'English'),
#     (12, 'Lord of the Flies', 'William Golding', 'English'),
#     (13, 'The Book Thief', 'Markus Zusak', 'English'),
#     (14, 'The Chronicles of Narnia', 'C.S. Lewis', 'English'),
#     (15, 'The Little Prince', 'Antoine de Saint-Exupéry', 'French'),
#     (16, 'One Hundred Years of Solitude', 'Gabriel García Márquez', 'Spanish'),
#     (17, 'Crime and Punishment', 'Fyodor Dostoevsky', 'Russian'),
#     (18, 'The Brothers Karamazov', 'Fyodor Dostoevsky', 'Russian'),
#     (19, 'Anna Karenina', 'Leo Tolstoy', 'Russian'),
#     (20, 'Don Quixote', 'Miguel de Cervantes', 'Spanish'),
#     (21, 'The Picture of Dorian Gray', 'Oscar Wilde', 'English'),
#     (22, 'War and Peace', 'Leo Tolstoy', 'Russian'),
#     (23, 'Moby Dick', 'Herman Melville', 'English'),
#     (24, 'Les Misérables', 'Victor Hugo', 'French'),
#     (25, 'Gone with the Wind', 'Margaret Mitchell', 'English'),
#     (26, 'Wuthering Heights', 'Emily Brontë', 'English'),
#     (27, 'The Count of Monte Cristo', 'Alexandre Dumas', 'French'),
#     (28, 'The Odyssey', 'Homer', 'Greek'),
#     (29, 'The Divine Comedy', 'Dante Alighieri', 'Italian'),
#     (30, 'The Adventures of Sherlock Holmes', 'Arthur Conan Doyle', 'English'),
#     (31, 'A Tale of Two Cities', 'Charles Dickens', 'English'),
#     (32, 'The Scarlet Letter', 'Nathaniel Hawthorne', 'English'),
#     (33, 'Frankenstein', 'Mary Shelley', 'English'),
#     (34, 'The Three Musketeers', 'Alexandre Dumas', 'French'),
#     (35, 'The Iliad', 'Homer', 'Greek'),
#     (36, 'Dracula', 'Bram Stoker', 'English'),
#     (37, 'The Grapes of Wrath', 'John Steinbeck', 'English'),
#     (38, 'Alice\'s Adventures in Wonderland', 'Lewis Carroll', 'English'),
#     (39, 'The Old Man and the Sea', 'Ernest Hemingway', 'English'),
#     (40, 'The Jungle Book', 'Rudyard Kipling', 'English'),
#     (41, 'Heart of Darkness', 'Joseph Conrad', 'English'),
#     (42, 'The Trial', 'Franz Kafka', 'German'),
#     (43, 'The Stranger', 'Albert Camus', 'French'),
#     (44, 'Slaughterhouse-Five', 'Kurt Vonnegut', 'English'),
#     (45, 'The Sun Also Rises', 'Ernest Hemingway', 'English'),
#     (46, 'A Clockwork Orange', 'Anthony Burgess', 'English'),
#     (47, 'The Road', 'Cormac McCarthy', 'English'),
#     (48, 'For Whom the Bell Tolls', 'Ernest Hemingway', 'English'),
#     (49, 'The Bell Jar', 'Sylvia Plath', 'English'),
#     (50, 'Catch-22', 'Joseph Heller', 'English'),
#     (51, 'A Farewell to Arms', 'Ernest Hemingway', 'English'),
#     (52, 'Walden', 'Henry David Thoreau', 'English'),
#     (53, 'The Lord of the Rings', 'J.R.R. Tolkien', 'English'),
#     (54, 'Beloved', 'Toni Morrison', 'English'),
#     (55, 'Middlemarch', 'George Eliot', 'English'),
#     (56, 'Mrs. Dalloway', 'Virginia Woolf', 'English'),
#     (57, 'A Passage to India', 'E.M. Forster', 'English'),
#     (58, 'Robinson Crusoe', 'Daniel Defoe', 'English'),
#     (59, 'Emma', 'Jane Austen', 'English'),
#     (60, 'Great Expectations', 'Charles Dickens', 'English'),
#     (61, 'The Canterbury Tales', 'Geoffrey Chaucer', 'Middle English'),
#     (62, 'The Master and Margarita', 'Mikhail Bulgakov', 'Russian'),
#     (63, 'The Wind in the Willows', 'Kenneth Grahame', 'English'),
#     (64, 'Ulysses', 'James Joyce', 'English'),
#     (65, 'Oliver Twist', 'Charles Dickens', 'English'),
#     (66, 'Gulliver\'s Travels', 'Jonathan Swift', 'English'),
#     (67, 'A Doll\'s House', 'Henrik Ibsen', 'Norwegian'),
#     (68, 'The Alchemist', 'Paulo Coelho', 'Portuguese'),
#     (69, 'The Metamorphosis', 'Franz Kafka', 'German'),
#     (70, 'The Sound and the Fury', 'William Faulkner', 'English'),
#     (71, 'Of Mice and Men', 'John Steinbeck', 'English'),
#     (72, 'Invisible Man', 'Ralph Ellison', 'English'),
#     (73, 'The Joy Luck Club', 'Amy Tan', 'English'),
#     (74, 'Things Fall Apart', 'Chinua Achebe', 'English'),
#     (75, 'The Color Purple', 'Alice Walker', 'English'),
#     (76, 'The Handmaid\'s Tale', 'Margaret Atwood', 'English'),
#     (77, 'The Stranger Beside Me', 'Ann Rule', 'English'),
#     (78, 'The Road Less Traveled', 'M. Scott Peck', 'English'),
#     (79, 'The Art of War', 'Sun Tzu', 'Chinese'),
#     (80, 'The Help', 'Kathryn Stockett', 'English'),
#     (81, 'The Da Vinci Code', 'Dan Brown', 'English'),
#     (82, 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Swedish'),
#     (83, 'The Shack', 'William P. Young', 'English'),
#     (84, 'The Lovely Bones', 'Alice Sebold', 'English'),
#     (85, 'The Hunger Games', 'Suzanne Collins', 'English'),
#     (86, 'The Fault in Our Stars', 'John Green', 'English'),
#     (87, 'The Martian', 'Andy Weir', 'English'),
#     (88, 'Divergent', 'Veronica Roth', 'English'),
#     (89, 'Gone Girl', 'Gillian Flynn', 'English'),
#     (90, 'The Goldfinch', 'Donna Tartt', 'English'),
#     (91, 'A Game of Thrones', 'George R.R. Martin', 'English'),
#     (92, 'The Help', 'Kathryn Stockett', 'English'),
#     (93, 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Swedish'),
#     (94, 'The Shack', 'William P. Young', 'English'),
#     (95, 'The Lovely Bones', 'Alice Sebold', 'English'),
#     (96, 'The Hunger Games', 'Suzanne Collins', 'English'),
#     (97, 'The Fault in Our Stars', 'John Green', 'English'),
#     (98, 'The Martian', 'Andy Weir', 'English'),
#     (99, 'Divergent', 'Veronica Roth', 'English'),
#     (100, 'Gone Girl', 'Gillian Flynn', 'English')
# ]


# # query.execute(f"INSERT INTO users (name, username, password, admin) VALUES ('Sumit Dubey', 'sumit810', {81015}, {1})")
# n = 0
# for book in books:
#     query.execute("INSERT INTO books VALUES (?, ?, ?, ?)", book)
#     n += 1
# print(f"{n} rows inserted")    

# query.execute("SELECT * FROM books")
# print(query.fetchall())
query.execute("SELECT * FROM users")
print(query.fetchall())
query.execute("SELECT * FROM student_book")
for data in query.fetchall():
    print(data)
database.commit()
database.close()
