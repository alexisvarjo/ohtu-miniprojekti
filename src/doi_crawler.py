"""Module for adding citations with a DOI"""

import requests

from repositories.article_repository import create_article
from db_helper import check_if_citekey_exists

ARTICLE_TYPES = ["article-journal",
                 "article-magazine",
                 "article-newspaper",
                 "article",
                 "journal-article"]

def citation_with_doi(doi, citekey):
    """Fetches citation information with a DOI"""

    if check_if_citekey_exists(citekey):
        return "The citekey already exists"

    try:
        response = requests.get(f"https://doi.org/{doi}", headers={"Accept": "application/vnd.citationstyles.csl+json"})
    except:
        return "The URL doesn't exist"

    if response.status_code == 404:
        return "The requested DOI doesn't exist"
    
    try:
        data = response.json()
    except:
        return "Error"

    # articles
    if data["type"] in ARTICLE_TYPES:
        authors = []
        for author in data["author"]:
            given = author.get("given", "")
            family = author.get("family", "")
            authors.append(f"{given} {family}")
        author = ", ".join(authors)

        year = data["issued"]["date-parts"][0][0]
        name = data.get("title", "")
        journal = data.get("container-title", "")
        volume = data.get("volume", "")
        number = data.get("issue", "")
        urldate = ""
        url = data.get("URL", "")

        create_article(citekey, author, year, name, journal, volume, number, urldate, url)
    
    # books
    # inproceedings

    return "success"


if __name__ == "__main__":
    citation_with_doi("10.1038/nature11631", "testing")