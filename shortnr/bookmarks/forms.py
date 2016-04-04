from django import forms
from bookmarks.models import Bookmark


class BookmarkForm(forms.ModelForm):

    class Meta:
        model = Bookmark
        fields = ("full_url", "boomark_description")