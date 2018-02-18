from django.db import models

from urllib.request import urlopen
import datetime
import json
import operator
import re

from books import utils

#======================= book details field ==========================
#class Category(models.Model):
#    category_name = models.CharField(max_length=453)

class Author(models.Model):
    name = models.CharField(max_length=453)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=453)

    def __str__(self):
        return self.name

def default_Publisher():
    obj, is_created = Publisher.objects.get_or_create(name = "unknown")
    return obj

class Bookdetails(models.Model):
    title = models.CharField(max_length=453)
    subtitle = models.CharField(max_length=453, blank=True)
    authors = models.ManyToManyField(Author) # [TODO] translator
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, default=default_Publisher)
    #published_date = models.DateField(blank=True, null=True)
    published_date = models.CharField(max_length=53, blank=True)
    #identifiers = models.ManyToManyField(BookIdentifier)
    #identifiers changed to foreignkey
    description = models.TextField(max_length=9453, blank=True)
    
    def __str__(self):
        return self.title

class BookIdentifier(models.Model):
    itype = models.CharField(max_length=7, choices=(
        ('ISBN_10', 'International Standard Book Number (10 digits)'),
        ('ISBN_13', 'International Standard Book Number (13 digits)'),
        ('ISSN', 'International Standard Serial Number (8 digits)')))

    identifier = models.CharField(max_length=13)
    belongbook = models.ForeignKey(Bookdetails, on_delete=models.CASCADE)

    def __str__(self):
        return self.identifier

#=================== book physical details field ========================
class Location(models.Model):
    description = models.CharField(max_length=53)
#[TODO]
#    floor = models.CharField(max_length=53, blank=True)
#    room = models.CharField(max_length=53, blank=True)
    def __str__(self):
        return self.description

def default_Location():
    obj, is_created = Location.objects.get_or_create(description = "unknown")
    return obj

class Possessor(models.Model):
    name = models.CharField(max_length=53)

    def __str__(self):
        return self.name

def default_Possessor():
    obj, is_created = Possessor.objects.get_or_create(name = "unknown")
    return obj

class Book(models.Model):
    detail = models.ForeignKey(Bookdetails, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_DEFAULT, default=default_Location)
    possessor = models.ForeignKey(Possessor, on_delete=models.SET_DEFAULT, default=default_Possessor)
    notas = models.TextField(max_length=9453, blank=True)

    def __str__(self):
        return '"%s" at "%s" belong to "%s"' % (self.detail, self.location, self.possessor)

