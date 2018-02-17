from django.contrib import admin
from books.models import Bookdetails, Book, BookIdentifier

class Identifier_inline(admin.TabularInline):
    model = BookIdentifier

class BookdetailAdmin(admin.ModelAdmin):
    list_display = ("title", "publisher")
    search_fields = ("name", "subtitle", "publisher", "description")
    inlines = [ Identifier_inline, ]


# Register your models here.
admin.site.register(Bookdetails, BookdetailAdmin)
admin.site.register(Book)

