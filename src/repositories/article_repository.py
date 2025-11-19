from sqlalchemy import text

from config import db
from entities.todo import Todo


def get_todos():
    result = db.session.execute(text("SELECT id, content, done FROM todos"))
    todos = result.fetchall()
    return [Todo(todo[0], todo[1], todo[2]) for todo in todos]


def set_done(todo_id):
    sql = text("UPDATE todos SET done = TRUE WHERE id = :id")
    db.session.execute(sql, {"id": todo_id})
    db.session.commit()


def normalize(value):
    return None if value == "" else value


def create_article(citekey, author, year, name, journal, volume, number, urldate, url):
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
