"""Functions for handling inroceedings in the database"""

from sqlalchemy import text

from config import db


def normalize(value):
    """No empty strings"""
    return None if value == "" else value


def create_inproceeding(citekey, author, editor, title, booktitle, publisher, pages, year, volume, number, urldate, url, tag):
    """Adds an inproceeding into the database"""
    # pylint: disable=too-many-arguments, too-many-positional-arguments

    sql = text("""
    INSERT INTO inproceedings (citekey, author, editor, title, booktitle, publisher, pages, year, volume, number, urldate, url, tag)
    VALUES (:citekey, :author, :editor, :title, :booktitle, :publisher, :pages, :year, :volume, :number, :urldate, :url, :tag)
""")
    db.session.execute(
        sql,
        {
            "citekey": citekey,
            "author": normalize(author),
            "editor": normalize(editor),
            "title": normalize(title),
            "booktitle": normalize(booktitle),
            "publisher": normalize(publisher),
            "pages": normalize(pages),
            "year": normalize(year),
            "volume": normalize(volume),
            "number": normalize(number),
            "urldate": normalize(urldate),
            "url": normalize(url),
            "tag": normalize(tag)
        },
    )
    db.session.commit()
