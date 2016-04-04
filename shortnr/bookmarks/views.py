from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy

# Create your views here.
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView

from bookmarks.forms import BookmarkForm
from bookmarks.models import Bookmark


class BookmarkCreate(LoginRequiredMixin, CreateView):
    model = Bookmark
    form_class =BookmarkForm
    success_url = reverse_lazy("bookmarks")
    template_name_suffix = "_create"
    pk_url_kwarg = 'id'

    def check_validity(self, form):
        form.instance.user = self.request.user
        return super().check_validity(form)
        #TODO: check this against Chirper example. See why 'check_validity is throwing error.



class BookmarkDelete(DeleteView):
    """
    From the HW desccription: The bookmark links should use the
    internal short-code route, not the original URL.
    From this page, they should be able to edit and
    delete bookmarks.
    """
    model = Bookmark
    success_url = reverse_lazy("bookmarks")
    template_name_suffix = "_delete"

class BookmarkUpdate(UpdateView):
    model = Bookmark
    form_class = BookmarkForm
    template_name_suffix = "_update"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("bookmarks")
    # TODO: Method needed for success URL here?

class BookmarkList(ListView):
    """
    FROM THE HW INSTRUCTIONS: On a logged in user's
    index page, they should see a list of the
    bookmarks they've saved in reverse chronological
    order, paginated.
    """
    model = Bookmark
    template_name_suffix = "_list"
    queryset = Bookmark.objects.order_by("-mod_date")
    context_object_name = "bookmarks"
    paginate_by = 10

class BookmarkDetail(DetailView):
    model = Bookmark
    template_name_suffix = "_detail"
    context_object_name = "bookmarks"

class UserList(ListView):
    model = User
    queryset = User.objects.order_by("-last_login")
    #TODO: remember to come back to this order_by if "last_login" isn't useful.
    context_object_name = "users"
    template_name_suffix = "_list"

class UserDetail(DetailView):
    model = User
    context_object_name = "users"
    template_name_suffix = "_detail"






