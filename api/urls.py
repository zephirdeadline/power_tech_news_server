from django.urls import path

from api.views.channel_views import ChannelViews
from api.views.natural_rss import NaturalRss
from api.views.rss_views import RssViews

urlpatterns = [
    path('rss/', RssViews.as_view({'get': 'list'})),
    path('naturalrss/', NaturalRss.as_view()),
    path('channel/', ChannelViews.as_view({'get': 'list'})),
]
