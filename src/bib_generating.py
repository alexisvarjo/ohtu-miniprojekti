"""Functions for bib generating"""

from repositories.all_citations_repository import fetch_all_citations

def bib_generator(citations):
    """Generates a bib string"""
    bib = ""
    for citation_type in citations:
        for citation in citations[citation_type]:
            short_citation = citation_type[:-1]
            single_bib = ""
            single_bib += f"@{short_citation}{{{citation["citekey"]},\n"
            for field in citation:
                if citation[field] is not None and field != "citekey":
                    single_bib += f"  {field}={{{citation[field]}}},\n"
            single_bib = single_bib[:-2]
            single_bib += "\n}\n\n"
            bib += single_bib

    return bib

def generate_bib_browser():
    """Generates a bib for the browser viewing"""
    citations = fetch_all_citations()
    return bib_generator(citations)

def generate_bib_file():
    """Generates a citations.bib file"""
    citations = fetch_all_citations()
    bib = bib_generator(citations)
    with open("citations.bib", "w", encoding="utf-8") as file:
        file.write(bib)
