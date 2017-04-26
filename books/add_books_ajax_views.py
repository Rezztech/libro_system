# The purpose of this file is to checking ISBN and return results to user browser when they keyin ISBN
from django.http import JsonResponse
import sys, os
GET_BOOK_DETAIL = os.path.join(os.path.dirname(__file__), "get_books_detail")
sys.path.append(GET_BOOK_DETAIL)
from get_book_detail import get_book_detail
from .utils import check_isbn_issn

def ajax_receive(request):
    return JsonResponse(request.POST, safe=False)

def isbn_to_detail(request):
    if request.is_ajax():
        isbn_input = request.POST["isbn_input"]
        
        if check_isbn_issn( str(isbn_input) ):
            response_object = get_book_detail(isbn_input)
            response_object["status"] = "success"
            return JsonResponse(response_object, safe=False)
        else:
            response_object = {}
            response_object["status"] = "invalid_identifier"
            return JsonResponse(response_object, safe=False)

