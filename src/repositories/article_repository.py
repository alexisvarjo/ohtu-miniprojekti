"""Functions for handling articles in the database"""

from sqlalchemy import text

from config import db


def normalize(value):
    """No empty strings"""
    return None if value == "" else value


def create_article(citekey, author, year, name, journal, volume, number, urldate, url):
    """Adds an article into the database"""
    # pylint: disable=too-many-arguments, too-many-positional-arguments

    sql = text("""
    INSERT INTO articles (citekey, author, year, name, journal, volume, number, urldate, url)
    VALUES (:citekey, :author, :year, :name, :journal, :volume, :number, :urldate, :url)
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
        },
    )
    db.session.commit()
