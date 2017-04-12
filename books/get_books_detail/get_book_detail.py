# request and return object is all like:
#{
# TotalItems:1
# items:[
#   {
#   "title": "",
#   "subtitle": "",
#   "authors":
#   [
#       ""
#   ],
#   "publisher": "",
#   "publishedDate": "",
#   "industryIdentifiers":
#   [
#       {
#           "type": "ISBN_13",
#           "identifier": "9789862723807"
#       },
#       {
#           "type": "ISBN_10",
#           "identifier": "9862723807"
#     }
#   ],
#   "description": ""
#   }
# ]
#}

# [soytw] to add: category

import sys, os
APIS_PATH = os.path.join(os.path.dirname(__file__), "APIs")
sys.path.append(APIS_PATH)
import Google_Books_API
import xISBN_API

def get_book_detail( request_bar ):
    return_object = {}
    return_object["TotalItems"] = 0
    return_object["items"] = []
    APIs = [Google_Books_API, xISBN_API]
    for API in APIs:
        respond_object = API.get_book_detail( request_bar )
        return_object["TotalItems"] = return_object["TotalItems"] + respond_object["TotalItems"]
        for item in respond_object["items"]:
            return_object["items"].append( item )
    return return_object

