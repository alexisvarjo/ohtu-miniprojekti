"""Helpers for interacting with the database"""

import os

from sqlalchemy import text

from testing_generator import string_generator, number_generator

from config import app, db


def clear_robot_sources():
    """Removes the sources added by the robot-tests"""
    sql_tables = tables()

    for table in sql_tables:
        sql = text(f"DELETE FROM {table} WHERE author = :author")
        db.session.execute(sql, {"author": "robot"})
    db.session.commit()


def tables():
    """Returns all table names from the database except those ending with _id_seq"""
    sql = text(
        "SELECT table_name "
        "FROM information_schema.tables "
        "WHERE table_schema = 'public' "
        "AND table_name NOT LIKE '%_id_seq'"
    )

    result = db.session.execute(sql)
    return [row[0] for row in result.fetchall()]


def setup_db():
    """
    Creating the database
    If database tables already exist, those are dropped before the creation
    """
    tables_in_db = tables()
    if len(tables_in_db) > 0:
        print(f"Tables exist, dropping: {', '.join(tables_in_db)}")
        for table in tables_in_db:
            sql = text(f"DROP TABLE {table}")
            db.session.execute(sql)
        db.session.commit()

    print("Creating database")

    # Read schema from schema.sql file
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read().strip()

    sql = text(schema_sql)
    db.session.execute(sql)
    db.session.commit()


def _filter_from_table(table, keyword, year, search_term):
    """helper function for filter_articles()"""
    base = f"SELECT * FROM {table} WHERE 1=1"
    params = {}

    # Year filter
    if year:
        base += " AND year = :year"
        params["year"] = year

    # Keyword search
    if keyword and search_term:
        # Map "title" → correct column
        if table == "articles":
            title_col = "name"
        else:
            title_col = "title"

        if keyword == "author":
            base += " AND author ILIKE :term"
        elif keyword == "title":
            base += f" AND {title_col} ILIKE :term"

        params["term"] = f"%{search_term}%"

    # Free text search
    elif search_term:
        # Title column differs between tables
        if table == "articles":
            title_col = "name"
        else:
            title_col = "title"

        base += f"""
            AND (
                citekey ILIKE :term OR
                author ILIKE :term OR
                {title_col} ILIKE :term
            )
        """
        params["term"] = f"%{search_term}%"

    sql = text(base)
    rows = db.session.execute(sql, params).mappings().all()

    return rows


def filter_articles(material, keyword, year, search_term):
    """Filters all articles from DB based on parameters"""
    # Map material → table name
    table_map = {"article": "articles", "book": "books", "misc": "miscs"}

    # If no material chosen → fetch from all three tables
    if not material:
        return (
            _filter_from_table("articles", keyword, year, search_term)
            + _filter_from_table("books", keyword, year, search_term)
            + _filter_from_table("miscs", keyword, year, search_term)
        )

    # Otherwise → fetch from the selected table
    return _filter_from_table(table_map[material], keyword, year, search_term)


def check_if_citekey_exists(citekey: str):
    """Checks if a citekey exists in the database"""
    sql = text("SELECT COUNT(*) FROM articles WHERE citekey = :citekey")
    count = db.session.execute(sql, {"citekey": citekey}).scalar()

    return count > 0


def get_article(citekey: str):
    """Returns all fields of an article identified by its citekey."""

    # Query using parameterized SQL
    sql = text("""
        SELECT
            citekey,
            author,
            year,
            name,
            journal,
            volume,
            number,
            urldate,
            url,
            tag
        FROM articles
        WHERE citekey = :citekey
    """)

    result = db.session.execute(sql, {"citekey": citekey}).mappings().first()

    if result is None:
        raise ValueError(f"Article with citekey '{citekey}' not found")

    return dict(result)


def modify_article(citekey: str, new_information: dict):
    """Modifies fields of an existing article identified by its citekey."""

    # pylint: disable=R0801

    # Check that article exists
    if not check_if_citekey_exists(citekey):
        raise ValueError(f"Article with citekey '{citekey}' not found")

    # Allowed fields to update
    allowed_fields = {
        "author",
        "year",
        "name",
        "journal",
        "volume",
        "number",
        "url",
        "tag"
    }

    # Filter out any invalid keys
    update_fields = {
        k: v
        for k, v in new_information.items()
        if k in allowed_fields and v is not None
    }

    if not update_fields:
        return  # No changes

    # Build SET clause from whitelisted columns
    # This is safe because column names are fixed, not user-provided
    set_clause = ", ".join(f"{col} = :{col}" for col in update_fields)

    # Create parameterized SQL
    sql = text(f"""
        UPDATE articles
        SET {set_clause}
        WHERE citekey = :citekey
    """)

    # Add citekey to parameters
    params = update_fields.copy()
    params["citekey"] = citekey

    # Execute safely with parameter binding
    db.session.execute(sql, params)
    db.session.commit()


def remove_article_from_database(citekey):
    """removes an article from database based on given parameter"""
    if not check_if_citekey_exists(citekey):
        raise ValueError("Article doesn't exist")
    sql = text("DELETE FROM articles WHERE citekey = :citekey")
    db.session.execute(sql, {"citekey": citekey})
    db.session.commit()

def add_test_source():
    """Adds a test source to the database"""

    sql = text("""
    INSERT INTO articles (citekey, author, year, name, journal, volume, number, urldate, url, tag)
    VALUES (:citekey, :author, :year, :name, :journal, :volume, :number, :urldate, :url, :tag)"""
    )

    db.session.execute(sql, {
            "citekey": string_generator(),
            "author": string_generator(),
            "year": number_generator(1700, 2000, 1),
            "name": string_generator(),
            "journal": string_generator(),
            "volume": number_generator(1, 10, 1),
            "number": number_generator(1, 10, 1),
            "urldate": string_generator(),
            "url": string_generator(),
            "tag": string_generator()
        }
    )
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        setup_db()
