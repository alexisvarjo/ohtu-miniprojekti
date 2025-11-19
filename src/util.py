"""utils"""

from db_helper import check_if_citekey_exists


class UserInputError(Exception):
    """Käyttäjäsyötön virhe, joka heitetään, kun syöte ei vastaa odotettua muotoa."""


def validate_author(author):
    """Tarkistaa, että author -parametri ei ole tyhjä tai yli 100 merkkiä."""
    if len(author) == 0:
        raise UserInputError("Author must not be empty")

    if len(author) > 100:
        raise UserInputError("Author length must be smaller than 100")


def validate_year(year):
    """Tarkistaa, että vuosi on epänegatiivinen."""
    if int(year) < 0:
        raise UserInputError("Invalid publication year")


def validate_name(name):
    """Tarkistaa, että nimi ei ole tyhjä tai yli 100 merkkiä."""
    if len(name) == 0:
        raise UserInputError("Name must not be empty")

    if len(name) > 100:
        raise UserInputError("Name length must be smaller than 100")


def validate_journal(journal):
    """Tarkistaa, että lehden nimi ei ole tyhjä tai yli 100 merkkiä."""
    if len(journal) == 0:
        raise UserInputError("Journal name must not be empty")

    if len(journal) > 100:
        raise UserInputError("Journal name length must be smaller than 100")


def validate_volume(volume):
    """Tarkistaa, että tilavuus on epänegatiivinen."""
    if int(volume) < 0:
        raise UserInputError("Invalid volume")


def validate_number(number):
    """Tarkistaa, että numero on epänegatiivinen."""
    if int(number) < 0:
        raise UserInputError("Invalid number")


def validate_citekey(citekey):
    """Tarkistaa, että citekey on olemassa ja ei ole jo käytössä."""
    if len(citekey) == 0:
        raise UserInputError("Citekey is needed")
    if check_if_citekey_exists(citekey):
        raise UserInputError("Citekey already exists")
