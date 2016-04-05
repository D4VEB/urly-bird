from django.conf.urls import url

from bookmarks.views import BookmarkList, BookmarkDetail, BookmarkUpdate,\
        BookmarkCreate

urlpatterns = [
    url(r'^$', BookmarkList.as_view(), name="bookmark_list"),
    url(r'^create$', BookmarkCreate.as_view(), name="bookmark_create"),
    url(r'^update/(?P<id>\d+)/$', BookmarkUpdate.as_view(),
        name="bookmark_update"),
    url(r'^(?P<pk>\d+)/$', BookmarkDetail.as_view(), name="bookmark_detail"),
]