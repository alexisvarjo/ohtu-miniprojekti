"""Module for adding citations with a DOI"""

import requests

from db_helper import check_if_citekey_exists
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


def citation_with_doi(doi, citekey, tag):
    """Fetches citation information with a DOI"""

    if check_if_citekey_exists(citekey):
        return "The citekey already exists"

    try:
        response = requests.get(
            f"https://doi.org/{doi}",
            headers={"Accept": "application/vnd.citationstyles.csl+json"},
            timeout=10,
        )
    except:
        return "The URL doesn't exist"

    if response.status_code == 404:
        return "The requested DOI doesn't exist"

    try:
        data = response.json()
    except:
        return "Error"
    
    print(data)

    # articles
    if data["type"] in ARTICLE_TYPES:
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

    # books
    elif data["type"] in BOOK_TYPES:
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

    # inproceedings
    elif data["type"] in INPROCEEDING_TYPES:
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
    else:
        return "The citation type is not supported"


    return "success"


if __name__ == "__main__":
    citation_with_doi("10.1038/nature11631", "testing")
