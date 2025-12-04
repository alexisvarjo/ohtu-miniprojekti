"""
Module for adding a citation with an ACM digital library link.

Due to all ACM Digital Library links having a DOI in the URL,
the citation fetching is done using the DOI crawler
"""

from services.doi_crawler import citation_with_doi_in_url

def acm_with_doi_in_url(url, citekey, tag):
    """Adding a citation with an ACM link with the DOI in the URL"""

    return citation_with_doi_in_url(url, citekey, tag)
