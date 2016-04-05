from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
import datetime
from django.utils import timezone

from django.db.models import Count

from django.views.generic import CreateView, DeleteView, UpdateView, ListView, \
        DetailView, RedirectView

from hashids import Hashids

from bookmarks.forms import BookmarkForm
from bookmarks.models import Bookmark, Click


# Create your views here.

class BookmarkCreate(LoginRequiredMixin, CreateView):
    model = Bookmark
    form_class = BookmarkForm
    success_url = reverse_lazy("bookmark_list")
    template_name_suffix = "_create"

    def check_validity(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    #

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
    success_url = reverse_lazy("bookmark_list")

class BookmarkList(ListView):
    """
    FROM THE HW INSTRUCTIONS: On a logged in user's
    index page, they should see a list of the
    bookmarks they've saved in reverse chronological
    order, paginated.
    """
    model = Bookmark
    template_name_suffix = "_list"
    queryset = Bookmark.objects.order_by("-pub_date")
    context_object_name = "bookmarks"
    paginate_by = 10

class BookmarkDetail(DetailView):
    model = Bookmark
    template_name_suffix = "_detail"
    context_object_name = "bookmarks"

class UserList(ListView):
    queryset = User.objects.order_by("-last_login")
    context_object_name = "users"
    template_name_suffix = "_list"
    paginate_by = 4

class UserDetail(ListView):
    context_object_name = "bookmarks"
    template_name_suffix = "_detail"
    paginate_by = 4

    def get_queryset(self):
        logged_user = User.objects.get(pk=self.kwargs['pk'])
        return Bookmark.objects.filter(user=logged_user).order_by("-pub_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logged_user = User.objects.get(pk=self.kwargs['pk'])
        context["logged_user"] = logged_user
        context["user_logged_in"] = self.request.user == logged_user
        return context

    class UserStats(DetailView):
        """
        FROM HW: Add an overall stats page for each user
        where you can see a table of their links by
        popularity and their number of clicks over the
        last 30 days. This page should only be visible
        to that user.
        """

        model = User
        template_name = "users/user_stats.html"
        context_object_name = "user"

        def get_context_data(self, **kwargs):

            context = super().get_context_data(**kwargs)
            last_month = timezone.now() - datetime.timedelta(days=30)

            context["bookmarks"] = self.object.bookmark_set.filter(
                click__created_at__gt=last_month).annotate(
                num_count=Count('click')).order_by('-num_count')
            return context

class ShortLink(RedirectView):
    permanent = False
    pattern_name = "redirect_link"

    def get_redirect_url(self, *args, **kwargs):
        hashid = Hashids()
        short_key = self.kwargs["url_key"]
        url_id = hashid.decode(short_key)[0]
        bookmark = get_object_or_404(Bookmark, pk=url_id)
        if self.request.user is User:
            Click.objects.create(bookmark=bookmark, user=self.request.user)
        else:
            Click.objects.create(bookmark=bookmark)
        return bookmark


