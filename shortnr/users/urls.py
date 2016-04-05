from users.views import UpdateProfile
from django.conf.urls import url

urlpatterns = [
    url(r'^update_profilepic/(?P<id>\d+)/$', UpdateProfile.as_view(),
        name="update_profile"),
    ]