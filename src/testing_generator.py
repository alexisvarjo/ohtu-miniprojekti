"""Module for generation used for testing"""

import random
from string import ascii_letters, digits

def string_generator(length=""):
    """Function for generating a random string"""
    if length == "":
        length = random.randrange(1, 10)

    random_string = "".join(random.choices(ascii_letters + digits, k=length))

    return random_string

def number_generator(start, end, step):
    """Function for generating a random numder"""

    return random.randrange(start, end, step)
