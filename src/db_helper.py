import os

from sqlalchemy import text

from config import app, db


def reset_db():
    print(f"Clearing contents from table todos")
    sql = text(f"DELETE FROM todos")
    db.session.execute(sql)
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
    with open(schema_path, "r") as f:
        schema_sql = f.read().strip()

    sql = text(schema_sql)
    db.session.execute(sql)
    db.session.commit()


def list_articles(query=None):
    sql = text("SELECT * FROM articles")
    result = db.session.execute(sql)
    return result.fetchall()


def _filter_from_table(table, keyword, year, search_term):
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


if __name__ == "__main__":
    with app.app_context():
        setup_db()
