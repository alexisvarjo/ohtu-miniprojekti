import sys
import unittest

from services.bib_generating import bib_generator

sys.path.insert(0, "src")


class BibGenerator(unittest.TestCase):
    """Unit-testing for the bib generator"""

    def setUp(self):
        """Dictionary with the citations"""
        self.citations = {
            "articles": [
                {
                    "citekey": "300000",
                    "author": "Hedelmien ystävät",
                    "name": "Ananas ei sovi pizzaan",
                    "journal": "10 maailman ratkaisematonta mysteeriä",
                    "year": 1956,
                    "volume": None,
                    "number": None,
                    "urldate": None,
                    "url": None,
                },
                {
                    "citekey": "12341234",
                    "author": "Suolakurkku RY",
                    "name": "Vähemmän säilöntäaineita",
                    "journal": "Eettinen vihanneskasvatus",
                    "year": 2000,
                    "volume": 5000,
                    "number": None,
                    "urldate": None,
                    "url": None,
                },
                {
                    "citekey": "123123",
                    "author": "Suomen meloniliitto",
                    "name": "Melonien villjely Suomessa",
                    "journal": "joku",
                    "year": 2015,
                    "volume": None,
                    "number": None,
                    "urldate": None,
                    "url": None,
                },
            ],
            "books": [],
            "miscs": [],
        }

    def test_correct_bib_generating(self):
        """bib generator comparison"""
        self.assertEqual(
            bib_generator(self.citations),
            "@article{300000,\n  author={Hedelmien ystävät},\n  name={Ananas ei sovi pizzaan},\n  journal={10 maailman ratkaisematonta mysteeriä},\n  year={1956}\n}\n\n@article{12341234,\n  author={Suolakurkku RY},\n  name={Vähemmän säilöntäaineita},\n  journal={Eettinen vihanneskasvatus},\n  year={2000},\n  volume={5000}\n}\n\n@article{123123,\n  author={Suomen meloniliitto},\n  name={Melonien villjely Suomessa},\n  journal={joku},\n  year={2015}\n}\n\n",
        )
