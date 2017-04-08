import sys
sys.path.append("./APIs")
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

