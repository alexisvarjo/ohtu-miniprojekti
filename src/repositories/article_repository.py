"""Functions for handling articles in the database"""

from sqlalchemy import text

from config import db


def normalize(value):
    """No empty strings"""
    return None if value == "" else value


def create_article(
    citekey, author, year, name, journal, volume, number, urldate, url, tag, pdf=None
):
    """Adds an article into the database"""
    # pylint: disable=too-many-arguments, too-many-positional-arguments

    sql = text("""
    INSERT INTO articles (citekey, author, year, name, journal, volume, number, urldate, url, tag, pdf)
    VALUES (:citekey, :author, :year, :name, :journal, :volume, :number, :urldate, :url, :tag, :pdf)
""")
    db.session.execute(
        sql,
        {
            "citekey": citekey,
            "author": normalize(author),
            "year": normalize(year),
            "name": normalize(name),
            "journal": normalize(journal),
            "volume": normalize(volume),
            "number": normalize(number),
            "urldate": normalize(urldate),
            "url": normalize(url),
            "tag": normalize(tag),
            "pdf": pdf,
        },
    )
    db.session.commit()
