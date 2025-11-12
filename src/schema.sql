CREATE TABLE todos (
  id SERIAL PRIMARY KEY, 
  content TEXT NOT NULL,
  done BOOLEAN DEFAULT FALSE
)

CREATE TABLE articles (
  id SERIAL PRIMARY KEY,
  citekey TEXT NOT NULL,
  author TEXT NOT NULL,
  title TEXT NOT NULL,
  journal TEXT NOT NULL,
  year INT NOT NULL,
  volume INT,
  number INT,
  urldate TEXT NOT NULL,
  url TEXT NOT NULL
);

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  citekey TEXT NOT NULL,
  author TEXT NOT NULL,
  editor TEXT NOT NULL,
  title TEXT NOT NULL,
  publisher TEXT NOT NULL,
  year INT NOT NULL,
  volume INT,
  number INT,
  urldate TEXT,
  url TEXT
);

CREATE TABLE miscs (
  id SERIAL PRIMARY KEY,
  citekey TEXT NOT NULL,
  author TEXT,
  title TEXT,
  year INT,
  howpublished TEXT,
  urldate TEXT,
  url TEXT
);