"""Functions relating to all of the citations in the database"""

# pylint: disable=protected-access

from sqlalchemy import text

from config import db
from db_helper import tables

def normalize(value):
    """No empty strings"""
    return None if value == "" else value

def fetch_all_citations():
    """Dictionary of citation types, with lists as values,
    that include dictionaries with column names as keys and values as values"""
    all_citations = {}
    for citation_type in tables():
        if citation_type == "":
            continue
        sql = text(f"SELECT * FROM {citation_type}")
        result = db.session.execute(sql).fetchall()
        all_citations[citation_type] = list(reversed([dict(row._mapping) for row in result]))

    return all_citations

def create_citation(citekey, citation_type, author, name, year, urldate, url, tag):
    print(citekey, citation_type, author, name, year, urldate, url, tag)
    sql = text("""
    INSERT INTO citations (citekey, citation_type, author, name, year, urldate, url, tag)
    VALUES (:citekey, :citation_type, :author, :name, :year, :urldate, :url, :tag)""")
    db.session.execute(
        sql,
        {
            "citekey": citekey,
            "citation_type": normalize(citation_type),
            "author": normalize(author),
            "name": normalize(name),
            "year": normalize(year),
            "urldate": normalize(urldate),
            "url": normalize(url),
            "tag": normalize(tag)
        },
    )
    db.session.commit()
