from flask import Flask, redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.book_repository import get_books, get_all_books, save_book_reference
from repositories.article_repository import get_articles, get_all_articles, save_article_reference
from repositories.inproceeding_repository import get_inproceedings, get_all_inproceedings, save_inproceeding_reference
from config import app, db, test_env
from db_helper import reset_db

@app.route("/")
def index():
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

@app.route("/inproceeding_form")
def new_inproceeding():
    return render_template("inproceeding_form.html")

@app.route("/show_latex", methods=["GET", "POST"])
def show_latex():
    books = get_all_books()
    articles = get_all_articles()
    inproceedings = get_all_inproceedings()
    return render_template("latex_form.html", books=books, articles=articles, inproceedings=inproceedings)

@app.route("/new_reference", methods=["POST"])
def new_reference():
    ref_type = request.form.get("ref_type")
    if ref_type == "book":
        return render_template("book_form.html") 
    if ref_type == "article":
        return render_template("article_form.html") 
    if ref_type == "inproceeding":
        return render_template("inproceeding_form.html") 
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
    save_book_reference(citekey, author, title, publisher, address, year)

    return redirect("/")#f"<pre>{latex_reference}</pre>"


@app.route("/generate_article_reference", methods=["POST", "GET"])
def generate_article_reference():
    citekey = request.form.get("citekey")
    author = request.form.get("author")
    title = request.form.get("title")
    journal = request.form.get("journal")
    volume = request.form.get("volume")
    year = request.form.get("year")
    pages = request.form.get("pages")

    latex_reference = f"""@article{{{citekey},
  author    = "{author}",
  title     = "{title}",
  journal = "{journal}",
  volume   = "{volume}",
  year      = {year},
  pages      = "{pages}"
}}"""
    save_article_reference(citekey, author, title, journal, volume, year, pages)

    return redirect("/")#f"<pre>{latex_reference}</pre>"

@app.route("/generate_inproceeding_reference", methods=["POST", "GET"])
def generate_inproceeding_reference():
    citekey = request.form.get("citekey")
    author = request.form.get("author")
    title = request.form.get("title")
    booktitle = request.form.get("booktitle")
    publisher = request.form.get("publisher")
    pages = request.form.get("pages")
    year = request.form.get("year")

    latex_reference = f"""@inproceeding{{{citekey},
  author    = "{author}",
  title     = "{title}",
  booktitle     = "{booktitle}",
  publisher = "{publisher}",
  pages   = "{pages}",
  year      = {year}
}}"""
    save_inproceeding_reference(citekey, author, title, booktitle, publisher, pages, year)

    return redirect("/")#f"<pre>{latex_reference}</pre>"

@app.route("/delete_entry/<ref_type>/<citekey>", methods=["POST"])
def delete_entry(ref_type, citekey):
    citekey = request.form.get("citekey")
    try:
        if ref_type == "book":
            sql = "DELETE FROM books WHERE citekey = :citekey"
        elif ref_type == "article":
            sql = "DELETE FROM articles WHERE citekey = :citekey"
        elif ref_type == "inproceeding":
            sql = "DELETE FROM inproceedings WHERE citekey = :citekey"
        else:
            flash("Invalid reference type.", "error")
            return redirect("/")
        
        db.session.execute(sql, {"citekey": citekey})
        db.session.commit()
    except Exception as e:
        app.logger.error(f"Error: {e}")
    return redirect("/")


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
    

