"""
notes from 04/01
1. create new "users" app
2. create templates directory in "users"
3. in Views, create class like "RegisterView"
4. create page like register.html
"""

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import CreateView, UpdateView


class RegisterUser(CreateView):
    model = User
    form_class = UserCreationForm
    template_name_suffix = "_register"
    success_url = reverse_lazy("bookmark_list")

class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ImageUpdateForm
    template_name_suffix = "_upload_profilepic"
    success_url = reverse_lazy("bookmark_list")
    pk_url_kwarg = "id"
