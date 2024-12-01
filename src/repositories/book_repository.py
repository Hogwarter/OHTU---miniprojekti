from config import db
from sqlalchemy.sql import text

#from entities.todo import Todo

def get_books(citekey):
    sql = ("SELECT * FROM books")
    books = db.session.execute(sql, {"citekey": citekey}).result.fetchall()
    return books 

def get_all_books():
    sql = text("SELECT citekey, author, title, publisher, address, year FROM books")
    result = db.session.execute(sql)
    books = result.fetchall()
    return books

#def set_done(todo_id):
#    sql = text("UPDATE todos SET done = TRUE WHERE id = :id")
#    db.session.execute(sql, { "id": todo_id })
#    db.session.commit()

def generate_book_reference(citekey, author, title, publisher, address, year):
    sql = text(""" 
        INSERT INTO books (citekey, author, title, publisher, address, year) 
        VALUES (:citekey, :author, :title, :publisher, :address, :year)
    """)
    db.session.execute(sql, { 
        "citekey": citekey, 
        "author": author, 
        "title": title, 
        "publisher": publisher, 
        "address": address, 
        "year": year 
    })
    db.session.commit()
    return
