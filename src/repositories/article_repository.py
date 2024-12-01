from config import db
from sqlalchemy.sql import text

#from entities.todo import Todo

def get_articles(citekey):
    sql = ("SELECT * FROM articles")
    articles = db.session.execute(sql, {"citekey": citekey}).result.fetchall()
    return articles 

def get_all_articles():
    sql = text("SELECT citekey, author, title, publisher, address, year FROM articles")
    result = db.session.execute(sql)
    articles = result.fetchall()
    return articles

def generate_articles_reference(citekey, author, title, publisher, address, year):
    sql = text(""" 
        INSERT INTO articles (citekey, author, title, publisher, address, year) 
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
