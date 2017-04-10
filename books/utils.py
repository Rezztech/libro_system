from urllib.request import urlopen
import json
import datetime

def get_book_info_online(isbn):
    # [TODO] handle duplicated items in response
    response1 = json.loads(
        urlopen('https://www.googleapis.com/books/v1/volumes?q=isbn:' + isbn)
        .read().decode())
    response2 = json.loads(urlopen(response1['items'][0]['selfLink']).read().decode())
    return response2['volumeInfo']

def parse_date(date_str):
	l = list(map(int, date_str.split('-')))
	year = month = day = 1
	if len(l) >= 1:
		year = l[0]
	if len(l) >= 2:
		month = l[1]
	if len(l) >= 3:
		day = l[2]
	return datetime.date(year, month, day)

# test
# print(get_book_info_online('9789866369186'))
# input()
# print(isbn_validator('7309045475'))
# print(isbn_validator('9789861817286'))
# print(issn_validator('03785955'))
