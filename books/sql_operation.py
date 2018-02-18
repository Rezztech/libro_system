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

    def store_location(self, location):
        location_description = ""
        location_description = "unknown" if location == "" else location
        obj, is_created = models.Location.objects.get_or_create(description = location_description)
        return obj

    def store_possessor(self, possessor):
        possessor_name = ""
        possessor_name = "unknown" if possessor == "" else possessor
        obj, is_created = models.Possessor.objects.get_or_create(name = possessor_name)
        return obj

    def store_book(self, book_detail, substance_information):
        ret = models.Book.objects.create(notas = substance_information["notas"], location = self.store_location(substance_information["location"]), possessor = self.store_possessor(substance_information["possessor"]), detail = self.store_book_detail(book_detail))
        ret.save()
        return ret

class search:
    "search from SQL"
    
    def search_using_identifier(self):
        pass

class check:
    "check SQL contain"
    def check_identifiers_valid(self, book_detail):
        for identifier in book_detail["identifiers"]:
            utils.check_isbn_issn(identifier["identifier"])

    def check_title_not_empty(self, book_detail):
        if book_detail["title"] == "":
            raise BookdetailValidError("title_empty")

    def check_identifier_valid(self, identifier):
        utils.check_isbn_issn(identifier)

    def check_resemble_book(self, book_detail):
        pass

    def check_duplicate_identifier(self, book_detail):
        pass

