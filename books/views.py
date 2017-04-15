from books import models

from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from django.http import HttpResponse

@ensure_csrf_cookie
def index(request):
	return render(request, "index.html")
