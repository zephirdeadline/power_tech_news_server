import feedparser
from django.contrib.auth.models import AnonymousUser

from api.models import Channel, Rss, Feed, RssStatus


class UniversalRss:

    def __init__(self):
        self.feeds = Feed.objects.all()

    def rss(self, request):
        rss_list = []
        for feed in self.feeds:
            news_feed = feedparser.parse(feed.channel.url)
            for rss in news_feed.entries:
                r, _ = Rss.objects.get_or_create(channel_id=feed.channel.id,
                                                 title=rss.get(feed.title, None),
                                                 description=rss.get(feed.description, None),
                                                 url_image=rss.get(feed.url_image, None),
                                                 url_origin=rss.get(feed.url_origin, None))
                if isinstance(request.user, AnonymousUser) or len(
                        RssStatus.objects.filter(user=request.user, rss=r)) == 0:
                    rss_list.append(r)
        # if not isinstance(user, AnonymousUser):
        #     rss.user_read.add(user)

        return rss_list
