from config import db, app
from sqlalchemy import text

table_name = "todo"

def table_exists(name):
  sql_table_existence = text(
    "SELECT EXISTS ("
    "  SELECT 1"
    "  FROM information_schema.tables"
    f" WHERE table_name = '{name}'"
    ")"
  )

  print(f"Checking if table {name} exists")
  print(sql_table_existence)

  result = db.session.execute(sql_table_existence)
  return result.fetchall()[0][0]

def reset_db():
  with app.app_context():
        # Droppaa existing table
        db.session.execute(text("DROP TABLE IF EXISTS books;"))
        
        # Recreattaa table
        db.session.execute(text("""        
            CREATE TABLE IF NOT EXISTS books (
                citekey TEXT NOT NULL,
                author TEXT NOT NULL,
                title TEXT NOT NULL,
                publisher TEXT NOT NULL,
                address TEXT NOT NULL,
                year INTEGER NOT NULL
            );"""))
        
        db.session.execute(text("DROP TABLE IF EXISTS articles;"))
        
        # Recreattaa table
        db.session.execute(text("""        
            CREATE TABLE IF NOT EXISTS articles (
                citekey TEXT NOT NULL,
                author TEXT NOT NULL,
                title TEXT NOT NULL,
                publisher TEXT NOT NULL,
                address TEXT NOT NULL,
                year INTEGER NOT NULL
            );"""))
        
        db.session.execute(text("DROP TABLE IF EXISTS inproceedings;"))
        
        # Recreattaa table
        db.session.execute(text("""        
            CREATE TABLE IF NOT EXISTS inproceedings (
                citekey TEXT NOT NULL,
                author TEXT NOT NULL,
                title TEXT NOT NULL,
                publisher TEXT NOT NULL,
                address TEXT NOT NULL,
                year INTEGER NOT NULL
            );"""))

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
      setup_db()
