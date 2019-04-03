import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your convertors here.


class Channel(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=128)


class Rss(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    url_image = models.CharField(max_length=128, null=True, blank=True)
    url_origin = models.CharField(max_length=128)
    date = models.DateTimeField(default=datetime.datetime.now())


class Feed(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    url_image = models.CharField(max_length=128, null=True, blank=True)
    url_origin = models.CharField(max_length=128)
    date = models.CharField(max_length=128)


class RssStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rss = models.ForeignKey(Rss, on_delete=models.CASCADE)
    isRead = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'rss')
