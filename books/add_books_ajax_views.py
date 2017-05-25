# The purpose of this file is to checking ISBN and return results to user browser when they keyin ISBN
# 2. receive book detail to store them
from django.http import JsonResponse
import sys, os
GET_BOOK_DETAIL = os.path.join(os.path.dirname(__file__), "get_books_detail")
sys.path.append(GET_BOOK_DETAIL)
from get_book_detail import get_book_detail
from .utils import check_isbn_issn

def response_receive_ajax(request):
    return JsonResponse(request.POST, safe=False)

def isbn_to_detail(request):
    if request.is_ajax():
        isbn_input = request.POST["isbn_input"]
        response_object = {}

        if check_isbn_issn( str(isbn_input) ):
            response_object = get_book_detail(isbn_input)
            response_object["status"] = "success"

        else:
            response_object["status"] = "invalid_identifier"

        return JsonResponse(response_object, safe=False)

def detail_to_store(request):
    if request.is_ajax():
        book_detail = {}
        book_detail["title"] = request.POST["title"]
        book_detail["subtitle"] = request.POST["subtitle"]
        book_detail["publisher"] = request.POST["publisher"]
        book_detail["publisheddate"] = request.POST["publisheddate"]
        book_detail["description"] = request.POST["description"]
        book_detail["authors"] = request.POST.getlist("authors[]")

        identifiers_not_split = request.POST.getlist("identifiers[]")
        identifiers_splited = []
        for identifier in identifiers_not_split:
            identifiers_splited.append({
                "type" : identifier.split(":")[0],
                "identifier" : identifier.split(":")[1]
                })
        book_detail["identifiers"] = identifiers_splited

        #return JsonResponse(book_detail, safe=False)

        response_object = {}
        response_object["status"] = "success"
        response_object["invalid_identifier_content"] = []
        if book_detail["title"] == "":
            response_object["status"] = "title_blank"
        for identifier in book_detail["identifiers"]:
            if not check_isbn_issn( identifier["identifier"] ):
                response_object["status"] = "invalid_identifier"
                response_object["invalid_identifier_content"].append(identifier["identifier"])

        return JsonResponse(response_object, safe=False)
