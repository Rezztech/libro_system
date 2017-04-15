from books import models

from django.shortcuts import render
from django.http import HttpResponse

'''
def add_books(request):
	models.BookDetails.add_books(request.POST.get('books'))
	return HttpResponse('add books')
'''


def add_books(request):
    return render(request, "pages/add-books.html", locals())

def index(request):
	return render(request, "index.html")
