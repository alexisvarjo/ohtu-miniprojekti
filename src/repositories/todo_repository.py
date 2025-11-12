from config import db
from sqlalchemy import text

from entities.todo import Todo

def get_todos():
    result = db.session.execute(text("SELECT id, content, done FROM todos"))
    todos = result.fetchall()
    return [Todo(todo[0], todo[1], todo[2]) for todo in todos] 

def set_done(todo_id):
    sql = text("UPDATE todos SET done = TRUE WHERE id = :id")
    db.session.execute(sql, { "id": todo_id })
    db.session.commit()

def create_article(citekey, author, year, name, journal, volume, number, urldate, url):
    sql = text("""
    INSERT INTO articles (citekey, author, year, name, journal, volume, number, urldate, url)
    VALUES (:citekey, :author, :year, :name, :journal, :volume, :number, :urldate, :url)
""")
    db.session.execute(sql, {
    "citekey": citekey,
    "author": author,
    "year": year,
    "name": name,
    "journal": journal,
    "volume": volume,
    "number": number,
    "urldate": urldate,
    "url": url
})  
    db.session.commit()
