"""Contains all routes of the app"""

from flask import flash, jsonify, redirect, render_template, request

from config import app, test_env
from db_helper import clear_robot_sources, filter_articles, reset_db
from repositories.article_repository import create_article, set_done  # ,get_todos,
from util import (
    validate_author,
    validate_citekey,
    validate_journal,
    validate_name,
    validate_number,
    validate_volume,
    validate_year,
)


@app.route("/")
@app.route("/<int:page>")
def index(page=1):
    """landing page"""
    page_size = 20

    # todos = get_todos()
    # unfinished = len([todo for todo in todos if not todo.done])

    search_query = request.args.get("search", "")

    material = request.args.get("material_type", "")
    keyword = request.args.get("keyword", "")
    year = request.args.get("year", "")
    search_term = request.args.get("search", "")

    if year:
        try:
            year = int(year)
        except:
            year = None

    # reversed list of the sources
    records = list(reversed(filter_articles(material, keyword, year, search_term)))

    all_articles = len(records)
    page_count = max((all_articles - 1) // page_size + 1, 1)

    if page < 1:
        return redirect("/1")
    if page > page_count:
        return redirect("/" + str(page_count))

    start = (page - 1) * page_size
    end = start + page_size
    records_page = records[start:end]

    return render_template(
        "index.html",
        records=records_page,
        page=page,
        page_count=page_count,
        search_query=search_query,
        columns=[
            "citekey",
            "author",
            "name",
            "journal",
            "year",
            "volume",
            "number",
            "urldate",
            "url",
        ],
    )


@app.route("/add_article")
def add_article():
    """route for displaying add_article.html"""
    return render_template("add_article.html")


@app.route("/create_article", methods=["POST"])
def try_create_article():
    """create article route"""
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
        validate_citekey(citekey)
        create_article(
            citekey, author, year, name, journal, volume, number, urldate, url
        )
        flash("Source added successfully")
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("add_article.html")


@app.route("/toggle_todo/<todo_id>", methods=["POST"])
def toggle_todo(todo_id):
    """todo on/off"""
    set_done(todo_id)
    return redirect("/")


# removes the sources added by the robot-tests
if test_env:

    @app.route("/delete_robot_sources_db")
    def delete_robot_sources():
        """URL for removing sources added by robot tests"""
        clear_robot_sources()
        flash("Robot sources deleted")
        return redirect("/")


# testausta varten oleva reitti
if test_env:

    @app.route("/reset_db")
    def reset_database():
        """reset database wrapper"""
        reset_db()
        return jsonify({"message": "db reset"})
