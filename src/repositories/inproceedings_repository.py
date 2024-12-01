from config import db
from sqlalchemy.sql import text

#from entities.todo import Todo

def get_inproceedings(citekey):
    sql = ("SELECT * FROM inproceedings")
    inproceedings = db.session.execute(sql, {"citekey": citekey}).result.fetchall()
    return inproceedings 

def get_all_inproceedings():
    sql = text("SELECT citekey, author, title, publisher, address, year FROM inproceedings")
    result = db.session.execute(sql)
    inproceedings = result.fetchall()
    return inproceedings

def generate_inproceedings_reference(citekey, author, title, publisher, address, year):
    sql = text(""" 
        INSERT INTO inproceedings (citekey, author, title, publisher, address, year) 
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