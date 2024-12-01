from config import db
from sqlalchemy.sql import text

def get_books(citekey):
    sql = text("SELECT * FROM books WHERE citekey = :citekey")
    books = db.session.execute(sql, {"citekey": citekey}).fetchall()
    return books 

def get_all_books():
    sql = text("SELECT citekey, author, title, publisher, address, year FROM books")
    result = db.session.execute(sql)
    books = result.fetchall()
    return books

def save_book_reference(citekey, author, title, publisher, address, year):
    try:
        sql = text(""" 
            INSERT INTO books (citekey, author, title, publisher, address, year) 
            VALUES (:citekey, :author, :title, :publisher, :address, :year)
        """)
        db.session.execute(sql, { 
            "citekey": str(citekey), 
            "author": str(author), 
            "title": str(title), 
            "publisher": str(publisher), 
            "address": str(address), 
            "year": int(year) 
        })
        db.session.commit()
        return print("DONEEEE")
    except Exception as e:
        print(f"Error: {e}")
        return print("Voi voi taas.")
    

