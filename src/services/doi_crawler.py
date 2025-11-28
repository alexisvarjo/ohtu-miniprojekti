"""Module for adding citations with a DOI"""

import requests

from db_helper import check_if_citekey_exists
from repositories.all_citations_repository import create_citation
from repositories.article_repository import create_article
from repositories.book_repository import create_book
from repositories.inproceeding_repository import create_inproceeding

ARTICLE_TYPES = [
    "article-journal",
    "article-magazine",
    "article-newspaper",
    "article",
    "journal-article",
]

BOOK_TYPES = [
    "book",
    "book-chapter",
    "edited-book"
]

INPROCEEDING_TYPES = [
    "proceedings-article",
    "conference-paper"
]

def _fetch_doi_citation(doi):
    """Fetches citation information with a DOI and turns the information into a JSON"""
    try:
        response = requests.get(
            f"https://doi.org/{doi}",
            headers={"Accept": "application/vnd.citationstyles.csl+json"},
            timeout=10,
        )
    except:
        return ("The URL doesn't exist", None)
    
    if response.status_code == 404:
        return ("The requested DOI doesn't exist", None)
    
    try:
        data = response.json()
    except:
        return ("Error", None)
    
    return ("success", data)

def _parse_add_article(data, citekey, tag):
    """Parses an article DOI"""
    authors = []
    for author in data["author"]:
        given = author.get("given", "")
        family = author.get("family", "")
        authors.append(f"{given} {family}")
    author = ", ".join(authors)

    year = data["issued"]["date-parts"][0][0]
    name = data.get("title", "")
    journal = data.get("container-title", "")
    volume = data.get("volume", "")
    number = data.get("issue", "")
    urldate = ""
    url = data.get("URL", "")

    create_article(
        citekey, author, year, name, journal, volume, number, urldate, url, tag
    )
    create_citation(
        citekey, "article", author, name, year, urldate, url, tag
    )

    return

def _parse_add_book(data, citekey, tag):
    """Parses a book DOI"""
    authors = []
    for author in data["author"]:
        given = author.get("given", "")
        family = author.get("family", "")
        authors.append(f"{given} {family}")
    author = ", ".join(authors)

    try:
        editors = []
        for editor in data["editor"]:
            given = editor.get("given", "")
            family = editor.get("family", "")
            editors.append(f"{given} {family}")
        editor = ", ".join(editors)
    except:
        editor = None

    title = data.get("title", "")
    publisher = data.get("publisher", "")
    year = data["issued"]["date-parts"][0][0]
    volume = data.get("volume", "")
    number = data.get("issue", "")
    urldate = ""
    url = data.get("URL", "")

    create_book(
        citekey, author, editor, title, publisher, year, volume, number, urldate, url, tag
    )
    create_citation(
        citekey, "book", author, title, year, urldate, url, tag
    )

    return

def _parse_add_inproceeding(data, citekey, tag):
    """Parses an inproceeding DOI"""
    authors = []
    for author in data["author"]:
        given = author.get("given", "")
        family = author.get("family", "")
        authors.append(f"{given} {family}")
    author = ", ".join(authors)

    try:
        editors = []
        for editor in data["editor"]:
            given = editor.get("given", "")
            family = editor.get("family", "")
            editors.append(f"{given} {family}")
        editor = ", ".join(editors)
    except:
        editor = None

    title = data.get("title", "")
    booktitle = data.get("container-title", "")
    publisher = data.get("publisher", "")
    pages = data.get("page", "")
    year = data["issued"]["date-parts"][0][0]
    volume = data.get("volume", "")
    number = data.get("issue", "")
    urldate = ""
    url = data.get("URL", "")

    create_inproceeding(
        citekey, author, editor, title, booktitle, publisher, pages, year, volume, number, urldate, url, tag
    )
    create_citation(
        citekey, "article", author, title, year, urldate, url, tag
    )

    return

def citation_with_doi(doi, citekey, tag):
    """Adds a citation with a doi"""
    if check_if_citekey_exists(citekey):
        return "The citekey already exists"

    data = _fetch_doi_citation(doi)
    if data[0] != "success":
        return data[0] # error message
    else:
        data = data[1] # data

    if data["type"] in ARTICLE_TYPES:
        _parse_add_article(data, citekey, tag)
    elif data["type"] in BOOK_TYPES:
        _parse_add_book(data, citekey, tag)
    elif data["type"] in INPROCEEDING_TYPES:
        _parse_add_inproceeding(data, citekey, tag)
    else:
        return "The citation type is not supported"

    return "success"


if __name__ == "__main__":
    citation_with_doi("10.1038/nature11631", "article", "article_tag") # article
    citation_with_doi("10.1007/978-3-031-45468-4", "book", "book_tag") # book
    citation_with_doi("10.1109/CVPR.2016.90", "inproceedings", "inproceedings_tag") # inproceeding
