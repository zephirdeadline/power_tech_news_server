from django.views import View

import feedparser
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from api.convertors.universal_rss import UniversalRss
from api.serializers.rss_serializer import RssSerializer


class NaturalRss(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        return Response(RssSerializer(UniversalRss().rss(request), many=True).data)

