from books import utils

from django.core.exceptions import ValidationError
from django.db import models

def isbn_issn_validator(string):
    if not utils.check_isbn_issn(string):
        raise ValidationError()


class Category(models.Model):
    category_name = models.CharField(max_length=453)

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
    subtitle = models.CharField(max_length=453)
    published_date = models.DateField()
    publisher = models.CharField(max_length=453)
    description = models.TextField(max_length=9453, null=True)

    categories = models.ManyToManyField(Category)
    authors = models.ManyToManyField(Author) # [TODO] translator
    identifiers = models.ManyToManyField(BookIdentifier)

    # books_owned = models.ForeignKey('Book', models.CASCADE, one_to_many=True)
    # [TODO] https://docs.djangoproject.com/en/dev/topics/db/queries/#following-relationships-backward

    @staticmethod
    def add_books(books):
        # add new books if not exist
        for book_info in books.get('items'):
            present_books = BookDetails.objects.filter(
                identifiers__identifier = book_info.get('industryIdentifiers')[0]
                                                   .get('identifier'))
            if present_books:
                return present_books[0]
            else:
                new_book = BookDetails(
                    title = book_info.get('title'),
                    subtitle = book_info.get('subtitle'),
                    published_date = utils.parse_date(book_info.get('publishedDate')),
                    publisher = book_info.get('publisher'),
                    description = book_info.get('description'))
                new_book.save()
                for d in book_info.get('industryIdentifiers'):
                    new_book.identifiers.add(
                        BookIdentifier.objects.get_or_create(type=d['type'],
                                                             identifier=d['identifier'])[0])
                for name in book_info.get('authors'):
                    new_book.authors.add(
                        Author.objects.get_or_create(name=name)[0])
                # [TODO] categories
                return new_book

class Book(models.Model):
    detail = models.ForeignKey(BookDetails, models.PROTECT)
    placed_floor = models.IntegerField()
    placed_room = models.CharField(max_length=453)
    owner = models.CharField(max_length=453)
