import urllib.request
from write_error_log import append_error_log
import json
import settings
def get_book_detail_using_isbn( input_isbn ):
    first_request_url = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + str(input_isbn) + "&key=" + str(settings.GOOGLE_BOOKS_API_TOKEN)
    first_request = urllib.request.Request(first_request_url)
    first_respond_data = ""
    try:
        first_respond = urllib.request.urlopen(first_request)
        first_respond_data = str(first_respond.read().decode('utf-8'))
        
    except Exception as e:
        append_error_log( "while request + " + first_request_url )
        append_error_log( str(e) )
        print( str(e) )
        return False

    first_respond_json = json.loads( first_respond_data )
    #return first_respond_json
    if first_respond_json["totalItems"] == 0:
        print( "Can't find any item!" )
        return False
    
    if first_respond_json["totalItems"] != 1:
        print( "find items more than 1!!!!!!!!!!" )
        append_error_log("Google Books API find more than one respond while isbn = " + input_isbn)

    second_request_url = first_respond_json["items"][0]["selfLink"]
    second_request = urllib.request.Request(second_request_url)
    second_respond_data = ""
    try:
        second_respond = urllib.request.urlopen(second_request)
        second_respond_data = str(second_respond.read().decode('utf-8'))
    except Exception as e:
        append_error_log( "while request + " + second_request_url )
        append_error_log( str(e) )

        print( str(e) )
        return False

    second_respond_json = json.loads( second_respond_data )
    return second_respond_json

