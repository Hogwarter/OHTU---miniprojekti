from config import db
from sqlalchemy import text

from entities.todo import Todo

def get_books():
    result = db.session.execute(text("SELECT * FROM books"))
    books = result.fetchall()
    return books 

#def set_done(todo_id):
#    sql = text("UPDATE todos SET done = TRUE WHERE id = :id")
#    db.session.execute(sql, { "id": todo_id })
#    db.session.commit()

def generate_book_reference(citekey, author, title, publisher, address, year):
    sql = text("INSERT INTO books (citekey, author, title, publisher, address, year) VALUES (:citekey, author, title, publisher, address, year)")
    db.session.execute(sql, { "content": citekey, author, title, publisher, address, year })
    db.session.commit()
    return
