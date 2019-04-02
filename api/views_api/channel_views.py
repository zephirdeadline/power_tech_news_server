from rest_framework import viewsets

from api.models import Channel
from api.serializers.channel_serializer import ChannelSerializer


class ChannelViews(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
