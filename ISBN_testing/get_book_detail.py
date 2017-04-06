import urllib.request
import settings
def get_book_detail_using_isbn( input_isbn ):
    my_request_url = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + str(input_isbn) + "&key=" + str(settings.API_TOKEN)
    print( my_request_url )
    my_request = urllib.request.Request(my_request_url)
    try:
        my_respond = urllib.request.urlopen(my_request)
        my_respond_data = str(my_respond.read().decode('utf-8'))
        print( my_respond_data )
    except Exception as e:
        print( str(e) )

    

