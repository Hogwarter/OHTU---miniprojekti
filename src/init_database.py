import db, app

application = app
application.app_context().push()

def create_table_books():
    db.session.execute("""        
        CREATE TABLE books (
            citekey TEXT,
            author TEXT,
            title TEXT,
            publisher TEXT,
            address TEXT,
            year INTEGER
        );""")
    db.session.commit()

def initialize_database():
    create_table_books()

if __name__ == "__main__":
    initialize_database()