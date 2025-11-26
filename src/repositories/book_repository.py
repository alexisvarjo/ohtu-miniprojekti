"""Functions for handling books in the database"""

from sqlalchemy import text

from config import db

def normalize(value):
    """No empty strings"""
    return None if value == "" else value


def create_book(citekey, author, editor, title, publisher, year, volume, number, urldate, url, tag):
    """Adds a book into the database"""
    # pylint: disable=too-many-arguments, too-many-positional-arguments

    sql = text("""
    INSERT INTO books (citekey, author, editor, title, publisher, year, volume, number, urldate, url, tag)
    VALUES (:citekey, :author, :editor, :title, :publisher, :year, :volume, :number, :urldate, :url, :tag)
""")
    db.session.execute(
        sql,
        {
            "citekey": citekey,
            "author": normalize(author),
            "editor": normalize(editor),
            "title": normalize(title),
            "publisher": normalize(publisher),
            "year": normalize(year),
            "volume": normalize(volume),
            "number": normalize(number),
            "urldate": normalize(urldate),
            "url": normalize(url),
            "tag": normalize(tag)
        },
    )
    db.session.commit()