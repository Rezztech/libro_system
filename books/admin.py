from django.contrib import admin
from books import models

class Identifier_inline(admin.TabularInline):
    model = models.BookIdentifier
    #foreign key backward , see detail:https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#inlinemodeladmin-objects

class Book_inline(admin.TabularInline):
    model = models.Book

class Bookdetail_inline(admin.TabularInline):
    model = models.Bookdetails
    fields = ("title",)

class Bookdetail_inline_manytomany(admin.TabularInline):
    model = models.Bookdetails.authors.through
    #https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#working-with-many-to-many-models

class BookdetailAdmin(admin.ModelAdmin):
    list_display = ("title", "publisher")
    search_fields = ("name", "subtitle", "publisher", "description")
    fields = (("title", "subtitle"), ("publisher", "published_date"), "authors", "description")
    inlines = [ Identifier_inline, ]    #foreignkey backward

class PossessorAdmin(admin.ModelAdmin):
    inlines = [ Book_inline, ]

class LocationAdmin(admin.ModelAdmin):
    inlines = [ Book_inline, ]

class AuthorAdmin(admin.ModelAdmin):
    inlines = [ Bookdetail_inline_manytomany, ]

class PublisherAdmin(admin.ModelAdmin):
    inlines = [ Bookdetail_inline, ]

class BookAdmin(admin.ModelAdmin):
    fields = ("detail", "location", "possessor")
    list_display = ("detail", "location", "possessor")

# Register your models here.
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Possessor, PossessorAdmin)
admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Bookdetails, BookdetailAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Publisher, PublisherAdmin)
