from config import db
from sqlalchemy.sql import text

def get_articles(citekey):
    sql = ("SELECT * FROM articles WHERE citekey = :citekey")
    articles = db.session.execute(sql, {"citekey": citekey}).fetchall()
    return articles 

def get_all_articles():
    sql = text("SELECT citekey, author, title, publisher, address, year FROM articles")
    result = db.session.execute(sql)
    articles = result.fetchall()
    return articles

def save_article_reference(citekey, author, title, publisher, address, year):
    try:
        sql = text(""" 
            INSERT INTO articles (citekey, author, title, publisher, address, year) 
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

