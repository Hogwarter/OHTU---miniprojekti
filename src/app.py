from flask import Flask, redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.book_repository import get_books, get_all_books, generate_book_reference
from repositories.article_repository import get_articles, get_all_articles, generate_articles_reference
from repositories.inproceedings_repository import get_inproceedings, get_all_inproceedings, generate_inproceedings_reference
from config import app, db, test_env
from db_helper import reset_db

@app.route("/")
def index():
    reset_db()
    books = get_all_books()
    articles = get_all_articles()
    inproceedings = get_all_inproceedings()
    return render_template("index.html", books=books, articles=articles, inproceedings=inproceedings) 

@app.route("/book_form")
def new_book():
    return render_template("book_form.html")
    
@app.route("/article_form")
def new_article():
    return render_template("article_form.html")

@app.route("/inproceedings_form")
def new_inproceeding():
    return render_template("inproceedings_form.html")


@app.route("/new_reference", methods=["POST"])
def new_reference():
    ref_type = request.form.get("ref_type")
    if ref_type == "book":
        return render_template("book_form.html") 
    if ref_type == "article":
        return render_template("article_form.html") 
    if ref_type == "inproceedings":
        return render_template("inproceedings_form.html") 
    else:
        return "Invalid reference type", 400


def generate_latex_reference(ref_type, citekey, author, title, publisher, address, year):
    return f"""@{ref_type}{{{citekey},
  author    = "{author}",
  title     = "{title}",
  publisher = "{publisher}",
  address   = "{address}",
  year      = {year}
}}"""

@app.route("/generate_book_reference", methods=["POST", "GET"])
def generate_book_reference_route():
    try:
        citekey = request.form.get("citekey")
        author = request.form.get("author")
        title = request.form.get("title")
        publisher = request.form.get("publisher")
        address = request.form.get("address")
        year = request.form.get("year")
    except Exception:
        return "Error", 500
    latex_reference = generate_latex_reference("book", citekey, author, title, publisher, address, year)
    generate_book_reference(citekey, author, title, publisher, address, year)

    return redirect("/")#f"<pre>{latex_reference}</pre>"


@app.route("/generate_articles_reference", methods=["POST", "GET"])
def generate_articles_reference_route():
    try:
        citekey = request.form.get("citekey")
        author = request.form.get("author")
        title = request.form.get("title")
        publisher = request.form.get("publisher")
        address = request.form.get("address")
        year = request.form.get("year")
    except Exception:
        return "Error", 500
    latex_reference = generate_latex_reference("article", citekey, author, title, publisher, address, year)
    generate_articles_reference(citekey, author, title, publisher, address, year)

    return redirect("/")#f"<pre>{latex_reference}</pre>"

@app.route("/generate_inproceedings_reference", methods=["POST", "GET"])
def generate_inproceedings_reference_route():
    try: 
        citekey = request.form.get("citekey")
        author = request.form.get("author")
        title = request.form.get("title")
        publisher = request.form.get("publisher")
        address = request.form.get("address")
        year = request.form.get("year")
    except Exception:
        return "Error", 500
    
    latex_reference = generate_latex_reference("inproceedings", citekey, author, title, publisher, address, year)
    generate_inproceedings_reference(citekey, author, title, publisher, address, year)

    return redirect("/")#f"<pre>{latex_reference}</pre>"


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
    

