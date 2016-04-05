from django import forms

from users.models import UserProfile

class ProfilePicUpload(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ("image",)
