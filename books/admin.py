from django.contrib import admin
from books import models

class Identifier_inline(admin.TabularInline):
    model = models.BookIdentifier

class BookdetailAdmin(admin.ModelAdmin):
    list_display = ("title", "publisher")
    search_fields = ("name", "subtitle", "publisher", "description")
    inlines = [ Identifier_inline, ]    #foreignkey backward


# Register your models here.
admin.site.register(models.Book)
admin.site.register(models.Bookdetails, BookdetailAdmin)
admin.site.register(models.Possessor)
admin.site.register(models.Location)

