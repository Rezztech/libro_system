import urllib.request
import json
import settings
def get_book_detail_using_isbn( input_isbn ):
    first_request_url = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + str(input_isbn) + "&key=" + str(settings.API_TOKEN)
    #print( first_request_url )
    first_request = urllib.request.Request(first_request_url)
    first_respond_data = ""
    try:
        first_respond = urllib.request.urlopen(first_request)
        first_respond_data = str(first_respond.read().decode('utf-8'))
        
    except Exception as e:
        print( str(e) )

    #print( first_respond_data )
    #return first_respond_data
    first_respond_json = json.loads( first_respond_data )
    #return first_respond_json
    second_request_url = first_respond_json["items"][0]["selfLink"]
    second_request = urllib.request.Request(second_request_url)
    second_respond_data = ""
    try:
        second_respond = urllib.request.urlopen(second_request)
        second_respond_data = str(second_respond.read().decode('utf-8'))
    except Exception as e:
        print( str(e) )

    second_respond_json = json.loads( second_respond_data )
    return second_respond_json

