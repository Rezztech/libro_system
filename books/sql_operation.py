from books import models
from books import utils
 
class store:
    "Store book in SQL"

    def store_identifier(self, industryidentifier, book_detail):
        #utils.check_isbn_issn(industryidentifier["identifier"])
        ret = models.BookIdentifier.objects.create(itype = industryidentifier["type"], identifier = industryidentifier["identifier"], belongbook = book_detail)
        ret.save()
        return ret

    def store_author(self, author):
        ret = models.Author.objects.create(name = author)
        ret.save()
        return ret

    def store_book_detail(self, book_detail):
        ret = models.Bookdetails.objects.create(title = book_detail["title"], subtitle = book_detail["subtitle"], publisher = book_detail["publisher"], published_date = book_detail["publisheddate"], description = book_detail["description"])
        for author in book_detail["authors"]:
            ret.authors.add(self.store_author(author))
        
        for industryidentifier in book_detail["identifiers"]:
            self.store_identifier(industryidentifier, ret)

        ret.save()
        return ret

    def store_book(self, book_detail, substance_information):
        pass

class search:
    "search from SQL"
    
    def search_using_identifier(self):
        pass

class check:
    "check SQL contain"
    def check_identifiers_valid(self, book_detail):
        for identifier in book_detail["identifiers"]:
            utils.check_isbn_issn(identifier["identifier"])

    def check_identifier_valid(self, identifier):
        utils.check_isbn_issn(identifier)

    def check_resemble_book(self, book_detail):
        pass

    def check_duplicate_identifier(self, book_detail):
        pass

