from urllib.request import urlopen
import json
import datetime
import re
import operator

class Error(Exception):
    pass

class IndustryIdentifierError(Error):
    def __init__(self, message):
        self.message = message

def check_isbn_issn(string):
    if (re.fullmatch(r'[0-9]{9}[0-9X]', string) or re.fullmatch(r'[0-9]{13}', string) or re.fullmatch(r'[0-9]{7}[0-9X]', string)):
        if len(string) == 10:
            # ISBN-10
            weight = (10, 9, 8, 7, 6, 5, 4, 3, 2)
            s = sum(map(operator.mul, map(int, string[:-1]), weight))
            n = 11 - (s % 11)
            if (n == 11 and string[-1] == '0') or (n == 10 and string[-1] == 'X') or (n != 11 and n != 10 and string[-1] == str(n)):
                return "ISBN_10"
            else:
                raise IndustryIdentifierError("ISBN-10 not valid")

        elif len(string) == 13:
            # ISBN-13
            weight = (1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3)
            s = sum(map(operator.mul, map(int, string[:-1]), weight))
            n = 10 - (s % 10)
            if n == 10:
                n = 0
            if string[-1] == str(n):
                return "ISBN_13"
            else:
                raise IndustryIdentifierError("ISBN-13 not valid")

        elif len(string) == 8:
            # ISSN
            weight = (8, 7, 6, 5, 4, 3, 2)
            s = sum(map(operator.mul, map(int, string[:-1]), weight))
            n = 11 - (s % 11)
            if (n == 11 and string[-1] == '0') or (n == 10 and string[-1] == 'X') or (n != 11 and n != 10 and string[-1] == str(n)):
                return "ISSN"
            else:
                raise IndustryIdentifierError("ISSN not valid")
    else:
        raise IndustryIdentifierError("identifier is not fit to ISBN or ISSN")

def parse_date(date_str):
    l = list(map(int, date_str.split('-')))
    year = month = day = 1
    if len(l) >= 1:
        year = l[0]
    if len(l) >= 2:
        month = l[1]
    if len(l) >= 3:
        day = l[2]
    return datetime.date(year, month, day)

# test
# print(get_book_info_online('9789866369186'))
# input()
# print(isbn_validator('7309045475'))
# print(isbn_validator('9789861817286'))
# print(issn_validator('03785955'))

