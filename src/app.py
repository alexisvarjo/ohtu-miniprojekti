from flask import redirect, render_template, request, jsonify, flash
from db_helper import search_articles, reset_db
from repositories.article_repository import get_todos, create_article, set_done
from config import app, test_env
from util import validate_author, validate_volume, validate_journal, validate_name, validate_number, validate_year

@app.route("/")
def index():
    todos = get_todos()
    unfinished = len([todo for todo in todos if not todo.done])

    search_query = request.args.get("search", "")
    records = search_articles(search_query)  # haku suoritetaan aina

    return render_template(
        "index.html",
        todos=todos,
        unfinished=unfinished,
        search_query=search_query,
        records=records,
        columns=["citekey","author","name","journal","year","volume","number","urldate","url"]
    )

@app.route("/add_article")
def add_article():
    return render_template("add_article.html")

@app.route("/create_article", methods=["POST"])
def create_article():
    citekey = request.form.get("citekey")
    author = request.form.get("author")
    year = request.form.get("year")
    name = request.form.get("name")
    journal = request.form.get("journal")
    volume = request.form.get("volume")
    number = request.form.get("number")
    urldate = request.form.get("urldate")
    url = request.form.get("url")

    try:
        validate_author(author)
        validate_year(year)
        validate_name(name)
        validate_journal(journal)
        validate_volume(volume)
        validate_number(number)
        create_article(citekey, author, year, name, journal, volume, number, urldate, url)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("add_article.html")

@app.route("/toggle_todo/<todo_id>", methods=["POST"])
def toggle_todo(todo_id):
    set_done(todo_id)
    return redirect("/")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
