from api.models import Channel, Feed


def initdata():
    Channel.objects.create(url="https://www.zdnet.fr/feeds/rss/actualites/", name="zdnet")
    Channel.objects.create(url="https://www.lemondeinformatique.fr/flux-rss/thematique/internet/rss.xml", name="lemondeinformatique")
    Feed.objects.create(title='title', channel_id=1, url_origin='link', date='pudDate')
    Feed.objects.create(title='title', channel_id=2, url_origin='link', date='published')
