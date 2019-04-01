from django.views import View

import feedparser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.convertors.lemondeinformatique import Lemondeinformatique
from api.convertors.zdnet import Zdnet
from api.serializers.rss_serializer import RssSerializer


class NaturalRss(APIView):

    channel_to_fetch = [
        Zdnet(),
        Lemondeinformatique(),
    ]

    def get(self, request):
        rss_list = []
        for ch in self.channel_to_fetch:
            news_feed = feedparser.parse(ch.url)
            for rss in news_feed.entries:
                rss_list.append(ch.rss(rss, request.user))
        return Response(RssSerializer(rss_list, many=True).data)

