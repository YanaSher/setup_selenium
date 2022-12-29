import random
import string


def random_string(lengt):
    return "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=lengt))


def random_telefone_number(lengt):
    return "".join(random.choices(string.digits, k=lengt))


def random_email(length_1, length_2):
    return random_string(length_1) + "@" + random_string(length_2) + "." + random.choice(["com", "ru", "org"])

