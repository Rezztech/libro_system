from django.shortcuts import render
from django.http import HttpResponse

from books import models

def add_books(request, isbn_list):
	res = 'added books: <br>'
	for isbn in isbn_list.split(','):
		book_info = models.get_book_info(isbn)
		res += book_info.title + '<br>'
	return HttpResponse(res)
