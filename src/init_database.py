from config import db, app
from sqlalchemy import text
from db_helper import reset_db


application = app
application.app_context().push()

def create_table_books():
    db.session.execute(text("""        
        CREATE TABLE IF NOT EXISTS books (
            citekey TEXT NOT NULL,
            author TEXT NOT NULL,
            title TEXT NOT NULL,
            publisher TEXT NOT NULL,
            address TEXT NOT NULL,
            year INTEGER NOT NULL
        );"""))
    db.session.commit()

def create_table_articles():
    db.session.execute(text("""        
        CREATE TABLE IF NOT EXISTS articles (
            citekey TEXT NOT NULL,
            author TEXT NOT NULL,
            title TEXT NOT NULL,
            journal TEXT NOT NULL,
            volume TEXT NOT NULL,
            year INTEGER NOT NULL,
            pages TEXT NOT NULL
        );"""))
    db.session.commit()

def create_table_inproceedings():
    db.session.execute(text("""        
        CREATE TABLE IF NOT EXISTS inproceedings (
            citekey TEXT NOT NULL,
            author TEXT NOT NULL,
            title TEXT NOT NULL,
            booktitle TEXT NOT NULL,
            publisher TEXT NOT NULL,
            pages TEXT NOT NULL,
            year INTEGER NOT NULL
        );"""))
    db.session.commit()


def initialize_database():
    with app.app_context():
        create_table_books()
        create_table_articles()
        create_table_inproceedings()
        reset_db()

if __name__ == "__main__":
    initialize_database()