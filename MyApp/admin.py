from django.contrib import admin

from .models import Book_details, User

# Register your models here.
admin.site.register(User)
admin.site.register(Book_details)
