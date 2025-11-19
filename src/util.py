class UserInputError(Exception):
    pass


def validate_author(author):
    if len(author) == 0:
        raise UserInputError("Author must not be empty")

    if len(author) > 100:
        raise UserInputError("Author length must be smaller than 100")


def validate_year(year):
    if int(year) < 0:
        raise UserInputError("Invalid publication year")


def validate_name(name):
    if len(name) == 0:
        raise UserInputError("Name must not be empty")

    if len(name) > 100:
        raise UserInputError("Name length must be smaller than 100")


def validate_journal(journal):
    if len(journal) == 0:
        raise UserInputError("Journal name must not be empty")

    if len(journal) > 100:
        raise UserInputError("Journal name length must be smaller than 100")


def validate_volume(volume):
    if int(volume) < 0:
        raise UserInputError("Invalid volume")


def validate_number(number):
    if int(number) < 0:
        raise UserInputError("Invalid number")


def validate_citekey(citekey):
    if len(citekey) == 0:
        raise UserInputError("Citekey is needed")
