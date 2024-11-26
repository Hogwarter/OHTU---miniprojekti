from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.book_repository import get_books, generate_book_reference
from config import app, test_env
from util import validate_todo

@app.route("/")
def index():
    #todos = get_todos()
    #unfinished = len([todo for todo in todos if not todo.done])
    return render_template("index.html") 

@app.route("/book_form")
def new():
    return render_template("book_form.html")

#@app.route("/create_todo", methods=["POST"])
#def todo_creation():
#    content = request.form.get("content")

#    try:
#        validate_todo(content)
#        create_todo(content)
#        return redirect("/")
#    except Exception as error:
#        flash(str(error))
#        return  redirect("/new_todo")

#@app.route("/toggle_todo/<todo_id>", methods=["POST"])
#def toggle_todo(todo_id):
#    set_done(todo_id)
#    return redirect("/")



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

    return redirect("/")#f"<pre>{latex_reference}</pre>"


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
