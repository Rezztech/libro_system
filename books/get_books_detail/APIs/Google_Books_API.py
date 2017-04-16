import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import urllib.request
from write_error_log import append_error_log
import json
import API_settings
def get_book_detail_using_isbn( input_isbn ):
    first_request_url = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + str(input_isbn) + "&key=" + str(API_settings.GOOGLE_BOOKS_API_TOKEN)
    first_request = urllib.request.Request(first_request_url)
    first_respond_data = ""
    try:
        first_respond = urllib.request.urlopen(first_request)
        first_respond_data = str(first_respond.read().decode('utf-8'))
        
    except Exception as e:
        append_error_log( "Google API error while request + " + first_request_url )
        append_error_log( str(e) )
        print( str(e) )
        return False

    first_respond_json = json.loads( first_respond_data )
    #return first_respond_json

    return_object = {}
    return_object["TotalItems"] = first_respond_json["totalItems"]
    return_object["items"] = first_respond_json["items"] if "items" in first_respond_json else []

    return return_object

def get_book_detail( request_bar ):
    return_object = {}
    respond_object = get_book_detail_using_isbn( request_bar )
    return_object["TotalItems"] = respond_object["TotalItems"]
    return_object["items"] = []
    for item in respond_object["items"]:
        temp_return_object = {}
        try:
            respond_item = item["volumeInfo"]
            #print(respond_item)
            temp_return_object["title"] = respond_item["title"] if "title" in respond_item else ""
            temp_return_object["subtitle"] = respond_item["subtitle"] if "subtitle" in respond_item else ""
            temp_return_object["authors"] = respond_item["authors"] if "authors" in respond_item else []
            temp_return_object["publisher"] = respond_item["publisher"] if "publisher" in respond_item else ""
            temp_return_object["publishedDate"] = respond_item["publishedDate"] if "publishedDate" in respond_item else ""
            temp_return_object["industryIdentifiers"] = respond_item["industryIdentifiers"] if "industryIdentifiers" in respond_item else []
            temp_return_object["description"] = respond_item["description"] if "description" in respond_item else ""
            return_object["items"].append( temp_return_object )
        except Exception as e:
            append_error_log( "while fill up temp_return_object " + str( request_bar ) + " (Google Books API)" )
            append_error_log( str(e) )
   
    return return_object

