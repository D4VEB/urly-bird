from django.contrib import admin
from bookmarks.models import Bookmark
# Register your models here.

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'full_url', 'bookmark_description', 'pub_date')
    # ordering = ('-pub_date',)


