from flask import Flask, redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.book_repository import get_books, get_all_books, generate_book_referencee
from config import app, test_env
from util import validate_todo

@app.route("/")
def index():
    books = get_all_books()
    return render_template("index.html", books=books, unfinished="some value") 

@app.route("/book_form")
def new():
    return render_template("book_form.html")
    


@app.route("/new_reference", methods=["POST"])
def new_reference():
    ref_type = request.form.get("ref_type")
    if ref_type == "book":
        return render_template("book_form.html") 
    else:
        return "Invalid reference type", 400

@app.route("/generate_book_reference", methods=["POST", "GET"])
def generate_book_reference():
    citekey = request.form.get("citekey")
    author = request.form.get("author")
    title = request.form.get("title")
    publisher = request.form.get("publisher")
    address = request.form.get("address")
    year = request.form.get("year")

    latex_reference = f"""@book{{{citekey},
  author    = "{author}",
  title     = "{title}",
  publisher = "{publisher}",
  address   = "{address}",
  year      = {year}
}}"""
    generate_book_referencee(citekey, author, title, publisher, address, year)

    return redirect("/")#f"<pre>{latex_reference}</pre>"


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
    

