import datetime

from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models

# from hashids import Hashids

# Create your models here.
#from hashids import Hashids


class Bookmark(models.Model):
    full_url = models.URLField(max_length=300)
    bookmark_description = description = models.CharField\
        (max_length=200, null=True, blank=True)
    # I used null=True and blank = True here
    # because the bookmark_description is optional
    pub_date = models.DateTimeField(auto_now=True)
    # count = models.IntegerField(default=0)

    def url_key(self):
        """
        This method will generate a hash id that can be used
        to create a shortened URL.
        """
        hashid = Hashids()
        return hashid.encode(self.id)

    def shortened_url(self):
        """
        This method will take the unique has id and create
        a shortened URL for the bookmark.

        From HW instructions: "Create a route like "/b/{code}"
        that will redirect any user -- not just logged in
        users -- to the bookmark associated with that code."
        """
        return "short/{}".format(self.url_key)

    def bookmark_clicks(self):
        """
        Added this method because I need this info for the stats
        pageto track how many times each link has been clicked.
        Used the suggested "Click" naming throughout per the
        homework directions.
        """
        return self.click_set.count()

    def last_month_clicks(self):
        """
        I added this method here to capture the number of clicks
        for the 'overall stats page' in the homework.
        """
        last_month = timezone.now() - datetime.timedelta(days=30)
        return self.click_set.filter(pub_date__gte=last_month).count()

    def __str__(self):
        return self.full_url
        # TODO change the variable name here to match the variable name used above.


class Click(models.Model):
    """
    FROM THE HW INSTRUCTIONS: When a user -- anonymous or logged in -- uses a bookmark URL,
    record that user, bookmark, and timestamp. A suggested
    name for this model is Click, even though you can navigate to
    the URL without a click by entering it in your navigation bar.
    """
    bookmark = models.ForeignKey(Bookmark)
    user = models.ForeignKey(User, null=True, blank=True)
    # null=True and blank=True so this is not limited
    # to logged-in users
    pub_date = models.DateTimeField(auto_now_add=True)

