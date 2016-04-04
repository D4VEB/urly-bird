"""
notes from 04/01
1. create new "users" app
2. create templates directory in "users"
3. in Views, create class like "RegisterView"
4. create page like register.html
"""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

class RegisterUser(CreateView):
    model = User
    form_class = UserCreationForm
    template_name_suffix = "_register"
    success_url = reverse_lazy("bookmarks")


