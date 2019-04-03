from datetime import time, datetime, timedelta
from time import mktime

import feedparser
import pytz
from django.contrib.auth.models import AnonymousUser
from django.utils import timezone

from api.models import Channel, Rss, Feed, RssStatus


class UniversalRss:

    def __init__(self):
        self.feeds = Feed.objects.all()

    def get_date(self, struc_date):
        if struc_date is None:
            return datetime.now()
        return datetime.fromtimestamp(mktime(struc_date))

    def rss(self, request):
        rss_list = []
        for feed in self.feeds:
            news_feed = feedparser.parse(feed.channel.url)
            for rss in news_feed.entries:
                r, _ = Rss.objects.get_or_create(channel_id=feed.channel.id,
                                                 title=rss.get('title', None),
                                                 description=rss.get('summary', None),
                                                 url_image=rss.get('r', None),
                                                 url_origin=rss.get('link', None),
                                                 date=self.get_date(rss.get('published_parsed', None)))

                if request.user.is_anonymous or len(RssStatus.objects.filter(user=request.user, rss=r)) == 0:
                    rss_list.append(r)
        # if not isinstance(user, AnonymousUser):
        #     rss.user_read.add(user)

        return sorted(rss_list, key=lambda x: x.date, reverse=True)
