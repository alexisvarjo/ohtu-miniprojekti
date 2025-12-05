CREATE TABLE citations (
  citekey TEXT PRIMARY KEY,
  citation_type TEXT,
  author TEXT,
  name TEXT,
  year INT,
  urldate TEXT,
  url TEXT,
  tag TEXT
);

CREATE TABLE articles (
  citekey TEXT PRIMARY KEY,
  author TEXT,
  name TEXT,
  journal TEXT,
  year INT,
  volume INT,
  number INT,
  urldate TEXT,
  url TEXT,
  tag TEXT,
  pdf BYTEA
);

CREATE TABLE books (
  citekey TEXT PRIMARY KEY,
  author TEXT,
  editor TEXT,
  title TEXT,
  publisher TEXT,
  year INT,
  volume INT,
  number INT,
  urldate TEXT,
  url TEXT,
  tag TEXT,
  pdf BYTEA
);

CREATE TABLE inproceedings (
  citekey TEXT PRIMARY KEY,
  author TEXT,
  editor TEXT,
  title TEXT,
  booktitle TEXT,
  publisher TEXT,
  pages TEXT,
  year INT,
  volume INT,
  number INT,
  urldate TEXT,
  url TEXT,
  tag TEXT,
  pdf BYTEA
);

CREATE TABLE miscs (
  citekey TEXT PRIMARY KEY,
  author TEXT,
  title TEXT,
  year INT,
  howpublished TEXT,
  urldate TEXT,
  url TEXT,
  pdf BYTEA
);
