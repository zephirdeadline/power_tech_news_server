from django.contrib.auth.models import AnonymousUser

from api.models import Channel, Rss


class Artima():

    def __init__(self):
        self.url = "https://www.artima.com/weblogs/feeds/weblogs.rss"
        self.channel = Channel.objects.get(url=self.url)

    def rss(self, rss_obj, user):
        rss, _ = Rss.objects.get_or_create(channel_id=self.channel.id,
                                           title=rss_obj.title,
                                           description=rss_obj.summary,
                                           url_image=None,
                                           url_origin=rss_obj.link)
        if not isinstance(user, AnonymousUser):
            rss.user_get.add(user)

        return rss
