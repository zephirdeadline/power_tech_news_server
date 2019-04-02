from django.views import View

import feedparser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.convertors.artima import Artima
from api.convertors.lemondeinformatique import Lemondeinformatique
from api.convertors.universal_rss import UniversalRss
from api.convertors.zdnet import Zdnet
from api.serializers.rss_serializer import RssSerializer


class NaturalRss(APIView):

    def get(self, request):

        # channel_to_fetch = [
        #     Zdnet(),
        #     Lemondeinformatique(),
        #     Artima()
        # ]
        #
        # rss_list = []
        # for ch in channel_to_fetch:
        #     news_feed = feedparser.parse(ch.url)
        #     for rss in news_feed.entries:
        #         r = ch.rss(rss, request.user)
        #         if request.user not in r.user_read.all():
        #             rss_list.append(r)
        return Response(RssSerializer(UniversalRss().rss(request), many=True).data)

