"""Contains all routes of the app"""

from flask import flash, redirect, render_template, send_file, url_for, request, Response

from bib_generating import generate_bib_browser, generate_bib_file
from config import app, test_env
from db_helper import (
    clear_robot_sources,
    filter_articles,
    get_article,
    modify_article,
    remove_article_from_database,
    add_test_source
)
from repositories.all_citations_repository import fetch_all_citations
from repositories.article_repository import create_article
from util import validate_citekey


@app.route("/")
@app.route("/<int:page>")
def index(page=1):
    """Landing page for the application, displays a paginated list of articles.

    Args:
        page (int): The current page number (default is 1).

    Returns:
        str: Rendered HTML template for the landing page.
    """
    page_size = 20

    search_query = request.args.get("search", "")

    material = request.args.get("material_type", "")
    keyword = request.args.get("keyword", "")
    year = request.args.get("year", "")
    search_term = request.args.get("search", "")

    if year:
        try:
            year = int(year)
        except ValueError:
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


@app.route("/add_inproceeding")
def add_inproceeding():
    """Route for displaying the 'add_inproceeding.html' form.

    Returns:
        str: Rendered HTML template for adding a new inproceeding.
    """
    return render_template("add_inproceeding.html")

@app.route("/add_book")
def add_book():
    """Route for displaying the 'add_book.html' form.

    Returns:
        str: Rendered HTML template for adding a new book.
    """
    return render_template("add_book.html")

@app.route("/add_article")
def add_article():
    """Route for displaying the 'add_article.html' form.

    Returns:
        str: Rendered HTML template for adding a new article.
    """
    return render_template("add_article.html")


@app.route("/create_article", methods=["POST"])
def try_create_article():
    """Route for creating a new article.

    Returns:
        str: Redirects to the landing page or back to the form on error.
    """
    # pylint: disable=broad-exception-caught

    citekey = request.form.get("citekey")
    author = request.form.get("author")
    year = request.form.get("year")
    name = request.form.get("name")
    journal = request.form.get("journal")
    volume = request.form.get("volume")
    number = request.form.get("number")
    urldate = request.form.get("urldate")
    url = request.form.get("url")

    # Required field validation
    required_fields = {
        "Cite key": citekey,
        "Author": author,
        "Publication year": year,
        "Article name": name,
        "Journal": journal
    }

    for field_name, value in required_fields.items():
        if not value or value.strip() == "":
            flash(f"{field_name} is required.")
            return redirect("add_article")

    try:
        validate_citekey(citekey)
        create_article(
            citekey, author, year, name, journal, volume, number, urldate, url
        )
        flash("Source added successfully")
        return redirect("add_article")
    except Exception as error:
        flash(str(error))
        return redirect("add_article")



@app.route("/edit_article/<citekey>")
def edit_article(citekey):
    """Renders the edit article template."""

    article = get_article(citekey)
    return render_template("edit_article.html", article=article)

@app.route("/modified_article/<citekey>", methods=["POST"])
def modified_article(citekey):
    """Route for modifying an existing article.

    Args:
        citekey (str): The unique identifier for the article.

    Returns:
        str: Redirects to the landing page or back to the form on error.
    """
    # pylint: disable=broad-exception-caught, unexpected-keyword-arg, R0801

    fields = [
        "citekey",
        "author",
        "year",
        "name",
        "journal",
        "volume",
        "number",
        "urldate",
        "url",
    ]

    modified_fields = {field: request.form.get(field) or None for field in fields}

    try:
        modify_article(citekey, modified_fields)
        flash("Article edited successfully")
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect(url_for("edit_article"), citekey=citekey)


@app.route("/remove_article/<citekey>", methods=["GET", "POST"])
def remove_article(citekey):
    """Route for displaying and handling the removal of an article.

    Args:
        citekey (str): The unique identifier for the article.

    Returns:
        str: Rendered HTML template for removing an article or redirect after removal.
    """
    if request.method == "GET":
        article = get_article(citekey)
        return render_template("remove_article.html", article=article, citekey=citekey)

    if request.method == "POST":
        if "remove" in request.form:
            remove_article_from_database(citekey)
        return redirect("/")

    return render_template("error")

@app.route("/bib_view")
def bib_view():
    """Route for viewing bib in the browser"""
    return Response(generate_bib_browser(), mimetype="text/plain")

@app.route("/bib_file")
def bib_file():
    """Route for downloading a .bib file"""
    generate_bib_file()
    path = "../citations.bib"
    return send_file(path, as_attachment=True)

if test_env:

    @app.route("/delete_robot_sources_db")
    def delete_robot_sources():
        """URL for removing sources added by robot tests.

        Returns:
            str: Redirects to the landing page after deletion.
        """
        clear_robot_sources()
        flash("Robot sources deleted")
        return redirect("/")

    @app.route("/citations")
    def citations():
        """Route for fetching all citations.

        Returns:
            list: A list of citations.
        """
        citations_for_web = fetch_all_citations()

        return citations_for_web

    @app.route("/test_source")
    def test_source():
        """Adds a random source to the database for testing"""

        add_test_source()

        return redirect("/")
