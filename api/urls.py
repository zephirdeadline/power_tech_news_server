from django.urls import path

from api import views
from api.views_api.channel_views import ChannelViews
from api.views_api.natural_rss import NaturalRss
from api.views_api.rss_views import RssViews

urlpatterns = [
    path('rss/', RssViews.as_view({'get': 'list'})),

    path('rss/<int:id_rss>/read/', views.set_as_read),
    path('naturalrss/', NaturalRss.as_view()),
    path('channel/', ChannelViews.as_view({'get': 'list'})),
    path('channel/<pk>/', ChannelViews.as_view({'delete': 'destroy'})),

    path('fetch/', views.fetch),
    path('init/', views.init)
]
