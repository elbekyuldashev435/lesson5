from django.contrib import admin
from .models import Category, Author, Books, BookAuthor
# Register your models here.

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Books)
admin.site.register(BookAuthor)