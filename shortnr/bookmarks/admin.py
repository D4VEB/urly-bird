from django.contrib import admin
from bookmarks.models import Bookmark


# Register your models here.

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('full_url', 'bookmark_description', 'pub_date')
    # ordering = ('-pub_date',)

# admin.site.register(Bookmark, BookmarkAdmin)
