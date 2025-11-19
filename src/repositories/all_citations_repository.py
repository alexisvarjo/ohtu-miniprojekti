from sqlalchemy import text

from config import db
from db_helper import tables


def fetch_all_citations():
    """Dictionary of citation types, with lists as values,
    that include dictionaries with column names as keys and values as values"""
    all_citations = {}
    for citation_type in tables():
        sql = text(f"SELECT * FROM {citation_type}")
        result = db.session.execute(sql).fetchall()
        all_citations[citation_type] = reversed([dict(row._mapping) for row in result])

    return all_citations
