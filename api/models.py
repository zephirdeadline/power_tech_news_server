from django.contrib.auth.models import User
from django.db import models

# Create your convertors here.


class Channel(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=128)


class Rss(models.Model):
    user_read = models.ManyToManyField(User, related_name='rss_read')
    user_get = models.ManyToManyField(User, related_name='rss_get')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    url_image = models.CharField(max_length=128, null=True, blank=True)
    url_origin = models.CharField(max_length=128)


class Feed(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    url_image = models.CharField(max_length=128, null=True, blank=True)
    url_origin = models.CharField(max_length=128)