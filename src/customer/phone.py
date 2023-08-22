import re


class Phone:
    def __init__(self, number):
        self.number = number

    def is_valid(self):
        phone_regex = r"\(\d{2}\)\s?9?\d{4}\d{4}"
        match = re.match("^" + phone_regex + "$", self.number)
        return bool(match)

    def __eq__(self, other):
        if isinstance(other, Phone):
            return self.number == other.number
        return False
