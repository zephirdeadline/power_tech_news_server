from rest_framework import viewsets

from api.models import Rss
from api.serializers.rss_serializer import RssSerializer


class RssViews(viewsets.ModelViewSet):
    queryset = Rss.objects.all()
    serializer_class = RssSerializer
