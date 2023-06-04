import sqlite3


def connect():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute(
        "create table if not exists books (id integer primary key,title text,author text,year integer,ISBN integer);")
    connection.commit()
    connection.close()


def insert(title, author, year, ISBN):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("insert into books values (NULL,?,?,?,?)",
                   (title, author, year, ISBN))
    connection.commit()
    connection.close()


def view():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("select * from books")
    rows = cursor.fetchall()
    connection.close()
    return rows


def search(title="", author="", year="", ISBN=""):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("select * from books where title=? or author=? or year=? or ISBN=?",
                   (title, author, year, ISBN))
    rows = cursor.fetchall()
    connection.close()
    return rows


def delete(id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("delete from books where id=?", (id,))
    connection.commit()
    connection.close()


def update(id, title, author, year, ISBN):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("update books set title=?,author=?,year=?,ISBN=? where id=?",
                   (title, author, year, ISBN, id))
    connection.commit()
    connection.close()
connect()
