from config import db
from sqlalchemy.sql import text
 
def get_articles(citekey):
    sql = ("SELECT * FROM articles WHERE citekey = :citekey")
    articles = db.session.execute(sql, {"citekey": citekey}).fetchall()
    return articles 

def get_all_articles():
    sql = text("SELECT citekey, author, title, journal, volume, year, pages FROM articles")
    result = db.session.execute(sql)
    articles = result.fetchall()
    return articles

def save_article_reference(citekey, author, title, journal, volume, year, pages):
    try:
        sql = text(""" 
            INSERT INTO articles (citekey, author, title, journal, volume, year, pages) 
            VALUES (:citekey, :author, :title, :journal, :volume, :year, :pages)
        """)
        db.session.execute(sql, { 
            "citekey": str(citekey), 
            "author": str(author), 
            "title": str(title), 
            "journal": str(journal), # journal, volume, pages
            "volume": str(volume), 
            "year": int(year),
            "pages": str(pages)
        })
        db.session.commit()
        return print("DONEEEE")
    except Exception as e:
        print(f"Error: {e}")
        return print("Voi voi taas.")

