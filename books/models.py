from books import utils

from django.core.exceptions import ValidationError
from django.db import models

from urllib.request import urlopen
import datetime
import json
import operator
import re


def isbn_issn_validator(string):
    def valid(string):
        if (re.fullmatch(r'[0-9]{9}[0-9X]', string)
                or re.fullmatch(r'[0-9]{13}', string)
                or re.fullmatch(r'[0-9]{7}[0-9X]', string)):
            if len(string) == 10:
                # ISBN-10
                weight = (10, 9, 8, 7, 6, 5, 4, 3, 2)
                s = sum(map(operator.mul, map(int, string[:-1]), weight))
                n = 11 - (s % 11)
                if n == 10:
                    return string[-1] == 'X'
                elif n == 11:
                    return string[-1] == '0'
                else:
                    return string[-1] == str(n)

            elif len(string) == 13:
                # ISBN-13
                weight = (1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3)
                s = sum(map(operator.mul, map(int, string[:-1]), weight))
                n = 10 - (s % 10)
                if n == 10:
                    n = 0
                return string[-1] == str(n)

            elif len(string) == 8:
                # ISSN
                weight = (8, 7, 6, 5, 4, 3, 2)
                s = sum(map(operator.mul, map(int, string[:-1]), weight))
                n = 11 - (s % 11)
                if n == 11:
                    return string[-1] == '0'
                elif n == 10:
                    return string[-1] == 'X'
                else:
                    return string[-1] == str(n)
        else:
            return False

    if not valid(string):
        raise ValidationError()


class BookIdentifier(models.Model):
    type = models.CharField(max_length=7, choices=(
        ('ISBN_10', 'International Standard Book Number (10 digits)'),
        ('ISBN_13', 'International Standard Book Number (13 digits)'),
        ('ISSN', 'International Standard Serial Number (8 digits)')))

    identifier = models.CharField(max_length=13,
                                  validators=[isbn_issn_validator])

class Author(models.Model):
    name = models.CharField(max_length=453)

class BookDetails(models.Model):
    title = models.CharField(max_length=453)
    published_date = models.DateField()
    publisher = models.CharField(max_length=453)
    category = models.CharField(max_length=453)
    description = models.TextField(max_length=9453, null=True)

    authors = models.ManyToManyField(Author) # [TODO] translator
    identifiers = models.ManyToManyField(BookIdentifier)

    # books_owned = models.ForeignKey('Book', models.CASCADE, one_to_many=True)
    # [TODO] https://docs.djangoproject.com/en/dev/topics/db/queries/#following-relationships-backward

class Book(models.Model):
    detail = models.ForeignKey(BookDetails, models.PROTECT)
    placed_floor = models.IntegerField()
    placed_room = models.CharField(max_length=453)
    owner = models.CharField(max_length=453)




def get_book_info(isbn):
    # !! DATABASE MODIFYING !!
    # will add a new book if not exist
    books = BookDetails.objects.filter(identifiers__identifier=isbn)
    if books:
        return books[0]
    else:
        book_info = utils.get_book_info_online(isbn)
        new_book = BookDetails(
            title = book_info.get('title'),
            published_date = utils.parse_date(book_info.get('publishedDate')),
            publisher = book_info.get('publisher'),
            description = book_info.get('description'),
            category = '')
        new_book.save()
        for d in book_info.get('industryIdentifiers'):
            new_book.identifiers.add(
                BookIdentifier.objects.get_or_create(type=d['type'],
                                                     identifier=d['identifier'])[0])
        for name in book_info.get('authors'):
            new_book.authors.add(
                Author.objects.get_or_create(name=name)[0])
        return new_book
