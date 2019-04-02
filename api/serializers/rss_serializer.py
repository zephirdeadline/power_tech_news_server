from rest_framework import serializers

from api.models import Rss
from api.serializers.channel_serializer import ChannelSerializer


class RssSerializer(serializers.ModelSerializer):

    channel = ChannelSerializer()
    class Meta:
        model = Rss
        fields = '__all__'

