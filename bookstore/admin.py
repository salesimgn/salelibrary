from django.contrib import admin
from .models import BookInfo

# Register your models here.

@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    fields = ["book_file","title","author","description","language","category","upload_by"]
