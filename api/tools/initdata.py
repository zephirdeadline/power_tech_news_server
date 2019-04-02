from api.models import Channel


def initdata():
    Channel.objects.create(url="https://www.zdnet.fr/feeds/rss/actualites/", name="zdnet")
    Channel.objects.create(url="https://www.lemondeinformatique.fr/flux-rss/thematique/internet/rss.xml", name="lemondeinformatique")
    Channel.objects.create(url="https://www.artima.com/weblogs/feeds/weblogs.rss", name="Artirma")

