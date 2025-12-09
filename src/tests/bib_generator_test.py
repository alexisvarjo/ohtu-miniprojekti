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
            "books": [
                {
                    "author": "Christopher M. Bishop, Hugh Bishop",
                    "citekey": "doi_book",
                    "editor": None,
                    "number": None,
                    "publisher": "Springer International Publishing",
                    "tag": None,
                    "title": "Deep Learning",
                    "url": "http://dx.doi.org/10.1007/978-3-031-45468-4",
                    "urldate": None,
                    "volume": None,
                    "year": 2024
                }
            ],
            "citations": [
                {
                    "author": "Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun",
                    "citation_type": "inproceedings",
                    "citekey": "doi_inproceedings",
                    "name": "Deep Residual Learning for Image Recognition",
                    "tag": None,
                    "url": "http://dx.doi.org/10.1109/CVPR.2016.90",
                    "urldate": None,
                    "year": 2016
                },
            ],
            "inproceedings": [
                {
                    "author": "Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun",
                    "booktitle": "2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)",
                    "citekey": "doi_inproceedings",
                    "editor": None,
                    "number": None,
                    "pages": "770-778",
                    "publisher": "IEEE",
                    "tag": None,
                    "title": "Deep Residual Learning for Image Recognition",
                    "url": "http://dx.doi.org/10.1109/CVPR.2016.90",
                    "urldate": None,
                    "volume": None,
                    "year": 2016
                }
            ]
        }

    def test_correct_bib_generating(self):
        """bib generator comparison"""
        self.assertEqual(
            bib_generator(self.citations),
            """@article{300000,\n  author={Hedelmien ystävät},\n  title={Ananas ei sovi pizzaan},\n  journal={10 maailman ratkaisematonta mysteeriä},\n  year={1956}\n}\n\n@article{12341234,\n  author={Suolakurkku RY},\n  title={Vähemmän säilöntäaineita},\n  journal={Eettinen vihanneskasvatus},\n  year={2000},\n  volume={5000}\n}\n\n@article{123123,\n  author={Suomen meloniliitto},\n  title={Melonien villjely Suomessa},\n  journal={joku},\n  year={2015}\n}\n\n@book{doi_book,\n  author={Christopher M. Bishop, Hugh Bishop},\n  publisher={Springer International Publishing},\n  title={Deep Learning},\n  url={http://dx.doi.org/10.1007/978-3-031-45468-4},\n  year={2024}\n}\n\n@inproceedings{doi_inproceedings,\n  author={Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun},\n  booktitle={2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages={770-778},\n  publisher={IEEE},\n  title={Deep Residual Learning for Image Recognition},\n  url={http://dx.doi.org/10.1109/CVPR.2016.90},\n  year={2016}\n}\n\n""",
        )
