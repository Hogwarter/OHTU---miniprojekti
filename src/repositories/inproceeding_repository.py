from config import db
from sqlalchemy.sql import text

def get_inproceedings(citekey):
    sql = text("SELECT * FROM inproceedings WHERE citekey = :citekey")
    inproceedings = db.session.execute(sql, {"citekey": citekey}).fetchall()
    return inproceedings 

def get_all_inproceedings():
    sql = text("SELECT citekey, author, title, publisher, address, year FROM inproceedings")
    result = db.session.execute(sql)
    inproceedings = result.fetchall()
    return inproceedings

def save_inproceeding_reference(citekey, author, title, publisher, address, year):
    try:
        sql = text(""" 
            INSERT INTO inproceedings (citekey, author, title, publisher, address, year) 
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