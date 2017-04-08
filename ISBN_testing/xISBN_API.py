import urllib.request
from write_error_log import append_error_log
import json
import settings

def get_book_detail_using_isbn( input_isbn ):
    first_request_url = "http://xisbn.worldcat.org/webservices/xid/isbn/" + str(input_isbn) + "?method=getEditions&format=json&fl=publisher,author,year,title"
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
    if first_respond_json["stat"] != "ok":
        print( "Can't find any item!" )
        return False

    return first_respond_json["list"]

def get_book_detail( request_bar ):
    return_object = {}
    respond_items = get_book_detail_using_isbn( request_bar )
    return_object["TotalItems"] = len(respond_items)
    return_object["items"] = []
    for item in respond_items:
        temp_return_item = {}
        try:
            temp_return_item["title"] = item["title"] if "title" in item else ""
            temp_return_item["subtitle"] = item["subtitle"] if "subtitle" in item else ""
            temp_return_item["authors"] = item["authors"] if "authors" in item else []
            temp_return_item["publisher"] = item["publisher"] if "publisher" in item else ""
            temp_return_item["publishedDate"] = item["year"] if "year" in item else ""
            temp_return_item["industryIdentifiers"] = []
            if "isbn" in item:
                for one_isbn in item["isbn"]:
                    temp_return_item["industryIdentifiers"].append( { "type": "ISBN_13", "identifier": one_isbn } )
            temp_return_item["description"] = item["description"] if "description" in item else ""
        except Exception as e:
            append_error_log( "while fill up temp_return_item " + str(request_bar) )
            append_error_log( str(e) )
            print( str(e) )
            return False
        return_object["items"].append( temp_return_item )
    return return_object
