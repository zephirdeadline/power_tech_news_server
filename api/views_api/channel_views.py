from django.db.models import Q, Model
from rest_framework import viewsets, permissions

from api.models import Channel, BlacklistChannel
from api.serializers.channel_serializer import ChannelSerializer


class ChannelViews(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChannelSerializer

    def get_queryset(self):
        user = self.request.user
        blchs = [blch.channel.id for blch in BlacklistChannel.objects.filter(user=user)]
        chs = [ch.id for ch in Channel.objects.filter(Q(user=None) | Q(user=user))]
        return Channel.objects.filter(pk__in=[ch for ch in chs if ch not in blchs])

    def perform_destroy(self, instance: Channel):
        if instance.user is None:
            BlacklistChannel.objects.create(user=self.request.user, channel=instance)
        else:
            instance.delete()
