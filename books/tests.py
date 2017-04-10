from django.test import TestCase

from books import models

print(models.BookDetails.add_books(
	{
	'TotalItems':1,
	'items':[
	  {
	  "title": "",
	  "subtitle": "",
	  "authors":
	  [
	      "soytw"
	  ],
	  "publisher": "TNFSH",
	  "publishedDate": "2017-9-9",
	  "industryIdentifiers":
	  [
	      {
	          "type": "ISBN_13",
	          "identifier": "9789862723807"
	      },
	      {
	          "type": "ISBN_10",
	          "identifier": "9862723807"
	    }
	  ],
	  "description": "lalala"
	  }
	]
	}))
