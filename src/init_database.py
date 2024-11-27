from config import db, app
from sqlalchemy import text


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

def initialize_database():
    with app.app_context(): 
        create_table_books()

if __name__ == "__main__":
    initialize_database()