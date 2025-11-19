from repositories.all_citations_repository import fetch_all_citations

def bib_generator():
    citations = fetch_all_citations()
    bib = ""

    for citation_type in citations:
        for citation in citations[citation_type]:
            short_citation = citation_type[:-1]
            single_bib = ""
            single_bib += f"@{short_citation}{{{citation["citekey"]},\n"
            for field in citation:
                if citation[field] != None and field != "citekey":
                    single_bib += f"  {field}={{{citation[field]}}},\n"
            single_bib = single_bib[:-2]
            single_bib += "\n}\n\n"
            bib += single_bib

    return bib

def generate_bib_file():
    bib = bib_generator()
    with open("citations.bib", "w") as file:
        file.write(bib)
