import feedparser
from django.http import HttpResponse
from django.shortcuts import render

# Create your views_api here.
from rest_framework.decorators import api_view
from rest_framework.utils import json

from api.models import Rss, RssStatus, Feed, Channel
from api.tools.initdata import initdata


def init(request):
    initdata()
    return HttpResponse('ok')


@api_view(['GET'])
def set_as_read(request, id_rss):
    status, _ = RssStatus.objects.get_or_create(rss_id=id_rss, user=request.user)
    status.isRead = True
    status.save()
    return HttpResponse()


@api_view(['GET'])
def fetch(request):
    url = request.GET.get('url')
    entries = feedparser.parse(url).entries
    channel = Channel.objects.create(url=url, name=url)
    Feed.objects.create(channel=channel, url_origin='link', description='summary', title='title', date='published')
    return HttpResponse()