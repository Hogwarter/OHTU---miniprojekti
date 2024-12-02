from config import db, app
from sqlalchemy import text

table_name = "todo"

def table_exists(name):
  sql_table_existence = text(
    "SELECT EXISTS ("
    "  SELECT 1"
    "  FROM information_schema.tables"
    f" WHERE table_name = '{name}' AND table_schema = 'public'"
    ")"
  )

  print(f"Checking if table {name} exists")
  print(sql_table_existence)

  result = db.session.execute(sql_table_existence, {"name":name})
  #return result.fetchall()[0][0]
  return result.scalar()

def reset_db():
    with app.app_context():
        tables = ["books", "articles", "inproceedings"]
        for table in tables:
            print(f"Dropping table {table} if exists")
            db.session.execute(text(f"DROP TABLE IF EXISTS {table};"))
        
        print("Recreating tables")
        db.session.execute(text("""
            CREATE TABLE books (
                citekey TEXT NOT NULL,
                author TEXT NOT NULL,
                title TEXT NOT NULL,
                publisher TEXT NOT NULL,
                address TEXT NOT NULL,
                year INTEGER NOT NULL
            );
        """))
        db.session.execute(text("""
            CREATE TABLE articles (
                citekey TEXT NOT NULL,
                author TEXT NOT NULL,
                title TEXT NOT NULL,
                journal TEXT NOT NULL,
                volume TEXT NOT NULL,
                year INTEGER NOT NULL,
                pages TEXT NOT NULL
            );
        """))
        db.session.execute(text("""
            CREATE TABLE inproceedings (
                citekey TEXT NOT NULL,
                author TEXT NOT NULL,
                title TEXT NOT NULL,
                booktitle TEXT NOT NULL,
                publisher TEXT NOT NULL,
                pages TEXT NOT NULL,
                year INTEGER NOT NULL
            );
        """))
        db.session.commit()

def setup_db():
  if table_exists(table_name):
    print(f"Table {table_name} exists, dropping")
    sql = text(f"DROP TABLE {table_name}")
    db.session.execute(sql)
    db.session.commit()

  print(f"Creating table {table_name}")
  sql = text(
    f"CREATE TABLE {table_name} ("
    "  id SERIAL PRIMARY KEY, "
    "  content TEXT NOT NULL,"
    "  done BOOLEAN DEFAULT FALSE"
    ")"
  )

  db.session.execute(sql)
  db.session.commit()

if __name__ == "__main__":
    with app.app_context():
      reset_db()
      setup_db()
