from rest_framework import serializers

from api.models import Rss


class RssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rss
        fields = '__all__'
