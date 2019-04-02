import feedparser

from api.models import Channel, Rss, Feed


class UniversalRss():

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
                if request.user not in r.user_read.all():
                    rss_list.append(r)
        # if not isinstance(user, AnonymousUser):
        #     rss.user_read.add(user)


        return rss_list
