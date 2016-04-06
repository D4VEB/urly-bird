import datetime
import csv
from django.core.management import BaseCommand
from django.db.models import Count
from django.utils import timezone
from bookmarks.models import Bookmark

class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Create a command that creates a csv report
        with the top 20 bookmarks in the past 2 days

        Used these docs for guidance:
        https://docs.python.org/3/library/csv.html#csv.writer
        https://docs.djangoproject.com/en/1.9/howto/outputting-csv/
        """
        past_two_days = timezone.now() - datetime.timedelta(days=2)
        top_bookmarks = Bookmark.objects.filter(click__pub_date__gte=past_two_days)\
            .annotate(click_count=Count("click")).order_by("click_count")

        with open('top_bookmarks.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Bookmark', ' Clicks in last two days'])
            for bookmark in top_bookmarks:
                writer.writerow([bookmark.title, bookmark.bookmark_clicks])
